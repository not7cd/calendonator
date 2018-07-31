from flask import render_template

from calendonator import app
from calendonator.calendars import *


@app.route('/')
def index():
    app.logger.warning('sample message')
    return render_template('index.html')

@app.route('/upcoming.ical')
def aggregated_calendar():
	event_sources = get_event_sources()
	ical = get_aggregated_ical(event_sources)
	return str(ical)

