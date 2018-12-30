# LDTS CRM API

[![Build Status](https://travis-ci.org/skalpel-tech/ldtscrm.svg?branch=master)](https://travis-ci.org/skalpel-tech/ldtscrm)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/cd69f740d0d144a79d2cccb023096261)](https://app.codacy.com/app/cedar-technologies/ldtscrm?utm_source=github.com&utm_medium=referral&utm_content=skalpel-tech/ldtscrm&utm_campaign=Badge_Grade_Settings)

Open Source CRM System  
Agile, Devops, Python, Elasticsearch, Logstash, Kibana, Cassandra

## Installation

[see Installation](/src/app/README.md)

## Project Structure

### Root folder

Folders:

* `app` - This RESTful API Server example implementation is here.
* `tasks` - [PyInvoke](http://www.pyinvoke.org/) commands are implemented here.
* `docs` - It contains just images for the README, so you can safely ignore it.

Files:

* `README.md`
* `.pylintrc` - Pylint configuration execute `pylint --disable=fixme src`
* `.travis.yml` - [Travis CI](https://travis-ci.org/) (automated continuous
  integration) config for automated testing.
* `.gitignore` - Lists files and file masks of the files which should not be
  added to git repository.
* `LICENSE` - Apache License, i.e. you are free to do whatever is needed with the
  given code with no limits.

### Where to start reading the code

The easiest way to start the application is by using PyInvoke command `app.run`
implemented in [`tasks/app/run.py`](tasks/app/run.py):

```bash
invoke app.run
```
