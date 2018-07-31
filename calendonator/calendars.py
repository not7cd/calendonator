"""Logic"""
import yaml
import ics
import requests
from glom import glom

def get_event_sources():
	with open("sources.yml") as f:
		sources = list(yaml.load_all(f))

	return sources

def get_aggregated_ical(sources):
	aggregated_calendar = ics.Calendar()
	for ics_url in glom(sources, ["ics_url"]):
		minor_calendar = ics.Calendar(requests.get(ics_url).text)
		for event in minor_calendar.events:
			aggregated_calendar.events.add(event)

	return aggregated_calendar
