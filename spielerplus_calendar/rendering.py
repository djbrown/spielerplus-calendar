from datetime import datetime

from icalendar import Calendar, Event

from spielerplus_calendar.appointment import Appointment


def to_icalendar(
    appointments: list[Appointment], team_name, server, timestamp: datetime = None
) -> Calendar:
    calendar = Calendar()
    calendar.add("PRODID", "-//SpielerPlus//Terminkalender 1.0//DE")
    calendar.add("VERSION", "2.0")
    calendar.add("CALSCALE", "GREGORIAN")
    calendar.add("METHOD", "PUBLISH")
    calendar.add("X-WR-CALNAME", f"SpielerPlus {team_name}")
    calendar.add("X-WR-TIMEZONE", "Europe/Berlin")
    calendar.add("X-WR-CALDESC", f'SpielerPlus Termine "{team_name}"')
    for appointment in appointments:
        event = to_icalendar_event(appointment, server, timestamp)
        calendar.add_component(event)
    return calendar


def to_icalendar_event(
    appointment: Appointment, server: str, timestamp: datetime = None
) -> Event:
    event = Event()
    event.add("summary", appointment.title)
    event.add("dtstart", appointment.start)
    event.add("dtend", appointment.end)
    event.add("dtstamp", datetime.now() if timestamp is None else timestamp)

    description = server + appointment.url
    if appointment.description:
        description += f"\n{appointment.description}"
    event.add("description", description)

    if appointment.address:
        event.add("location", appointment.address)

    event["uid"] = f"{appointment.id}"

    return event
