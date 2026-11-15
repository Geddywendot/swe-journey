# Development Environment Setup: macOS

This guide configures a macOS development workstation (Apple Silicon M-series or Intel).

---

## 1. Install Xcode Command Line Tools

Open Terminal and run:

```bash
xcode-select --install
```
Follow the graphical prompt to complete the installation.

---

## 2. Install Homebrew

The standard package manager for macOS:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Add Homebrew to your shell environment (for Apple Silicon):
```bash
echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zprofile
eval "$(/opt/homebrew/bin/brew shellenv)"
```

---

## 3. Install Git and GitHub CLI

```bash
brew install git gh
```

Configure your Git identity:
```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
git config --global init.defaultBranch main
```

---

## 4. Install uv (Fast Python Package & Environment Manager)

Install via the official script or Homebrew:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```
Reload your terminal or run `source ~/.zshrc`. Then install Python 3.12:

```bash
uv --version
uv python install 3.12
```

---

## 5. Install Node.js LTS

Install `fnm` (Fast Node Manager) to manage Node versions:

```bash
brew install fnm
echo 'eval "$(fnm env --use-on-cd)"' >> ~/.zshrc
source ~/.zshrc
fnm install --lts
fnm use --lts
node --version
npm --version
```

---

## 6. Install Docker Desktop

```bash
brew install --cask docker
```
Launch Docker from Applications, grant required system permissions, and verify:
```bash
docker --version
docker compose version
```

---

## 7. Install Visual Studio Code

```bash
brew install --cask visual-studio-code
```

Verify command line integration:
```bash
code --version
```
*(If `code` is not found, launch VS Code, press `Cmd + Shift + P`, and select **Shell Command: Install 'code' command in PATH**).*
