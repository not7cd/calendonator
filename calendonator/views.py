from flask import render_template

from calendonator import app
from calendonator.calendars import *


def get_calendar():
	event_sources = get_event_sources()
	return get_aggregated_ical(event_sources)

@app.route('/')
def index():
    app.logger.warning('sample message')
    return render_template('index.html', events=get_calendar().events)

@app.route('/upcoming.ical')
def aggregated_calendar():
	return str(get_calendar())

