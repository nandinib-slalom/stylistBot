# StylistBot

A simple stylist agent that suggests an outfit (top, bottom, shoes, jacket) based on the weather.

## Features
- Hardcoded weather for demonstration (can be extended to use a real API)
- Outfit suggestions for different weather types

## Usage

## Prerequisites

You need Python 3.7 or higher installed on your system. If you do not have Python installed:

- **macOS**: Python 3 may already be installed. To check, run `python3 --version` in your terminal. If not installed, download it from [python.org/downloads](https://www.python.org/downloads/) or install via Homebrew:
	```bash
	brew install python
	```
- **Windows**: Download and install Python from [python.org/downloads](https://www.python.org/downloads/). Make sure to check the box to add Python to your PATH during installation.
- **Linux**: Use your package manager, e.g.:
	```bash
	sudo apt-get update
	sudo apt-get install python3 python3-venv python3-pip
	```



1. Clone the repository or copy the files into your project directory.
2. (Optional) Create and activate a virtual environment:
	```bash
	python3 -m venv venv
	source venv/bin/activate
	```
3. Install dependencies:
	```bash
	pip install -r requirements.txt
	```
4. Run the main script:
	```bash
	python main.py
	```

## File Structure
- `main.py`: Entry point for the application.
- `weather.py`: Contains weather-related logic (currently hardcoded).
- `stylist.py`: Contains the outfit suggestion logic.

## Customization
- To change the weather, modify the return value in `weather.py`.
- To add more outfit options, update the logic in `stylist.py`.

## License
MIT

## Deploying to GitHub

To move your code to GitHub:

1. Create a new repository on [GitHub](https://github.com/new).
2. Initialize a local git repository (if you haven't already):
	```bash
	git init
	```
3. Add all files and commit:
	```bash
	git add .
	git commit -m "Initial commit"
	```
4. Add the remote repository (replace `<your-username>` and `<repo-name>`):
	```bash
	git remote add origin https://github.com/<your-username>/<repo-name>.git
	```
5. Push your code to GitHub:
	```bash
	git branch -M main
	git push -u origin main
	```
