import json
from datetime import datetime
from pathlib import Path

from spielerplus_calendar import parsing


def test_parse_event_calendar():
    html = Path("tests/data/event-calendar.html").read_text()
    target = json.loads(Path("tests/data/event-calendar-items.json").read_text())

    actual = parsing.parse_event_calendar(html)

    assert actual == target


def test_parse_datetime():
    timestamp = "2022-12-14T17:25:00Z"
    target = datetime(2022, 12, 14, 17, 25)

    actual = parsing.parse_timestamp(timestamp)

    assert actual == target
