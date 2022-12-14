from spielerplus_calendar import appointment, config, crawler, parsing, rendering


def team_calendar(server: str, identity: str, team_name) -> str:
    html = crawler.fetch_event_calendar(server, identity)
    items = parsing.parse_event_calendar(html)
    filtered = appointment.filter_items(items)
    appointments = [appointment.from_calendar_item(item) for item in filtered]
    calendar = rendering.to_icalendar(appointments, team_name)
    return calendar.to_ical().decode("utf-8")


def personal_calendar(server: str, identity: str, team_name) -> str:
    event_list_html = crawler.fetch_event_list(server, identity)
    items = parsing.parse_event_list_items(event_list_html)
    appointments = [appointment.from_event_list_item(item) for item in items]

    event_htmls = [
        crawler.fetch_event(server, identity, app.url) for app in appointments
    ]
    years = [parsing.parse_event_year(event_html) for event_html in event_htmls]
    appointments = [
        appointment.updated_year(app, year) for app, year in zip(appointments, years)
    ]

    calendar = rendering.to_icalendar(appointments, team_name)
    return calendar.to_ical().decode("utf-8")


def main():
    conf = config.from_file()
    # ics = team_calendar(conf.server, conf.identity, conf.team_name)
    ics = personal_calendar(conf.server, conf.identity, conf.team_name)
    print(ics)


if __name__ == "__main__":
    main()
