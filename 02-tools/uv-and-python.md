# uv and Modern Python Environment Management

`uv` is an extremely fast Python package and project manager written in Rust by Astral. It consolidates Python version installation, virtual environment management, dependency resolution, and script execution into a single tool.

---

## 1. Why uv Replaces Traditional Tooling

- **Speed:** 10x–100x faster than `pip` and `virtualenv` due to global caching and multi-threaded parallel downloads.
- **Python Version Management:** Replaces tools like `pyenv`. You can install and pin exact Python versions on demand (`uv python install 3.12`).
- **Deterministic Lockfiles:** Provides cargo-like lockfiles (`uv.lock`) ensuring identical environments across team members and CI/CD servers.
- **Drop-in Compatibility:** Provides a `uv pip` interface that works as an exact, high-speed replacement for classic `pip` commands.

---

## 2. Essential Commands

### Python Version Management
```bash
# List available and installed Python versions
uv python list

# Install Python 3.12
uv python install 3.12

# Pin local directory to Python 3.12
uv python pin 3.12
```

### Virtual Environments
```bash
# Create a virtual environment using Python 3.12 in .venv
uv venv --python 3.12

# Activate the virtual environment
# Linux / macOS:
source .venv/bin/activate
# Windows PowerShell:
.venv\Scripts\Activate.ps1
```

### Running Commands in Isolated Environments
You do not even need to manually activate `.venv`. `uv run` executes scripts directly within the project environment:
```bash
uv run python main.py
uv run pytest tests/
```

### Managing Dependencies in Projects
```bash
# Initialize a new Python project with pyproject.toml
uv init my-project
cd my-project

# Add runtime dependencies
uv add fastapi "uvicorn[standard]" pydantic

# Add development-only dependencies
uv add --dev pytest ruff mypy

# Generate or update uv.lock
uv lock

# Synchronize the environment to match uv.lock exactly
uv sync
```

### Classic pip-style Operations
```bash
# Install a package into the active virtual environment
uv pip install requests

# Install from requirements.txt
uv pip install -r requirements.txt

# Export locked dependencies
uv pip compile pyproject.toml -o requirements.txt
```
