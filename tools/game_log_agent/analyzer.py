"""Rule-based gameplay log analyzer for Smash112.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any

try:
    from .report_generator import generate_markdown_report
except ImportError:
    from report_generator import generate_markdown_report


MOVE_ACTIONS = {
    "move",
    "move_left",
    "move_right",
    "walk",
    "walk_left",
    "walk_right",
    "approach",
    "jump",
}

IDLE_ACTIONS = {"idle", "none", "wait", "stand"}

HIT_EVENTS = {"attack_hit", "projectile_hit", "hit_confirmed"}


@dataclass
class Finding:
    rule_id: str
    title: str
    severity: str
    evidence: list[str]
    possible_modules: list[str]
    suggested_reproduction: str
    start_time: float | int | str | None = None
    end_time: float | int | str | None = None
    raw_events: list[dict[str, Any]] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


def load_log(path: Path) -> list[dict[str, Any]]:
    with path.open("r", encoding="utf-8") as log_file:
        data = json.load(log_file)

    if not isinstance(data, list):
        raise ValueError("Gameplay log must be a JSON list of event objects.")

    for index, event in enumerate(data):
        if not isinstance(event, dict):
            raise ValueError(f"Log entry {index} is not a JSON object.")

    return data


def analyze_log(events: list[dict[str, Any]]) -> list[Finding]:
    findings: list[Finding] = []
    findings.extend(detect_stuck_player(events))
    findings.extend(detect_negative_health(events))
    findings.extend(detect_repeated_collision_error(events))
    findings.extend(detect_ai_idle(events))
    findings.extend(detect_combat_no_damage(events))
    return findings


def detect_stuck_player(
    events: list[dict[str, Any]],
    min_frames: int = 3,
) -> list[Finding]:
    """Find movement attempts where a character's position does not change."""

    findings: list[Finding] = []
    for actor, actor_events in _events_by_actor(events).items():
        run: list[dict[str, Any]] = []
        previous_position: tuple[Any, Any] | None = None

        for event in actor_events:
            position = _position(event)
            if position is None:
                run = []
                previous_position = None
                continue

            if position == previous_position and _has_movement_intent(event):
                if not run:
                    run = [event]
                else:
                    run.append(event)
            else:
                run = [event] if _has_movement_intent(event) else []

            previous_position = position

            if len(run) >= min_frames:
                times = [_time(item) for item in run]
                collision_count = sum(
                    1 for item in run if _event_name(item) == "collision_error"
                )
                findings.append(
                    Finding(
                        rule_id="stuck_player",
                        title=f"Potential Bug: {actor} stuck while moving",
                        severity="medium",
                        evidence=[
                            (
                                f"{actor} stayed at position {position} for "
                                f"{len(run)} consecutive movement frames."
                            ),
                            f"Times: {', '.join(str(time) for time in times)}.",
                            (
                                f"collision_error appeared {collision_count} time(s) "
                                "inside the stuck window."
                            ),
                        ],
                        possible_modules=[
                            "movement update",
                            "collision handling",
                            "platform boundary correction",
                        ],
                        suggested_reproduction=(
                            "Move the character into a wall or platform edge and "
                            "hold the movement key for several frames."
                        ),
                        start_time=times[0],
                        end_time=times[-1],
                        raw_events=run.copy(),
                    )
                )
                break

    return findings


def detect_negative_health(events: list[dict[str, Any]]) -> list[Finding]:
    findings: list[Finding] = []

    for event in events:
        health = _number(event, ["health", "player_health"])
        if health is None:
            actor = _actor(event)
            health = _number(event, [f"{actor}_health"])

        if health is not None and health < 0:
            actor = _actor(event)
            findings.append(
                Finding(
                    rule_id="negative_health",
                    title=f"Potential Bug: {actor} health dropped below zero",
                    severity="high",
                    evidence=[
                        f"{actor} health was {health} at t={_time(event)}.",
                        "Smash112 game-over logic expects health to be clamped near zero.",
                    ],
                    possible_modules=[
                        "damage application",
                        "health clamp",
                        "game-over state handling",
                    ],
                    suggested_reproduction=(
                        "Trigger repeated attacks or projectile hits near the end of a round "
                        "and inspect health after each damage event."
                    ),
                    start_time=_time(event),
                    end_time=_time(event),
                    raw_events=[event],
                )
            )

    return findings


