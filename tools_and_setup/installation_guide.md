# 🛠️ Tools & Setup Guide

Complete installation and configuration guide for all MLOps tools used in this program.

---

## 📋 Prerequisites

### System Requirements
- **OS**: Windows 10/11, macOS, or Linux
- **RAM**: Minimum 8GB (16GB recommended)
- **Storage**: At least 20GB free space
- **Internet**: Stable connection for downloads

---

## 🐍 Python Setup

### Install Python 3.9+

**Windows**:
```powershell
# Using Chocolatey
choco install python --version=3.9.13

# Or download from python.org
# https://www.python.org/downloads/
```

**macOS**:
```bash
# Using Homebrew
brew install python@3.9
```

**Linux (Ubuntu/Debian)**:
```bash
sudo apt update
sudo apt install python3.9 python3.9-venv python3-pip
```

### Verify Installation
```bash
python --version
# Should show Python 3.9.x or higher

pip --version
# Should show pip version
```

---

## 📦 Virtual Environment Setup

### Create Project Environment

```bash
# Navigate to MLOps directory
cd c:/Users/asidd/Desktop/Data_science_projects/MLOps

# Create virtual environment
python -m venv mlops_env

# Activate environment
# Windows:
mlops_env\\Scripts\\activate

# macOS/Linux:
source mlops_env/bin/activate
```

### Verify Activation
```bash
# Your prompt should show (mlops_env)
which python  # macOS/Linux
where python  # Windows
# Should point to mlops_env directory
```

---

## 📚 Core Python Packages

### Create requirements.txt

Create a file `requirements.txt` in your MLOps directory:

```text
# Core Components
numpy>=1.24.3
pandas>=2.0.3
scikit-learn>=1.3.0
matplotlib>=3.7.2
seaborn>=0.12.2

# Deep Learning
torch>=2.0.1
torchvision>=0.15.2

# MLOps Tools
mlflow>=2.5.0
dvc>=3.15.0
wandb>=0.15.5
evidently>=0.4.0
prometheus-client>=0.17.1

# Data Engineering
pyspark>=3.4.1
feast>=0.32.0
prefect>=2.11.0

# API & Deployment
fastapi>=0.100.0
uvicorn[standard]>=0.23.1
pydantic>=2.1.1
onnx>=1.14.0
onnxruntime>=1.15.1

# Testing & Dev
pytest>=7.4.0
hydra-core>=1.3.2
typer>=0.9.0
python-dotenv>=1.0.0
requests>=2.31.0
jupyterlab>=4.0.3

```

### Install Packages
```bash
pip install -r requirements.txt
```

This may take 5-10 minutes. ☕

---

## 🐳 Docker Setup

### Install Docker Desktop

