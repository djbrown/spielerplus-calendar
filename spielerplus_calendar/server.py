from email import header

from flask import Flask, Response, make_response

from spielerplus_calendar import appointment, config, crawler, parsing, rendering

app = Flask(__name__)


@app.route("/")
def hello_world():
    c = config.from_file()
    html = crawler.fetch_event_calendar(identity=c.identity)
    items = parsing.parse_event_calendar(html)
    filtered = appointment.filter_items(items)
    appointments = [appointment.to_appointment(item) for item in filtered]
    calendar = rendering.to_icalendar(appointments, c.team_name)
    headers = {"content-disposition": f'attachment; filename="calendar.ics"'}
    return Response(calendar.to_ical(), mimetype="text/calendar", headers=headers)
