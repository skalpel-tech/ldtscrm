# LDTS Crm Python Flask Api

LDTS Crm is using python 3.7 see requirements.txt for information about dependencies.

## Pre-requisite

For development:
* install [virutalenv](https://pypi.org/project/virtualenv/)
* install [virtualenvwrapper](https://pypi.org/project/virtualenvwrapper/)
Windows:
* install [virtualenvwrapper-win](https://pypi.org/project/virtualenvwrapper-win/)

For mac osx user:
get the path for virtualenvwrapper.sh
```
which virtualenvwrapper.sh
```
set .bash_profile
```
$ cat >> ~/.bash_profile
export WORKON_HOME=$HOME/.virtualenvs
source /usr/local/bin/
^D
```

## Instalation

1. Create a virtual environment  
```
cd /rootDirectory
$ mkvirtualenv lstdcrm
```

2. Activate the environment  
```
$ activate
```

3. Install Application dependencies  
```
$ pip install -r requirements.txt
```

4. Run the application
```
$ invoke app.run
```

5. Browse to http://localhost:8888/api

## Configuration

Configuration can be changed in app/config/settings.py

## Pylint

Execute the following cmd to lint the code:
```
$ pylint --disable=fixme src
```

Configuration is in the root folder.