**Windows & macOS**:
1. Download from [docker.com](https://www.docker.com/products/docker-desktop/)
2. Run installer
3. Restart computer
4. Launch Docker Desktop

**Linux (Ubuntu)**:
```bash
# Update apt
sudo apt update

# Install dependencies
sudo apt install apt-transport-https ca-certificates curl software-properties-common

# Add Docker GPG key
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

# Add Docker repository
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# Install Docker
sudo apt update
sudo apt install docker-ce docker-ce-cli containerd.io

# Start Docker
sudo systemctl start docker
sudo systemctl enable docker

# Add user to docker group (to run without sudo)
sudo usermod -aG docker $USER
```

### Verify Docker Installation
```bash
docker --version
# Should show Docker version 20.x or higher

docker run hello-world
# Should download and run test container
```

---

## 📝 Git Configuration

### Install Git

**Windows**:
```powershell
choco install git
```

**macOS**:
```bash
brew install git
```

**Linux**:
```bash
sudo apt install git
```

### Configure Git
```bash
# Set your name and email
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# Set default branch name
git config --global init.defaultBranch main

# Verify configuration
git config --list
```

---

## 🗄️ DVC (Data Version Control) Setup

### Install DVC

```bash
# Already installed via requirements.txt
# Or install separately:
pip install dvc
```

### Configure DVC with Cloud Storage (Optional)

**For Google Cloud Storage**:
```bash
pip install dvc[gs]
```

**For AWS S3**:
```bash
pip install dvc[s3]
```

**For Azure Blob**:
```bash
pip install dvc[azure]
```

### Initialize DVC in Project
```bash
# We'll do this in Module 3
# dvc init
```

---

## 📊 MLflow Setup

### Install MLflow
```bash
# Already installed via requirements.txt
# Or:
pip install mlflow
```

### Test MLflow UI
```bash
mlflow ui

# Navigate to http://localhost:5000
# Press Ctrl+C to stop
```

---

## 🎯 Weights & Biases Setup

### Create Account

1. Visit [wandb.ai](https://wandb.ai/)
2. Sign up (free tier available)
3. Get your API key

### Install wandb
```bash
# Already installed via requirements.txt
# Or:
pip install wandb
```

### Login to W&B
```bash
wandb login

# Paste your API key when prompted
# Find it at: https://wandb.ai/authorize
```

### Test Installation
```python
import wandb

# Test login
wandb.login()

print("W&B is configured successfully!")
```

---

## 🧪 Verify All Installations

Create a test script `test_setup.py`:

```python
#!/usr/bin/env python
"""
Test script to verify all MLOps tools are installed correctly.
"""

import sys

def test_imports():
    """Test all critical imports."""
    packages = {
        'numpy': 'NumPy',
        'pandas': 'Pandas',
        'sklearn': 'Scikit-learn',
        'torch': 'PyTorch',
        'mlflow': 'MLflow',
        'wandb': 'Weights & Biases',
        'fastapi': 'FastAPI',
        'uvicorn': 'Uvicorn',
    }
    
    results = []
    for package, name in packages.items():
        try:
            __import__(package)
            results.append(f"✅ {name}")
        except ImportError:
            results.append(f"❌ {name} - NOT INSTALLED")
    
    return results

def test_command_tools():
    """Test command-line tools."""
    import subprocess
    
    tools = {
        'git': ['git', '--version'],
        'docker': ['docker', '--version'],
        'dvc': ['dvc', 'version'],
    }
    
    results = []
    for tool, cmd in tools.items():
        try:
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=5)
            if result.returncode == 0:
                version = result.stdout.strip().split('\\n')[0]
                results.append(f"✅ {tool.upper()}: {version}")
            else:
                results.append(f"❌ {tool.upper()} - NOT WORKING")
        except Exception as e:
            results.append(f"❌ {tool.upper()} - NOT INSTALLED")
    
    return results

if __name__ == "__main__":
    print("🔍 MLOps Tools Installation Check\\n")
    print("=" * 60)
    
    print("\\n📦 Python Packages:")
    print("-" * 60)
    for result in test_imports():
        print(result)
    
    print("\\n🛠️  Command-Line Tools:")
    print("-" * 60)
    for result in test_command_tools():
        print(result)
    
    print("\\n" + "=" * 60)
    print("\\nPython version:", sys.version)
    print("\\n✨ Setup verification complete!")
```

Run the test:
```bash
python test_setup.py
```

---

## 🎯 IDE Setup (Optional but Recommended)

### VS Code

**Install**:
- Download from [code.visualstudio.com](https://code.visualstudio.com/)

**Recommended Extensions**:
- Python (Microsoft)
- Jupyter (Microsoft)
- Docker (Microsoft)
- GitLens
- YAML
- Markdown All in One

**Configure Python Interpreter**:
1. Open Command Palette (`Ctrl+Shift+P` / `Cmd+Shift+P`)
2. Type "Python: Select Interpreter"
3. Choose the `mlops_env` environment

---

## 📁 Directory Structure Check

Run this to verify folder structure:

```bash
# Windows
tree /F /A

# macOS/Linux
tree -L 2
```

Expected output:
```
MLOps/
├── README.md
├── resources/
│   ├── reference_links.md
│   └── cheatsheets/
├── module_01_foundations/
├── module_02_ml_lifecycle/
├── module_03_reproducibility/
├── module_04_advanced_tooling/
├── capstone_project/
└── tools_and_setup/
```

---

## 🆘 Troubleshooting

### Common Issues

**Issue**: `pip install` fails
- **Solution**: Upgrade pip: `python -m pip install --upgrade pip`

**Issue**: Docker won't start
- **Solution**: 
  - Windows: Enable virtualization in BIOS
  - macOS: Give Docker Desktop permissions
  - Linux: Check `docker` service status

**Issue**: Permission denied (Linux/macOS)
- **Solution**: Use `sudo` or fix permissions on directories

**Issue**: Import errors in Jupyter
- **Solution**: Ensure kernel is using correct environment
  ```bash
  python -m ipykernel install --user --name=mlops_env
  ```

---

## ✅ Setup Complete!

If all tests pass, you're ready to start the learning program!

**Next Steps**:
1. Activate your virtual environment
2. Start Jupyter Lab: `jupyter lab`
3. Open Module 1 → Lesson 1

**Need Help?**
- Check tool documentation links in [reference_links.md](../resources/reference_links.md)
- Google error messages (they're usually well-documented)
- Check relevant GitHub issues/Stack Overflow

---

**Happy Learning! 🚀**
