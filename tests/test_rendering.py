from datetime import datetime
from pathlib import Path

from spielerplus_calendar import rendering

from tests import fixtures


def test_to_calendar():
    appointments = fixtures.appointments()

    timestamp = datetime(2022, 9, 29, 4, 7, 57)
    cal = rendering.to_icalendar(appointments, "HSG Blau-Weiß 22/23", timestamp)
    actual = cal.to_ical().decode().replace("\r\n", "\n")

    target = Path("tests/data/event-calendar.ics").read_text("utf-8")

    assert actual == target


def test_to_calendar_event():
    app = fixtures.practice()
    timestamp = datetime.now()

    target = (
        "BEGIN:VEVENT\r\n"
        "SUMMARY:Training\r\n"
        "DTSTART;VALUE=DATE-TIME:20220916T184000\r\n"
        "DTEND;VALUE=DATE-TIME:20220916T203000\r\n"
        "DTSTAMP;VALUE=DATE-TIME:" + timestamp.strftime("%Y%m%dT%H%M%S") + "Z\r\n"
        "UID:12345\r\n"
        "END:VEVENT\r\n"
    )

    actual = rendering.to_icalendar_event(app, timestamp).to_ical().decode()

    assert actual == target
