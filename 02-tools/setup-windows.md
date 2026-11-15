# Development Environment Setup: Windows

This guide establishes a production-grade development workstation on Windows 10/11. The recommended approach is using **WSL 2 (Windows Subsystem for Linux)** with Ubuntu, which provides a native Linux environment for Python, Docker, and terminal tooling.

---

## 1. Prerequisites: WSL 2 (Recommended Path)

Open Windows PowerShell as Administrator and run:

```powershell
wsl --install
```

After restarting your computer, launch Ubuntu from the Start Menu, create your Linux username and password, and update packages:

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install -y build-essential curl git unzip pkg-config libssl-dev
```

*Note: Once WSL 2 is installed, follow `02-tools/setup-linux.md` inside your Ubuntu terminal for uv, Python, and Node setup.*

---

## 2. Native Windows Path (Alternative)

If you prefer working natively in Windows without WSL:

### Install Winget / Package Manager
Ensure `winget` is available (included by default in modern Windows 10/11).

### Install Git for Windows
```powershell
winget install --id Git.Git -e --source winget
```
During installation, select **Use Git from the command prompt and also from 3rd-party software** and choose **Checkout as-is, commit Unix-style line endings (`core.autocrlf = input`)**.

### Install Visual Studio Code
```powershell
winget install --id Microsoft.VisualStudioCode -e --source winget
```

### Install uv (Python Package and Version Manager)
Run in PowerShell:
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```
Verify installation:
```powershell
uv --version
uv python install 3.12
```

### Install Node.js LTS
Install via `fnm` (Fast Node Manager) or winget:
```powershell
winget install Schniz.fnm
fnm install --lts
fnm use --lts
node -v
npm -v
```

### Install Docker Desktop
```powershell
winget install --id Docker.DockerDesktop -e --source winget
```
- During setup, enable **Use WSL 2 instead of Hyper-V (recommended)**.
- Start Docker Desktop and verify in terminal:
  ```powershell
  docker --version
  docker compose version
  ```

---

## 3. Verify All Tools

Open a fresh terminal and confirm:
```powershell
git --version
uv --version
node --version
docker --version
code --version
```
