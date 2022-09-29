import requests
import urllib


def fetch_event_list(identity: str, offset=0):
    url = "https://www.spielerplus.de/events/ajaxgetevents"
    iterative = requests.post(
        url,
        cookies={"_identity": urllib.parse.quote(identity)},
        data={"offset": offset},
    ).json()
    return iterative["count"]


def fetch_event_calendar(identity: str, date: str = "2022-09-01") -> str:
    url = f"https://www.spielerplus.de/events/calendar?date={date}"
    cookies = dict(_identity=urllib.parse.quote(identity))
    return requests.post(url, cookies=cookies).text
