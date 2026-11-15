# Visual Studio Code Configuration

A calibrated VS Code setup tailored for Python, TypeScript, React, and Docker fullstack workflows.

---

## 1. Recommended Extensions

Install these extensions via the Extensions tab (`Ctrl+Shift+X` or `Cmd+Shift+X`):

### Python & Backend
- **Python** (`ms-python.python`): Rich Python support, debugging, and interpreter switching.
- **Pylance** (`ms-python.vscode-pylance`): High-performance static type analysis.
- **Ruff** (`charliermarsh.ruff`): Extremely fast Python linter and formatter.

### Frontend & Web
- **ESLint** (`dbaeumer.vscode-eslint`): Integrates ESLint for TypeScript/JavaScript code analysis.
- **Prettier - Code Formatter** (`esbenp.prettier-vscode`): Enforces consistent code formatting.
- **Tailwind CSS IntelliSense** (`bradlc.vscode-tailwindcss`): Autocomplete and class linting.

### DevOps & Data
- **Docker** (`ms-azuretools.vscode-docker`): Syntax highlighting, container and image inspection.
- **PostgreSQL** (`ckolkman.vscode-postgres`): Database connection and query execution in editor.
- **Even Better TOML** (`tamasfe.even-better-toml`): Syntax highlighting and validation for `pyproject.toml`.

---

## 2. Recommended Workspace Settings

Place the following configuration in `.vscode/settings.json`:

```json
{
  "editor.formatOnSave": true,
  "editor.codeActionsOnSave": {
    "source.fixAll": "explicit",
    "source.organizeImports": "explicit"
  },
  "editor.rulers": [88, 100],
  "editor.tabSize": 2,

  "[python]": {
    "editor.tabSize": 4,
    "editor.defaultFormatter": "charliermarsh.ruff"
  },
  "[typescript]": {
    "editor.defaultFormatter": "esbenp.prettier-vscode"
  },
  "[typescriptreact]": {
    "editor.defaultFormatter": "esbenp.prettier-vscode"
  },
  "[json]": {
    "editor.defaultFormatter": "esbenp.prettier-vscode"
  },

  "python.analysis.typeCheckingMode": "standard",
  "python.analysis.autoImportCompletions": true,
  "files.trimTrailingWhitespace": true,
  "files.insertFinalNewline": true
}
```

---

## 3. Selecting the uv Virtual Environment

1. Press `Ctrl+Shift+P` (or `Cmd+Shift+P` on macOS).
2. Type and select: **Python: Select Interpreter**.
3. Choose the `.venv` created by `uv` in your project folder (e.g., `./.venv/bin/python`).
