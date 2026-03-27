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

### GitHub Authentication: Passwords vs Tokens

GitHub no longer supports password authentication for Git operations. You must use a **personal access token (PAT)** instead of your GitHub password when pushing code from the command line.

When prompted for a password after `git push`, paste your personal access token (PAT) instead.

#### How to Create a Personal Access Token

1. Go to [GitHub Settings > Developer settings > Personal access tokens](https://github.com/settings/tokens).
2. Click **Generate new token**.
3. For most users, select **classic** token for simplicity. If you want more control, use a **fine-grained** token and set the following permissions:
   - **Repository permissions**: Contents (Read and write)
   - **Actions**: Read and write (for GitHub Actions workflows)
   - **Packages**: Read and write (for GitHub Packages, e.g., container images)
4. Choose the repositories you want the token to access ("All repositories" or "Only select repositories").
5. Copy and save the token securely. You will not be able to see it again.

#### Recommended Permissions for CI/CD and Automation

- For classic tokens: Enable **repo** and **workflow** permissions.
- For fine-grained tokens: Enable **Contents: Read and write**, **Actions: Read and write**, and **Packages: Read and write** if needed.

#### Security Tips

- Never share your token or commit it to your repository.
- Use the minimal permissions necessary for your needs.
- You can revoke or regenerate tokens at any time from your GitHub settings.

#### More Info

See the [GitHub documentation on personal access tokens](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token) for details.
