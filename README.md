# python-scripting

A small Python script that finds the game folders in a messy directory
and copies them into a clean one, using only the standard library.

## What it does

The `data/` folder mixes game folders with unrelated files (`a.py`,
`b.py`, `info.txt`, ...). `get_game_data.py`:

1. **Finds the games.** Any folder directly inside the source folder with
   `game` in its name.
2. **Copies them into the target folder**, dropping the `_game` suffix
   (`hello_world_game` becomes `hello_world`). Existing copies are
   replaced.

Planned: write a `metadata.json`, then compile and run each Go game.

## Project structure

```
.
├── get_game_data.py   # the script
├── project.txt        # assumptions and requirements
├── pyproject.toml     # project + ruff/pyright config
└── data/              # input: games mixed with unrelated files
```

## Requirements

- Python 3.12+
- [uv](https://docs.astral.sh/uv/)

## Usage

```bash
uv run python get_game_data.py <source_folder> <target_folder>
# example
uv run python get_game_data.py data game
```

## Checks

```bash
uv run ruff format .
uv run ruff check .
uv run pyright
```

## Credit

Based on the [Python Scripting Project](https://github.com/techwithtim/Python-Scripting-Project)
tutorial by Tech With Tim.
