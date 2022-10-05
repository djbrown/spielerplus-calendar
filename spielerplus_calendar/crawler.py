import urllib

import requests


def fetch_event_list(server: str, identity: str, offset=0, old=False) -> str:
    url = f"{server}/events/ajaxgetevents"
    response = requests.post(
        url,
        cookies={"_identity": urllib.parse.quote(identity)},
        data={"offset": offset, "old": str(old)},
        timeout=5,
    )
    return response.json()["html"]


def fetch_event_calendar(server, identity: str, date: str = "2022-09-01") -> str:
    url = f"{server}/events/calendar?date={date}"
    cookies = dict(_identity=urllib.parse.quote(identity))
    response = requests.post(
        url,
        cookies=cookies,
        timeout=5,
    )
    return response.text
