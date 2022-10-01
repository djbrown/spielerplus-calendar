import json
import re
from datetime import datetime


def parse_event_calendar(html: str) -> list:
    pattern = (
        r'^        },"locale":"de","firstDay":1,"events":(\[.*\]),'
        r'"allDayDefault":true,"eventRender":    \(function\(event, element\) {$'
    )
    data = re.search(pattern, html, re.MULTILINE).group(1)
    return json.loads(data)


def parse_timestamp(timestamp: str) -> datetime:
    return datetime.fromisoformat(timestamp[:-1])  # stip trailing Z


def parse_event_list(html: str):
    pass
