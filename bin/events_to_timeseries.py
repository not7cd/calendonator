import csv
import ics
import requests
import arrow

OLD_CAL = u"https://calendar.google.com/calendar/ical/8s96dmhr9qv1akadn3b2el9kk8%40group.calendar.google.com/public/basic.ics"
CURRENT_CAL = u"https://calendar.google.com/calendar/ical/codeme.pl_ksn59c5sr9fn3bd78lh7vj07pg%40group.calendar.google.com/public/basic.ics"

calendar = ics.Calendar(
    requests.get(
        CURRENT_CAL
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
