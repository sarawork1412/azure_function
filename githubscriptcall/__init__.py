import requests
import subprocess

# URL of the raw script on GitHub
github_script_url = "https://raw.githubusercontent.com/yourusername/yourrepo/branch/script.py"

# Fetch the script content
response = requests.get(github_script_url)
script_content = response.text

# Execute the script
result = subprocess.run(["python", "-c", script_content], capture_output=True, text=True)

# Get the output and any errors
output = result.stdout
error = result.stderr

# Do something with the output and error, such as logging or returning it from the Azure Function.
