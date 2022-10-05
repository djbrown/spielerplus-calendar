from spielerplus_calendar import appointment, config, crawler, parsing, rendering


def team_calendar(server: str, identity: str, team_name) -> str:
    html = crawler.fetch_event_calendar(server, identity)
    items = parsing.parse_event_calendar(html)
    filtered = appointment.filter_items(items)
    appointments = [appointment.from_calendar_item(item) for item in filtered]
    calendar = rendering.to_icalendar(appointments, team_name)
    return calendar.to_ical().decode("utf-8")


def main():
    conf = config.from_file()
    ics = team_calendar(conf.server, conf.identity, conf.team_name)
    print(ics)


if __name__ == "__main__":
    main()
