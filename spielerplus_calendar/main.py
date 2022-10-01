from spielerplus_calendar import appointment, crawler, parsing, rendering

identity = "identity-string"
team_name = "HSG Blau-Weiß 22/23"


if __name__ == "__main__":
    html = crawler.fetch_event_calendar(identity=identity)
    items = parsing.parse_event_calendar(html)
    filtered = appointment.filter_items(items)
    appointments = [appointment.to_appointment(item) for item in filtered]
    calendar = rendering.to_icalendar(appointments, team_name)
    print(calendar.to_ical())
