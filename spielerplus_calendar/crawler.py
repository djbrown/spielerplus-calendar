import urllib

import requests


def fetch_event_list(server: str, identity: str) -> str:
    all_html = ""

    offset = 0
    count = 3
    while count > 0:
        (html, count) = _event_list(server, identity, offset=offset, old=True)
        offset += count
        all_html = html + all_html

    offset = 0
    count = 5
    while count > 0:
        (html, count) = _event_list(server, identity, offset=offset, old=False)
        offset += count
        all_html = all_html + html
    return all_html


def _event_list(server: str, identity: str, offset=0, old=False) -> tuple[str, int]:
    url = f"{server}/events/ajaxgetevents"

    data = {"offset": offset}
    if old:
        data["old"] = "true"

    response = requests.post(
        url,
        cookies={"_identity": urllib.parse.quote(identity)},
        data=data,
        timeout=5,
    )
    json = response.json()
    return (json["html"], json["count"])


def fetch_event_calendar(server, identity: str, date: str = "2022-09-01") -> str:
    url = f"{server}/events/calendar?date={date}"
    cookies = dict(_identity=urllib.parse.quote(identity))
    response = requests.post(
        url,
        cookies=cookies,
        timeout=5,
    )
    return response.text
