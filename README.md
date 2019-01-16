# LDTS CRM API

[![Build Status](https://travis-ci.org/skalpel-tech/ldtscrm.svg?branch=master)](https://travis-ci.org/skalpel-tech/ldtscrm)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/cd69f740d0d144a79d2cccb023096261)](https://app.codacy.com/app/cedar-technologies/ldtscrm?utm_source=github.com&utm_medium=referral&utm_content=skalpel-tech/ldtscrm&utm_campaign=Badge_Grade_Settings)
[<img src="https://img.shields.io/badge/slack-ldtscrmapi-%2370ccdc.svg?logo=slack">](https://skalpel.slack.com/messages/CF75MFVB4/)

### https://skalpel-tech.github.io/ldtscrm/

LTDS CRM API is a distributed, RESTful Open Source CRM System API driven. LDTS CRM allows you to collect, analyze and gain insight into the most important information about your customers with modern, powerful and incredibly robust software.
Our team members and contributors adhere to strict Agile and Devops Engineering methodologies which ensure code quality and efficiency.

Features include:

* Various Set of Restful APIs.
  * Contact Management modules.

## Installation

LDTS Crm is using python 3.5 see requirements.txt for information about dependencies.

### Pre-requisite

For development:
* install [python 3.5](https://www.python.org/downloads/release/python-356/)
* install [virutalenv](https://pypi.org/project/virtualenv/)
* install [virtualenvwrapper](https://pypi.org/project/virtualenvwrapper/)
Windows:
* install [virtualenvwrapper-win](https://pypi.org/project/virtualenvwrapper-win/)
* create a database, currently tested with [postgres 11](https://www.postgresql.org/download/) and `mysql`

For osx user:
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

### Instructions

Create a virtual environment  

```bash
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

Create a local configuration `local_config.py`, you can copy the `local_config.py.template` and set up your database connection

Upgrad the database to current version

```bash
invoke app.db.upgrade
```

Run the application

```bash
invoke app.run
```

Browse to `http://localhost:8888/api`

## Configuration

Configuration can be changed in `config.py`

## Project Structure

### Root folder

Folders:

* `app` - This RESTful API Server example implementation is here.
* `tasks` - [PyInvoke](http://www.pyinvoke.org/) commands are implemented here.
* `tests` - It contains pytest suite for LDTS CRM API.
* `docs` - It contains just images for the README, so you can safely ignore it.

Files:

* `README.md`
* `.coveragerc`- Code coverage requirements.
* `.gitignore` - Lists files and file masks of the files which should not be
  added to git repository.
* `.pylintrc` - Pylint configuration execute `pylint --disable=fixme app`.
* `.remarkrc` - Linter configuration for markdown documents.
* `.travis.yml` - [Travis CI](https://travis-ci.org/) (automated continuous
  integration) config for automated testing.
* `bandit.yml` - bandit configuration for codacy code review
* `CODE_OF_CONDUCT.md` - LDTS CRM API Development Code of Conduct.
* `CONTRIBUTING.md` - LDTS CRM API contributing guidelines.
* `config.py` - Configuration file of the LDTS CRM Restful api.
* `LICENSE` - Apache License, i.e. you are free to do whatever is needed with the
  given code with no limits.
* `local_config.py.template` - Example of local configuration, create a local_config.py to set your application
* `requirements.txt` - LDTS CRM API Python requirements.

### Where to start reading the code

The easiest way to start the application is by using PyInvoke command `app.run`
implemented in [`tasks/app/run.py`](tasks/app/run.py):

```bash
invoke app.run
```

## Configuration

look at `config.py`

## Unit Test

Install the dependencies

```bash
pip install -r test/requirements.txt
```
