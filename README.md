# spielerplus-calendar

Get your [Spielerplus](https://www.spielerplus.de/) events in [ICS](https://en.wikipedia.org/wiki/ICalendar) format for calendar subscription.

[![CI Build](https://github.com/djbrown/spielerplus-calendar/actions/workflows/ci-build.yml/badge.svg)](https://github.com/djbrown/spielerplus-calendar/actions/workflows/ci-build.yml)
[![Docker](https://github.com/djbrown/spielerplus-calendar/actions/workflows/docker.yml/badge.svg)](https://github.com/djbrown/spielerplus-calendar/actions/workflows/docker.yml)
[![Docker Image)](https://img.shields.io/docker/v/djbrown/spielerplus-calendar?label=Docker%20Image)](https://hub.docker.com/r/djbrown/spielerplus-calendar)


## Setup

* vscode
* pyenv
* python 3.10
* poetry
* docker

## Tools

* black
* pytest
* pylint
* mypy

## Configuration

The application has to be configured with a `config.json` file.
For an example see [tests/data/config.json](https://github.com/djbrown/spielerplus-calendar/blob/main/tests/data/config.json)


* `server`: base URL of the Spielerplus server e.g. `https://www.spielerplus.de`.
* `team[].identity`: your personal `_identity` cookie on the Spielerplus server for the respective team. You can access the cookie value from the the browser settings or DevTools (e.g. [Firefox](https://firefox-source-docs.mozilla.org/devtools-user/storage_inspector/index.html) or [Chrome](https://developer.chrome.com/docs/devtools/application/cookies/)). ⚠️ Copying from Browser DevTools or pasting into an IDE might mix up the encoding. The value has to be encodet just at the inline double quotes to be a valid json string value. For an example see [tests/data/config.json](https://github.com/djbrown/spielerplus-calendar/blob/main/tests/data/config.json).
* `team[].name`: can be chosen freely, as it is only used for naming the calendar.

## Development Flask Server

Start a development server:<br/>
`poetry run flask --app spielerplus_calendar/server.py --debug run`

The server is reachable under `http://localhost:5000` (flask default).

Endpoints ([spielerplus-calendar/server.py](https://github.com/djbrown/spielerplus-calendar/blob/main/spielerplus-calendar/server.py)):
* `/team/<team_id>` serves all Events of the team
* `/personal/<team_id>` serves only Events attend

## CLI

Generates ICS output for custom postprocessing:<br/>
`poetry run python spielerplus_calendar/main.py`

## Production Docker Image

Starts a production ready server in a docker container:<br/>
`docker run -p 5000:5000 -v $(pwd)/config.json:/app/config.json:ro djbrown/spielerplus-calendar`
The server will be reachable under port `5000` on all public ip addresses of your machine.
You may optionally change the default server timeout (300s) e.g: `-e SERVER_TIMEOUT=600`.
