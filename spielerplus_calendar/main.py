from spielerplus_calendar import appointment, config, crawler, parsing, rendering


if __name__ == "__main__":
    c = config.read_config()
    html = crawler.fetch_event_calendar(identity=c.identity)
    items = parsing.parse_event_calendar(html)
    filtered = appointment.filter_items(items)
    appointments = [appointment.to_appointment(item) for item in filtered]
    calendar = rendering.to_icalendar(appointments, c.team_name)
    print(calendar.to_ical())
