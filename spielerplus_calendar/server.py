from flask import Flask, Response

from spielerplus_calendar import config, main

app = Flask(__name__)


@app.route("/")
def hello_world():
    conf = config.from_file()
    ics = main.create_ics(conf.server, conf.identity, conf.team_name)
    headers = {"content-disposition": 'attachment; filename="calendar.ics"'}
    return Response(ics, mimetype="text/calendar", headers=headers)
