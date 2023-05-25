# spielerplus-calendar

Get your [Spielerplus](https://www.spielerplus.de/) events in [ICS](https://en.wikipedia.org/wiki/ICalendar) format for calendar subscription.

[![CI Build](https://github.com/djbrown/spielerplus-calendar/actions/workflows/ci-build.yml/badge.svg)](https://github.com/djbrown/spielerplus-calendar/actions/workflows/ci-build.yml)

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

## Configuration

The application has to be configured with a `config.json` file.
For an example see [tests/data/config.json](https://github.com/djbrown/spielerplus-calendar/blob/main/tests/data/config.json)


* `server`: base URL of the Spielerplus server e.g. `https://www.spielerplus.de`.
* `team[].identity`: your personal `_identity` cookie on the Spielerplus server for the respective team. You can access the cookie value from the the browser settings or DevTools (e.g. [Firefox](https://firefox-source-docs.mozilla.org/devtools-user/storage_inspector/index.html) or [Chrome](https://developer.chrome.com/docs/devtools/application/cookies/)).
* `team[].name`: can be chosen freely, as it is only used for naming the calendar.

## Server

Start a (development) server on `http://localhost:5000`:<br/>
`poetry run flask --app spielerplus_calendar/server.py --debug run`<br/>
⚠️ This is not suitable for production!

Endpoints ([spielerplus-calendar/server.py](https://github.com/djbrown/spielerplus-calendar/blob/main/spielerplus-calendar/server.py)):
* `/team/<team_id>` serves all Events of the team
* `/personal/<team_id>` serves only Events attend

## CLI

Generates ICS output for custom postprocessing ().
`poetry run python spielerplus_calendar/main.py`

## production

`poetry install --with prod`

