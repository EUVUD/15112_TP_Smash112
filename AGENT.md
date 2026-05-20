# Agent Guide

## Project Overview

Smash112 is a CMU Graphics platform fighting game. It supports local multiplayer and an AI mode where player 2 is controlled by a hand-built behavior tree.

The game flow is:

1. Start screen
2. Multiplayer or AI mode selection
3. Field selection
4. Character selection
5. Instruction screen
6. Fight screen

## How To Run

Run the game from the `src` directory so relative image paths like `../Graphics/...` resolve correctly:

```bash
cd src
python3 Game_Basics.py
```

Dependency:

- `cmu_graphics`

There is no requirements file yet. If adding one, keep it minimal and include `cmu_graphics`.

## Important Files

- `src/Game_Basics.py`: Main CMU Graphics app, screen flow, input handlers, drawing, combat, physics, cooldowns, projectiles, and game-over logic.
- `src/Game_Char.py`: Character and projectile classes, sprite path lists, character-specific image assets.
- `src/Game_Field.py`: Field/block definitions and AI jump points for platform navigation.
- `src/BT.py`: Behavior tree construction for the AI player.
- `src/BT_Composite.py`: `Selector` and `Sequence` composite node implementations.
- `src/BT_Behavior.py`: `Condition` and `Action` behavior node wrappers.
- `Graphics/`: Character, background, projectile, and instruction assets.
- `AI_Resources/`: Reference material for behavior trees.

## Behavior Tree Notes

The AI player is `app.player2`. In AI mode, `game_onStep` calls:

```python
BT.btAiPlayer(app).tick()
```

`btAiPlayer(app)` builds a root `Selector` with two high-level behaviors:

- Shoot logic: checks projectile cooldown, then tries same-height shooting or jump-shooting.
- Attack logic: checks attack cooldown, then attacks if close, navigates toward jump points if the human is higher, or walks toward the human.

Behavior node return values are strings:

- `'Success'`
- `'Failure'`
- `'Running'`

Keep those exact values unless you refactor all tree nodes together.

Composite semantics:

- `Selector`: returns the first child that succeeds or is running; fails only if every child fails.
- `Sequence`: fails on the first failing child; runs on the first running child; succeeds only if every child succeeds.

## Game State Conventions

Most state lives on the CMU Graphics `app` object. Important fields include:

- `app.aiMode`: `True` for AI mode, otherwise local multiplayer.
- `app.selectedField`: current `Field`, including blocks and jump points.
- `app.player1`, `app.player2`: active `Char` instances.
- `app.projection`: shared projectile list.
- `app.pause`, `app.gameOver`: game state flags.
- Sprite indices such as `app.player1StandInd`, `app.player2WalkInd`, and bullet indices.
- `app.closetJumpPoint`: current AI jump target. The spelling is currently `closet`, not `closest`; avoid changing it casually because it is used across the AI code.

Character state conventions:

- `x`, `y`: character center position for drawing and collisions.
- `dx`, `dy`: movement velocity.
- `jump`: `True` while airborne.
- `walk`, `attack`, `attackAni`, `defend`, `antiDefend`, `antiDefendAni`: animation/action flags.
- `attackCD`, `shuriCD`, `antiDefCD`: cooldown counters decremented in `attackCD(app)`.
- `health`: starts at `5`; `bloodFixed(app)` clamps defeated players to `0.1`, and game-over checks use `0.1`.

## Assets And Paths

Sprite and background paths are relative to `src`, for example `../Graphics/Background/beginBg.webp`. When adding assets:

- Put them under `Graphics/`.
- Follow existing folder naming for character sprites.
- Make sure generated sprite lists in `Game_Char.py` match the actual frame numbers.
- Do not move `Graphics/` unless you also update every image path.

## Gameplay Editing Guidelines

- Keep player 1 human-controlled and player 2 AI-controlled in AI mode.
- Be careful changing collision geometry: field blocks are used both for drawing and physics.
- If changing platform layouts in `Game_Field.py`, also update that field's `jumpPoint` list so the AI can navigate upward.
- If changing action cooldowns, check both player controls and AI behavior so neither side can spam or stall unexpectedly.
- If changing sprite counts, update animation modulo logic and character sprite list ranges together.
- Avoid broad rewrites of the CMU Graphics screen structure unless the task specifically asks for it.

## Coding And Collaboration Rules

- Keep generated code changes small enough for a human reviewer to inspect comfortably.
- Do not produce a huge block of new code, documentation, or explanation in a single response unless the user explicitly asks for a complete artifact.
- Prefer incremental edits: inspect the relevant files, explain the intended change briefly, then patch only the necessary section.
- When adding or changing behavior tree logic, describe the new node order and expected return statuses before or alongside the code change.
- Avoid silently rewriting unrelated code. If a change touches multiple systems, separate the work into reviewable pieces.
- Ask for human review before broad refactors, major AI behavior changes, large asset reorganizations, or changes that alter player controls/game balance.
- Preserve human agency in reviews: summarize what changed, why it changed, and which files/behaviors should be checked manually.
- Do not hide important implementation details behind vague summaries. Keep summaries concise, but include enough detail for the reviewer to verify the work.

## Testing Checklist

Manual smoke test after gameplay or AI changes:

1. Start the game from `src`.
2. Enter multiplayer mode and confirm both players can move, jump, attack, defend, anti-defend, and shoot.
3. Enter AI mode and confirm player 2 approaches, jumps toward platforms when needed, attacks, and shoots.
4. Try each field once if field, physics, or AI navigation changed.
5. Confirm projectiles disappear at screen edges, on block collision, and after hitting players.
6. Confirm game-over and restart with `r`.

## Style Notes

- The codebase uses simple classes and module-level helper functions.
- Prefer small, local changes over new abstractions.
- Keep comments concise and useful.
- Preserve existing asset credits in comments and documentation.
