# Linux Environment
Linux tools and environment setup

## SSH Keys
Create new SSH keys to allow access to Git and other sites by copying the contents of the public key (~/.ssh/id_rsa.pub) to sites
* Create SSH keys: ```ssh-keygen```

## Python
Assuming that Python3 is already installed:
* Install Python virtual environment: ```apt install python3.10-venv```
* Create a virtual environment: ```python3 -m venv ~/venv```
* Start the virtual environment: ```source ~/venv/bin/activate```

## Visual Studio Code
Install Visual Studio Code then add the following extensions to Code
* GitLens
* Python
* VSCode-Icons
* Intellicode
* Auto Close Tag
* Code Spell Checker
