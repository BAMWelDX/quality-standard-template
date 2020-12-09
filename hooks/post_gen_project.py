import subprocess

{% if cookiecutter.git_setup == "yes" %}
subprocess.call(["git", "init"])
subprocess.call(["git", "add", "*"])
subprocess.call(["git", "commit", "-m", "Cookiecutter setup commit"])

subprocess.call(["git", "tag", "1.0.0"])

subprocess.call(["python", "setup.py", "--version"])
{% endif %}