def detect_repeated_collision_error(
    events: list[dict[str, Any]],
    min_count: int = 3,
    max_time_span: float = 5,
) -> list[Finding]:
    findings: list[Finding] = []

    collision_events = [
        event for event in events if _event_name(event) == "collision_error"
    ]
    for actor, actor_events in _events_by_actor(collision_events).items():
        for start_index in range(len(actor_events)):
            window = [actor_events[start_index]]
            start_time = _numeric_time(actor_events[start_index])

            for event in actor_events[start_index + 1 :]:
                if start_time is None or _numeric_time(event) is None:
                    window.append(event)
                elif _numeric_time(event) - start_time <= max_time_span:
                    window.append(event)

                if len(window) >= min_count:
                    times = [_time(item) for item in window]
                    positions = [_position(item) for item in window]
                    findings.append(
                        Finding(
                            rule_id="repeated_collision_error",
                            title=f"Potential Bug: repeated collision errors for {actor}",
                            severity="medium",
                            evidence=[
                                (
                                    f"{len(window)} collision_error events occurred "
                                    f"within {max_time_span:g} seconds/frames."
                                ),
                                f"Times: {', '.join(str(time) for time in times)}.",
                                f"Positions: {positions}.",
                            ],
                            possible_modules=[
                                "collision handling",
                                "block boundary checks",
                                "physics correction",
                            ],
                            suggested_reproduction=(
                                "Move or knock a character into the same platform edge and "
                                "watch whether collision correction repeats every frame."
                            ),
                            start_time=times[0],
                            end_time=times[-1],
                            raw_events=window.copy(),
                        )
                    )
                    return findings

    return findings


def detect_ai_idle(
    events: list[dict[str, Any]],
    min_frames: int = 4,
    min_player_distance: float = 80,
) -> list[Finding]:
    findings: list[Finding] = []
    run: list[dict[str, Any]] = []

    ai_events = [
        event
        for event in events
        if str(event.get("controller", "")).lower() == "ai"
        or str(event.get("actor", "")).lower() in {"ai", "player2_ai"}
    ]

    for event in ai_events:
        if _is_idle_ai_event(event, min_player_distance):
            run.append(event)
        else:
            run = []

        if len(run) >= min_frames:
            times = [_time(item) for item in run]
            distances = [item.get("player_distance") for item in run]
            actor = _actor(run[-1])
            findings.append(
                Finding(
                    rule_id="ai_idle",
                    title=f"Potential Bug: {actor} AI stayed idle too long",
                    severity="medium",
                    evidence=[
                        f"AI produced no movement/action for {len(run)} consecutive frames.",
                        f"Times: {', '.join(str(time) for time in times)}.",
                        f"Player distances: {distances}.",
                    ],
                    possible_modules=[
                        "behavior tree selector",
                        "AI action conditions",
                        "jump-point navigation",
                    ],
                    suggested_reproduction=(
                        "Start AI mode, place the human player outside attack range, "
                        "and observe whether player 2 approaches or stalls."
                    ),
                    start_time=times[0],
                    end_time=times[-1],
                    raw_events=run.copy(),
                )
            )
            break

    return findings


def detect_combat_no_damage(events: list[dict[str, Any]]) -> list[Finding]:
    findings: list[Finding] = []

    for event in events:
        event_name = _event_name(event)
        hit_confirmed = bool(event.get("hit_confirmed"))
        if event_name not in HIT_EVENTS and not hit_confirmed:
            continue

        expected_damage = _number(event, ["damage_expected", "expected_damage"])
        applied_damage = _number(event, ["damage_applied", "applied_damage"])
        before = _number(event, ["target_health_before"])
        after = _number(event, ["target_health_after"])
        target_defending = bool(event.get("target_defending", False))

        expected_positive = expected_damage is None or expected_damage > 0
        health_unchanged = before is not None and after is not None and before == after
        no_damage_applied = applied_damage == 0 or health_unchanged

        if expected_positive and no_damage_applied and not target_defending:
            actor = _actor(event)
            target = event.get("target", "target")
            findings.append(
                Finding(
                    rule_id="combat_no_damage",
                    title="Potential Bug: attack hit did not apply damage",
                    severity="high",
                    evidence=[
                        (
                            f"{actor} hit {target} at t={_time(event)}, "
                            "but damage_applied was 0 or target health did not change."
                        ),
                        f"target_health_before={before}, target_health_after={after}.",
                        f"target_defending={target_defending}.",
                    ],
                    possible_modules=[
                        "combat hit resolution",
                        "damage application",
                        "defense state handling",
                    ],
                    suggested_reproduction=(
                        "Put both players in normal attack range, perform a melee hit, "
                        "and compare target health before and after the hit frame."
                    ),
                    start_time=_time(event),
                    end_time=_time(event),
                    raw_events=[event],
                )
            )

    return findings


