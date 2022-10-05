from flask import Flask, Response

from spielerplus_calendar import config, main

app = Flask(__name__)


@app.route("/team/")
def team_calendar_view():
    conf = config.from_file()
    ics = main.team_calendar(conf.server, conf.identity, conf.team_name)
    headers = {"content-disposition": 'attachment; filename="team.ics"'}
    return Response(ics, mimetype="text/calendar", headers=headers)
