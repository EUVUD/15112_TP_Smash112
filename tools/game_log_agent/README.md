# Smash112 Game Log Analysis / QA Agent

This is a small standalone QA extension for Smash112. It does not change the
live CMU Graphics game loop. Instead, it analyzes saved gameplay logs and turns
rule findings into developer-readable bug reports.

## Why This Exists

Smash112 started as a gameplay prototype. This tool shows a practical extension
around game tooling, structured data, and agent-style reporting:

1. Deterministic log analysis finds suspicious gameplay patterns.
2. LLM-style report generation turns raw findings into a readable bug report.

The first version uses a deterministic summarizer so it runs without API keys.
The report generator is shaped so a future ChatGPT or Doubao API call can
replace that summarization stage.

## Run

From the repository root:

```bash
python3 tools/game_log_agent/analyzer.py tools/game_log_agent/sample_logs/stuck_bug.json --print
```

Write a Markdown report:

```bash
python3 tools/game_log_agent/analyzer.py tools/game_log_agent/sample_logs/combat_no_damage_bug.json -o bug_report.md
```

Print raw rule findings:

```bash
python3 tools/game_log_agent/analyzer.py tools/game_log_agent/sample_logs/health_bug.json --json
```

## Rules

- `detect_stuck_player`: character tries to move but position stays unchanged.
- `detect_negative_health`: health becomes negative after damage.
- `detect_repeated_collision_error`: collision errors repeat in a short window.
- `detect_ai_idle`: AI-controlled player stays idle while far from the human.
- `detect_combat_no_damage`: hit is confirmed but no damage is applied.

## Log Shape

Each sample log is a JSON list of events. The analyzer accepts simple fields
like these:

```json
{
  "time": 12,
  "actor": "player2",
  "controller": "ai",
  "x": 420,
  "y": 457,
  "health": 5,
  "action": "idle",
  "event": "ai_tick",
  "dx": 0,
  "dy": 0,
  "player_distance": 180
}
```

The analyzer also supports the simpler prototype-style names `player_x`,
`player_y`, and `player_health`.
