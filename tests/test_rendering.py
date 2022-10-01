from datetime import datetime
from pathlib import Path

from spielerplus_calendar import appointment, rendering


def test_to_calendar():
    appointments = [
        appointment.Appointment(
            id=65426556,
            title="Training",
            start=datetime(2022, 9, 30, 18, 55, 00),
            end=datetime(2022, 9, 30, 20, 30, 00),
            url="/training/view?id=65426556",
            color="#44AD34",
        ),
        appointment.Appointment(
            id=5603407,
            title="Gegner A",
            start=datetime(2022, 7, 11, 18, 10, 00),
            end=datetime(2022, 7, 11, 20, 00, 00),
            url="/game/view?id=5603407",
            color="#34692D",
        ),
        appointment.Appointment(
            id=1049518,
            title="Training + Spiel",
            start=datetime(2022, 4, 24, 11, 55, 00),
            end=datetime(2022, 4, 24, 15, 30, 00),
            url="/event/view?id=1049518",
            color="#34692D",
        ),
        appointment.Appointment(
            id=710393,
            title="Turnier",
            start=datetime(2022, 7, 9, 12, 45, 00),
            end=datetime(2022, 7, 9, 23, 59, 59),
            url="/tournament/view?id=710393",
            color="#34692D",
        ),
    ]

    timestamp = datetime(2022, 9, 29, 4, 7, 57)
    cal = rendering.to_icalendar(appointments, "HSG Blau-Weiß 22/23", timestamp)
    actual = cal.to_ical().decode().replace("\r\n", "\n")

    target = Path("tests/data/event-calendar.ics").read_text(encoding="utf-8")

    assert actual == target


def test_to_calendar_event():
    appointment = appointment.Appointment(
        id=12345,
        title="Training",
        start=datetime(2022, 9, 16, 18, 40),
        end=datetime(2022, 9, 16, 20, 30),
        url="/training/view?id=12345",
        color="#44AD34",
    )
    timestamp = datetime.now()

    target = (
        "BEGIN:VEVENT\r\n"
        "SUMMARY:Training\r\n"
        "DTSTART;VALUE=DATE-TIME:20220916T184000\r\n"
        "DTEND;VALUE=DATE-TIME:20220916T203000\r\n"
        "DTSTAMP;VALUE=DATE-TIME:" + timestamp.strftime("%Y%m%dT%H%M%S") + "Z\r\n"
        "UID:event/12345@spielerplus.de\r\n"
        "END:VEVENT\r\n"
    )

    actual = rendering.to_icalendar_event(appointment, timestamp).to_ical().decode()

    assert actual == target
