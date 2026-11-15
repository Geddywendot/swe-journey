# Development Environment Setup: Linux

This guide covers Debian/Ubuntu and Fedora/RHEL-based distributions (including WSL 2 environments).

---

## 1. System Packages & Build Essentials

### Debian / Ubuntu
```bash
sudo apt update && sudo apt upgrade -y
sudo apt install -y build-essential curl git unzip pkg-config libssl-dev ca-certificates
```

### Fedora / RHEL
```bash
sudo dnf check-update
sudo dnf groupinstall -y "Development Tools"
sudo dnf install -y curl git unzip openssl-devel
```

---

## 2. Install Git and GitHub CLI

### Debian / Ubuntu
```bash
sudo apt install -y git
# GitHub CLI
type -p curl >/dev/null || (sudo apt update && sudo apt install curl -y)
curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg | sudo dd of=/usr/share/keyrings/githubcli-archive-keyring.gpg
sudo chmod go+r /usr/share/keyrings/githubcli-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null
sudo apt update
sudo apt install -y gh
```

### Configure Git
```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
git config --global init.defaultBranch main
```

---

## 3. Install uv & Python 3.12

Install `uv` via the official standalone installer:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
source ~/.bashrc  # or source ~/.zshrc
```

Verify and install Python 3.12:
```bash
uv --version
uv python install 3.12
```

---

## 4. Install Node.js LTS (via fnm)

```bash
curl -fsSL https://fnm.vercel.app/install | bash
source ~/.bashrc  # or source ~/.zshrc
fnm install --lts
fnm use --lts
node --version
npm --version
```

---

## 5. Install Docker Engine & Docker Compose

Follow the official Docker repository installation for Ubuntu:

```bash
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

sudo apt update
sudo apt install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

# Enable running docker without sudo
sudo usermod -aG docker $USER
newgrp docker
```

Verify Docker:
```bash
docker --version
docker compose version
docker run hello-world
```

---

## 6. Install Visual Studio Code

### Ubuntu (.deb)
```bash
sudo apt install -y software-properties-common apt-transport-https wget
wget -q https://packages.microsoft.com/keys/microsoft.asc -O- | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://packages.microsoft.com/repos/vscode stable main"
sudo apt update
sudo apt install -y code
```
