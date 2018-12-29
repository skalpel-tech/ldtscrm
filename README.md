# LDTS CRM API

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/83f9da84377f42339dd96b0424af1271)](https://app.codacy.com/app/cedar-technologies/skpcrm?utm_source=github.com&utm_medium=referral&utm_content=skalpel-tech/skpcrm&utm_campaign=Badge_Grade_Dashboard)
[![Build Status](https://travis-ci.org/skalpel-tech/skpcrm.svg?branch=master)](https://travis-ci.org/skalpel-tech/skpcrm)

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

```
$ invoke app.run
```