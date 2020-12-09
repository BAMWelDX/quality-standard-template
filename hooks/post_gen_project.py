import subprocess

subprocess.call(["git", "init"])
subprocess.call(["git", "add", "*"])
subprocess.call(["git", "commit", "-m", "Cookiecutter setup commit"])

subprocess.call(["git", "tag", "0.1.0"])

subprocess.call(["python", "setup.py", "--version"])
