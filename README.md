# spielerplus-calendar

Get ics calendar data for spielerplus team.

## Setup

* vscode
* pyenv
* python 3.10
* poetry

## Tools

* black
* pytest
* pylint
* mypy

## Server

`poetry run flask --app spielerplus_calendar/server.py --debug run`

## CLI

`poetry run python spielerplus_calendar/main.py`

## production

`poetry install --with prod`

