# Quick Start for OpenAI Bytes

Follow this setup to open the notebook and send your first API call. Refer to [`setup_instructions.md`](setup_instructions.md) for deeper dives into Git, package management, or troubleshooting.

## 1. Prerequisites
- Python 3.11+ installed
- `uv` package manager available (`pip install uv` if missing)
- OpenAI API key with access to GPT-5/GPT-4 series models

## 2. Clone and Activate the Project
1. Clone the repository:
	```bash
	git clone https://github.com/solitontech/Hands-on-LevelUp-in-AI.git
	```
2. Move into the project directory:
	```bash
	cd Hands-on-LevelUp-in-AI
	```
3. Create a virtual environment:
	```bash
	python -m venv .venv
	```
4. Activate the environment (run the command that matches your shell):
	```bash
	source .venv/bin/activate
	```
	```powershell
	.venv\Scripts\Activate.ps1
	```

## 3. Install Dependencies (Editable Mode)
```bash
uv pip install -e .
```

If a single package is missing later, you can patch it quickly:
```bash
uv add <package-name>
```

## 4. Configure Environment Variables
```bash
cp .env.example .env  # create one if you do not have it yet
```
Edit `.env` and set:
```
OPENAI_API_KEY="your_sk-live-or-team-key"
```

Run the notebooks top to bottom. Use your OpenAI key and start experimenting with the hero models.

Need more detail? Dive into [`setup_instructions.md`](setup_instructions.md) for Git basics, dependency management tips, and optional tools.
