from spielerplus_calendar import appointment, config, crawler, parsing, rendering


def create_ics(conf: config.Config) -> str:
    html = crawler.fetch_event_calendar(identity=conf.identity)
    items = parsing.parse_event_calendar(html)
    filtered = appointment.filter_items(items)
    appointments = [appointment.to_appointment(item) for item in filtered]
    calendar = rendering.to_icalendar(appointments, conf.team_name)
    return calendar.to_ical()


def main():
    conf = config.from_file()
    ics = create_ics(conf)
    print(ics)


if __name__ == "__main__":
    main()
