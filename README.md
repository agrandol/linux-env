# Linux Environment
Linux tools and environment setup

## SSH Keys
Create new SSH keys to allow access to Git and other sites by copying the contents of the public key (~/.ssh/id_rsa.pub) to sites
* Create SSH keys: ```ssh-keygen```

## Python
Assuming Python3 is already installed:
* Install Python virtual environment: ```apt install python3.10-venv```
* Create a virtual environment: ```python3 -m venv ~/venv```
* Start the virtual environment: ```source ~/venv/bin/activate```
* Install pyinstaller: ```pip install -U pyinstaller```

## Node.js and NPM
Download and install Node.js and NPM as follows:
* Download the latest LTS version from https://nodejs.org/en/  (node-v18.14.2-linux-x64.tar.xz)
* Unzip and install in /usr/local
```
   cd /usr/local
   sudo tar --strip-components 1 -xvf /home/<user>/Downloads/node-v18.14.2-linux-x64.tar.xz
```
* Verify installs
```
   node --version
   npm --version
```

## Visual Studio Code
Install Visual Studio Code then add the following extensions to Code
* GitLens
* Python
* VSCode-Icons
* Intellicode
* Auto Close Tag
* Code Spell Checker
