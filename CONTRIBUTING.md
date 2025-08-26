# Contributing

Thanks for your interest in contributing! Please follow these steps:

- Fork the repository and create your branch from `main`.
- If you've added code, add tests where reasonable.
- Ensure the linter passes and the app starts locally.
- Open a Pull Request with a clear title and description.

## Development setup

1) Create a virtual environment and install dependencies

```powershell
python -m venv .venv; .\.venv\Scripts\Activate.ps1; pip install -r requirements.txt
```

2) Run API locally

```powershell
python app.py
```

3) Run a quick prediction

```powershell
python demo.py
```

## Code style

- Follow PEP8 where applicable.
- Keep functions small and focused.
- Document public functions and classes with docstrings.

## Commit messages

Use conventional commits where possible:

- feat: add a new feature
- fix: bug fix
- docs: documentation only changes
- chore: tooling, build, CI, etc.
