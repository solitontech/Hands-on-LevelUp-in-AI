# Setup Instructions for Python and AI Learning Path

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
2. Click on "Download Python" (choose the latest version, 3.10 or newer)
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

1. Open VS Code
2. Open the Extensions view by clicking on the Extensions icon in the Activity Bar on the side of the window or pressing `Ctrl+Shift+X` (Windows/Linux) or `Cmd+Shift+X` (macOS)
3. Search for and install the following extensions:
   - **Python** (by Microsoft)
   - **Jupyter** (by Microsoft)
   - **Pylance** (by Microsoft)

## 4. Setting Up a Virtual Environment

A virtual environment isolates your project dependencies from your system Python. You can use either the traditional venv approach or UV's built-in virtual environment management.

### Option A: Using Python's venv module

#### Windows
```powershell
# Navigate to your project folder
cd path\to\your\project

# Check which Python version you have installed
python --version

# Create a virtual environment (using default python)
python -m venv venv

# List all Python installations on your system
 ## Command - where python
# If you have multiple Python versions, you can:
# Use 'where python' to list all available Python installations and select the appropriate one from the output.
# For example: C:\Python311\python.exe -m venv venv

# Activate the virtual environment
.\venv\Scripts\activate
```

#### macOS/Linux
```bash
# Navigate to your project folder
cd path/to/your/project

# Check which Python version you have installed
python3 --version

# Create a virtual environment (using default python3)
python3 -m venv venv

# If you have multiple Python versions, you can specify the full path
# For example: /usr/bin/python3.11 -m venv venv
# Or check available versions: ls /usr/bin/python*

# Activate the virtual environment
source venv/bin/activate
```

### Option B: Using UV's virtual environment management (after installing UV)

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

## 5. Installing and Using UV for Package Management

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

### Installing Required Python Packages with UV

With your virtual environment activated, install the necessary packages:

```bash
uv pip install numpy pandas matplotlib scikit-learn jupyter
```

## 6. Cloning the Learning Content Repository

```bash
# Clone the repository
git clone [repository-url]

# Navigate to the repository folder
cd [repository-name]
```

Replace `[repository-url]` with the actual URL of the provided repository.

## 7. Running Jupyter Notebooks in VS Code

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