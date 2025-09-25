# Setup Instructions for Python

Congratulations on taking this amazing step to level up your skills! Get ready for an exciting Python and AI learning journey ahead! You've got this! 🚀

This guide will help you set up your development environment for the Python and AI weekly learning content. Follow these steps to install and configure all necessary tools.

## 1. Installing Visual Studio Code

VS Code is a lightweight but powerful source code editor that runs on your desktop.

### Windows
1. Visit the [VS Code download page](https://code.visualstudio.com/download)
2. Click on the Windows download button
3. Run the installer (.exe file) that you downloaded
4. Follow the installation wizard (use default settings)
5. Launch VS Code after installation

### macOS
1. Visit the [VS Code download page](https://code.visualstudio.com/download)
2. Click on the macOS download button
3. Open the downloaded .zip file
4. Drag Visual Studio Code.app to the Applications folder
5. Launch VS Code from your Applications folder

### Linux
1. Visit the [VS Code download page](https://code.visualstudio.com/download)
2. Download the appropriate package for your distribution
3. Install using your package manager:
   - Debian/Ubuntu: `sudo apt install ./downloaded-package.deb`
   - RHEL/Fedora/CentOS: `sudo rpm -i downloaded-package.rpm`
4. Launch VS Code from your applications menu or terminal

## 2. Installing Python

### Windows
1. Visit the [Python downloads page](https://www.python.org/downloads/)
2. Click on "Download Python" (choose the latest stable version, 3.12.6)
3. Run the installer
4. **Important**: Check the box that says "Add Python to PATH"
5. Click "Install Now"
6. Verify installation by opening Command Prompt and typing:
   ```
   python --version
   ```

### macOS
1. Install Homebrew if you don't have it:
   ```
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```
2. Install Python using Homebrew:
   ```
   brew install python
   ```
3. Verify installation by opening Terminal and typing:
   ```
   python3 --version
   ```

### Linux
1. Most Linux distributions come with Python pre-installed
2. If not, install it using your package manager:
   - Debian/Ubuntu: `sudo apt update && sudo apt install python3 python3-pip`
   - RHEL/Fedora/CentOS: `sudo dnf install python3 python3-pip`
3. Verify installation by opening Terminal and typing:
   ```
   python3 --version
   ```

## 3. Installing Required VS Code Extensions

VS Code extensions are add-ons that enhance the editor's functionality for specific programming languages, frameworks, and tools.They provide features like syntax highlighting, code completion, debugging capabilities, and specialized tools that make development easier and more efficient. Extensions allow you to customize VS Code to create an ideal environment for your specific programming needs.

For our Python and AI learning path, we'll need several key extensions that will provide essential Python development features:

1. Open VS Code
2. Open the Extensions view by clicking on the Extensions icon in the Activity Bar on the side of the window or pressing `Ctrl+Shift+X` (Windows/Linux) or `Cmd+Shift+X` (macOS)
3. Search for and install the following extensions:
   - **Python** (by Microsoft) - Provides Python language support, debugging, and Jupyter notebook integration
   - **Jupyter** (by Microsoft) - Allows you to create and run Jupyter notebooks directly within VS Code
   - **Pylance** (by Microsoft) - Offers advanced Python language features like type checking and intelligent code completion

## 4. Installing and Using UV for Package Management

UV is a modern Python package manager that's significantly faster than pip. It provides improved dependency resolution and installation speed.

### Installing UV

With your virtual environment activated:

#### Windows
```powershell
# Install UV using pip
pip install uv
# Verify installation
uv --version
```

#### macOS/Linux
```bash
# Install UV using pip
pip install uv

# Verify installation
uv --version
```

## 5. Setting Up a Virtual Environment

A virtual environment isolates your project dependencies from your system Python. You can use either the traditional venv approach or UV's built-in virtual environment management.

### Using UV's virtual environment management (after installing UV)

#### Windows/macOS/Linux
```bash
# Navigate to your project folder
cd path/to/your/project

# Create and activate a virtual environment with UV
uv venv

# Similar to the venv approach, you can also specify a specific Python version with UV
# For example: uv venv --python python3.11
# Or specify the full path: uv venv --python C:\Python311\python.exe (Windows)
# Or on macOS/Linux: uv venv --python /usr/bin/python3.11

# On Windows
.venv\Scripts\activate

# On macOS/Linux
source .venv/bin/activate
```

# Repository Setup

## 1. Cloning the Learning Content Repository

```bash
# Clone the repository
git clone [repository-url]

# Navigate to the repository folder
cd [repository-name]

# Create and activate venv with uv
uv venv

# Install the packages from the pyproject.toml
uv pip install -e .

# To add custom packages
uv add <package_name>

```

Replace `[repository-url]` with the actual URL of the provided repository.

### Essential Git Commands

Here are the key Git commands you'll use most frequently:

1. **git pull**: Update your local repository with the latest learning materials and examples. This is the command you'll use most often to get new content.
   ```bash
   git pull
   ```

2. **git status**: Check if your local repository is up-to-date or if there are new changes available.
   ```bash
   git status
   ```

3. **git log**: View the history of updates to the learning materials.
   ```bash
   # View recent commits
   git log --oneline -n 5
   ```

4. **git checkout**: Switch to specific versions of learning materials or examples if needed.
   ```bash
   # Checkout a specific file from the repository
   git checkout origin/main -- path/to/file.py
   ```

## 2. Running Jupyter Notebooks in VS Code

1. Open VS Code
2. Open the project folder: `File > Open Folder` and select the cloned repository folder
3. Navigate to the `notebooks` folder in the Explorer view
4. Open `python_basics.ipynb`
5. In the top right corner, select the Python interpreter from your virtual environment
6. You can now run cells by clicking the play button to the left of each cell or by pressing `Shift+Enter`

## Troubleshooting

### Python not found
- Make sure Python is added to your PATH
- Try using `python3` instead of `python` on macOS/Linux

### Jupyter not working
- Make sure you've installed the Jupyter extension for VS Code
- Try reinstalling the Jupyter package: `uv pip install --upgrade jupyter`

### Package installation errors
- Make sure your virtual environment is activated
- Try using UV to install packages: `uv pip install <package-name>`
- If UV is having issues, try reinstalling it
- On Windows, you might need Visual C++ build tools for some packages: [Microsoft C++ Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/)

### UV specific issues
- If UV commands aren't found, ensure it's properly installed and in your PATH
- For dependency conflicts, try `uv pip install --resolution=highest <package-name>` to get the latest compatible versions

## Need Help?

If you encounter any issues during setup, please contact your team coordinator for assistance.

Happy coding!