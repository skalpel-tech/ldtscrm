# LDTS Crm Python Flask Api

LDTS Crm is using python 3.5 see requirements.txt for information about dependencies.

## Pre-requisite

For development:
* install [python 3.5](https://www.python.org/downloads/release/python-356/)
* install [virutalenv](https://pypi.org/project/virtualenv/)
* install [virtualenvwrapper](https://pypi.org/project/virtualenvwrapper/)
Windows:
* install [virtualenvwrapper-win](https://pypi.org/project/virtualenvwrapper-win/)

For mac osx user:
get the path for virtualenvwrapper.sh

```bash
which virtualenvwrapper.sh
```

set .bash_profile

```bash
$ cat >> ~/.bash_profile
export WORKON_HOME=$HOME/.virtualenvs
export PROJECT_HOME=$HOME/Devel
source [result of `which virtualenvwrapper.sh`]
^D
```

## Instalation

Create a virtual environment  

```cmd
cd /rootDirectory
mkvirtualenv lstdcrm
```

Activate the environment for windows only

```bash
activate
```

Install Application dependencies  

```bash
pip install -r requirements.txt
```

Run the application

```bash
invoke app.run
```

Browse to http://localhost:8888/api

## Configuration

Configuration can be changed in app/config/settings.py

## Pylint

Install Pylint globally (make sure you are not working on your virtualenv)

```bash
pip install pylint
```

Execute the following cmd to lint the code:

```bash
pylint --disable=fixme src
```

Configuration is in the root folder.