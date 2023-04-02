from flask import Flask, Response

from spielerplus_calendar import config, main

app = Flask(__name__)


@app.route("/team/<int:team_id>/")
def team_calendar_view(team_id: int = 0):
    conf = config.from_file()
    team = conf.teams[team_id]
    ics = main.team_calendar(conf.server, team.identity, team.name)
    headers = {"content-disposition": 'attachment; filename="team.ics"'}
    return Response(ics, mimetype="text/calendar", headers=headers)


@app.route("/personal/<int:team_id>/")
def personal_calendar_view(team_id: int = 0):
    conf = config.from_file()
    team = conf.teams[team_id]
    ics = main.personal_calendar(conf.server, team.identity, team.name)
    headers = {"content-disposition": 'attachment; filename="personal.ics"'}
    return Response(ics, mimetype="text/calendar", headers=headers)
