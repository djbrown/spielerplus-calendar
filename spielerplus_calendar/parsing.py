import json
import re
from datetime import datetime


def parse_event_calendar(html: str) -> list:
    pattern = (
        r'^        },"locale":"de","firstDay":1,"events":(\[.*\]),'
        r'"allDayDefault":true,"eventRender":    \(function\(event, element\) {$'
    )
    result: re.Match[str] | None = re.search(pattern, html, re.MULTILINE)
    if result is None:
        raise Exception("Could not parse calendar html")
    data = result.group(1)
    return json.loads(data)


def parse_timestamp(timestamp: str) -> datetime:
    return datetime.fromisoformat(timestamp[:-1])  # stip trailing Z
