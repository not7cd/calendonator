from flask import render_template, json

from calendonator import app
from calendonator.calendars import *
import arrow
from glom import glom


def get_calendar():
    event_sources = get_event_sources()
    return get_aggregated_ical(event_sources)


@app.route("/")
def index():
    app.logger.warning("sample message")
    timeline = ics.timeline.Timeline(get_calendar())
    now = arrow.now()
    return render_template("index.html", events=timeline.start_after(now))


@app.route("/upcoming.ical")
def aggregated_calendar():
    return str(get_calendar())

def events_list(events):
    for event in events:
        yield glom(event, {
            "name": "name",
            "begin": ("begin", lambda b: b.format('YYYY-MM-DD HH:mm:ss'))
            })

@app.route("/api/now")
def now():
    timeline = ics.timeline.Timeline(get_calendar())
    return json.dumps(list(events_list(timeline.now())))

@app.route("/api/upcoming")
def upcoming():
    timeline = ics.timeline.Timeline(get_calendar())
    now = arrow.now()
    return json.dumps(list(events_list(timeline.start_after(now))))

