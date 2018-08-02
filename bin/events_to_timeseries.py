import csv
import ics
import requests
import arrow

calendar = ics.Calendar(
    requests.get(
        u"https://calendar.google.com/calendar/ical/8s96dmhr9qv1akadn3b2el9kk8%40group.calendar.google.com/public/basic.ics"
    ).text
)

timeline = ics.timeline.Timeline(calendar)

series = []

strr = arrow.utcnow()
strr = strr.replace(year=2015)

for day in arrow.Arrow.range("day", strr, arrow.now()):
	row = {"date": day, "events": len(list(timeline.on(day)))}
	print(row)
	if row["events"] != 0:
		series.append(row)

with open("events.csv", "w") as f:
    writer = csv.DictWriter(f, fieldnames=list(series[0].keys()))
    writer.writeheader()
    for row in series:
        writer.writerow(row)