def _events_by_actor(events: list[dict[str, Any]]) -> dict[str, list[dict[str, Any]]]:
    grouped: dict[str, list[dict[str, Any]]] = {}
    for event in sorted(events, key=_sort_key):
        grouped.setdefault(_actor(event), []).append(event)
    return grouped


def _actor(event: dict[str, Any]) -> str:
    return str(
        event.get("actor")
        or event.get("player")
        or event.get("character")
        or "player"
    )


def _event_name(event: dict[str, Any]) -> str:
    return str(event.get("event") or event.get("type") or "").lower()


def _time(event: dict[str, Any]) -> float | int | str | None:
    return event.get("time", event.get("frame"))


def _numeric_time(event: dict[str, Any]) -> float | None:
    value = _time(event)
    if isinstance(value, (int, float)):
        return float(value)
    return None


def _sort_key(event: dict[str, Any]) -> tuple[int, float | str]:
    time_value = _time(event)
    if isinstance(time_value, (int, float)):
        return (0, float(time_value))
    return (1, str(time_value))


def _position(event: dict[str, Any]) -> tuple[Any, Any] | None:
    actor = _actor(event)
    x = _value(event, ["x", "player_x", f"{actor}_x"])
    y = _value(event, ["y", "player_y", f"{actor}_y"])
    if x is None or y is None:
        return None
    return (x, y)


def _has_movement_intent(event: dict[str, Any]) -> bool:
    action = str(event.get("action", "")).lower()
    input_value = str(event.get("input", "")).lower()
    dx = _number(event, ["dx"])
    dy = _number(event, ["dy"])

    return (
        action in MOVE_ACTIONS
        or input_value in {"left", "right", "a", "d"}
        or (dx is not None and dx != 0)
        or (dy is not None and dy != 0 and action == "jump")
    )


def _is_idle_ai_event(event: dict[str, Any], min_player_distance: float) -> bool:
    action = str(event.get("action", "")).lower()
    dx = _number(event, ["dx"]) or 0
    dy = _number(event, ["dy"]) or 0
    player_distance = _number(event, ["player_distance"])
    is_far = player_distance is None or player_distance >= min_player_distance
    no_attack = not bool(event.get("attack", False))
    no_projectile = not bool(event.get("shoot", False))

    return action in IDLE_ACTIONS and dx == 0 and dy == 0 and is_far and no_attack and no_projectile


def _number(event: dict[str, Any], keys: list[str]) -> float | int | None:
    value = _value(event, keys)
    if isinstance(value, (int, float)):
        return value
    return None


def _value(event: dict[str, Any], keys: list[str]) -> Any:
    for key in keys:
        if key in event:
            return event[key]
    return None


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Analyze Smash112 gameplay logs and generate a QA report."
    )
    parser.add_argument("log_path", type=Path, help="Path to a JSON gameplay log.")
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        default=Path("bug_report.md"),
        help="Markdown report output path. Defaults to bug_report.md.",
    )
    parser.add_argument(
        "--print",
        action="store_true",
        help="Print the Markdown report instead of writing it to disk.",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Print raw analyzer findings as JSON.",
    )
    return parser.parse_args()


def main() -> None:
    args = _parse_args()
    events = load_log(args.log_path)
    findings = analyze_log(events)

    if args.json:
        print(json.dumps([finding.to_dict() for finding in findings], indent=2))
        return

    report = generate_markdown_report(findings, source_name=str(args.log_path))
    if args.print:
        print(report)
    else:
        args.output.write_text(report, encoding="utf-8")
        print(f"Wrote report to {args.output}")


if __name__ == "__main__":
    main()
