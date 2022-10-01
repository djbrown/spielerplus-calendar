from pathlib import Path

from spielerplus_calendar import appointment, config, crawler, parsing, rendering


def create_ics(server: str, identity: str, team_name) -> str:
    html = crawler.fetch_event_calendar(server, identity)
    items = parsing.parse_event_calendar(html)
    filtered = appointment.filter_items(items)
    appointments = [appointment.to_appointment(item) for item in filtered]
    calendar = rendering.to_icalendar(appointments, team_name)
    return calendar.to_ical()


def main():
    conf = config.from_file()
    identity = Path("identity.txt").read_text("utf-8").strip()
    ics = create_ics(conf.server, identity, conf.team_name)
    print(ics)


if __name__ == "__main__":
    main()
