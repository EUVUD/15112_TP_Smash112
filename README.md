# Smash112

Smash112 is a CMU Graphics platform fighting game with local multiplayer, a
behavior-tree AI mode, and a small gameplay log QA agent extension.

## Project Structure

```text
.
├── src/                         # CMU Graphics game source
├── Graphics/                    # Runtime sprites and backgrounds
├── tools/game_log_agent/        # Log analyzer and report generator
├── tests/                       # Lightweight QA-agent tests
├── docs/ai_resources/           # Behavior tree reference material
├── docs/course_artifacts/       # Local course exports and demos, ignored by git
├── pyproject.toml               # Python project metadata
└── requirements.txt             # Runtime dependency list
```

`src/` and `Graphics/` intentionally stay at the repository root because the
game's image paths are relative to running from `src`.

## Run The Game

```bash
cd src
python3 Game_Basics.py
```

Dependency:

```bash
pip install -r requirements.txt
```

## Gameplay Log QA Agent

During a match, press `o` to export a real gameplay log. The game also exports
automatically when a round ends.

The latest generated log is written to:

```text
tools/game_log_agent/generated_logs/latest_game_log.json
```

Analyze a generated log:

```bash
python3 tools/game_log_agent/analyzer.py tools/game_log_agent/generated_logs/latest_game_log.json --print
```

Analyze a sample log:

```bash
python3 -m tools.game_log_agent tools/game_log_agent/sample_logs/stuck_bug.json --print
```

The analyzer detects suspicious patterns such as stuck movement, negative health,
repeated collision errors, AI idle loops, and confirmed hits that do not apply
damage.

## Tests

```bash
python3 -m unittest discover -s tests
```
