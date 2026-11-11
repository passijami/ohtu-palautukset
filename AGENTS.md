# Repository guidance

- This repository is a set of independent weekly exercises, not a root-level Python workspace. Run `uv` and test commands from the specific exercise directory containing its `pyproject.toml` and `uv.lock`; Python projects require Python 3.14.
- `viikko2/kopio/` contains copies of earlier exercises. Treat each copy as its own project and avoid assuming changes should be mirrored to the original.

## Focused checks

- `viikko1/riippuvuuksien-injektointi`: `uv run pytest src/tests`
- `viikko1/nhl-statistics`: `uv run pytest src/tests`
- `viikko2/nhl-reader`: `uv run pylint src`
- `viikko3/hello-robot`: `uv run robot src/tests`
- `viikko3/viikko3/login` is a `uv` project; run commands from that directory using `uv run ...`. Start the app with `uv run python src/index.py`; it serves on port `5001`. Keep it running while Robot Framework tests execute with `uv run robot src/tests` in another terminal. Tests use a visible Chromium browser by default.
- Login project registration validation (required fields, username/password lengths, uniqueness, and password confirmation) is in `src/services/user_service.py`, method `validate`. Login credential checks are in the same file, method `check_credentials`.

Robot Framework projects emit `output.xml`, `log.html`, and `report.html` in the project directory; these are generated test artifacts.
