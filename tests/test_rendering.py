from datetime import datetime
from pathlib import Path

import pytz

from spielerplus_calendar import rendering

from tests import fixtures

tz = pytz.timezone("Europe/Berlin")


def test_to_calendar():
    appointments = fixtures.appointments()

    timestamp = datetime(2022, 9, 29, 4, 7, 57)
    cal = rendering.to_icalendar(
        appointments, "HSG Blau-Weiß 22/23", "http://myserver.tld", timestamp
    )
    actual = cal.to_ical().decode().replace("\r\n", "\n")

    target = Path("tests/data/event-calendar.ics").read_text("utf-8")

    assert actual == target


def test_to_calendar_event():
    app = fixtures.practice()
    timestamp = datetime(2023, 7, 7, 18, 9, 42)

    target = (
        "BEGIN:VEVENT\r\n"
        "SUMMARY:Training\r\n"
        "DTSTART;TZID=Europe/Berlin;VALUE=DATE-TIME:20220916T184000\r\n"
        "DTEND;TZID=Europe/Berlin;VALUE=DATE-TIME:20220916T203000\r\n"
        "DTSTAMP;VALUE=DATE-TIME:20230707T160942Z\r\n"
        "UID:12345\r\n"
        "DESCRIPTION:this is my description\\n\\nhttp://myserver.tld/training/view?id\r\n"
        " =12345\r\n"
        "END:VEVENT\r\n"
    )

    actual = (
        rendering.to_icalendar_event(app, "http://myserver.tld", timestamp)
        .to_ical()
        .decode()
    )

    assert actual == target
