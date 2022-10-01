import urllib

import requests


def fetch_event_list(server: str, identity: str, offset=0):
    url = f"{server}/events/ajaxgetevents"
    iterative = requests.post(
        url,
        cookies={"_identity": urllib.parse.quote(identity)},
        data={"offset": offset},
        timeout=5,
    ).json()
    return iterative["count"]


def fetch_event_calendar(server, identity: str, date: str = "2022-09-01") -> str:
    url = f"{server}/events/calendar?date={date}"
    cookies = dict(_identity=urllib.parse.quote(identity))
    return requests.post(
        url,
        cookies=cookies,
        timeout=5,
    ).text
