import urllib

import requests


def fetch_event_list(server: str, identity: str) -> str:
    html = _fetch_event_list(server, identity, old=True)
    html += _fetch_todays_event_list(server, identity)
    html += _fetch_event_list(server, identity, old=False)
    return html


def _fetch_todays_event_list(server: str, identity: str) -> str:
    url = f"{server}/events"
    cookies = dict(_identity=urllib.parse.quote(identity))
    response = requests.get(url, cookies=cookies, timeout=5)
    return response.text


def _fetch_event_list(server: str, identity: str, old: bool) -> str:
    all_html = ""
    count = 3 if old else 5
    offset = 0 if old else 5

    while count > 0:
        url = f"{server}/events/ajaxgetevents"
        cookies = dict(_identity=urllib.parse.quote(identity))
        data: dict[str, int | str] = {"offset": offset}
        if old:
            data["old"] = "true"

        response = requests.post(url, cookies=cookies, data=data, timeout=5)

        json = response.json()
        all_html += json["html"]
        count = json["count"]
        offset += count

    return all_html


def fetch_event_calendar(server, identity: str, date: str = "2022-09-01") -> str:
    url = f"{server}/events/calendar?date={date}"
    cookies = dict(_identity=urllib.parse.quote(identity))
    response = requests.post(url, cookies=cookies, timeout=5)
    return response.text


def fetch_event(server, identity: str, path: str) -> str:
    url = f"{server}{path}"
    cookies = dict(_identity=urllib.parse.quote(identity))
    response = requests.post(url, cookies=cookies, timeout=5)
    return response.text
