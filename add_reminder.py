from datetime import datetime, timedelta, time
import caldav

# Variables
with open("pw.txt", "r") as f:
    url = f.read()

today = datetime.combine(datetime.today(), time(0, 0))

# Main
client = caldav.DAVClient(url)
principal = client.principal()
calendars = principal.calendars()

if len(calendars) > 0:
    calendar = calendars[0]
    events = calendar.date_search(today, datetime.combine(today, time(23, 59, 59, 59)))

    if len(events) == 0:
        print("No events today!")
    else:
        print("Total {num_events} events:".format(num_events=len(events)))

        for event in events:
            event.load()
            e = event.instance.vevent
            if e.dtstart.value.strftime("%H:%M") == "00:00":
                # This is an "allday" event
                eventTime = e.dtstart.value.strftime("%D")
                print("{eventTime} {eventSummary} ({eventLocation})".format(
                    eventTime=eventTime, eventSummary=e.summary.value, eventLocation=1))
            else:
                # This is a "normal" event
                eventTime = e.dtstart.value.strftime("%H:%M")
                print("{eventTime} {eventSummary} ({eventLocation})".format(
                    eventTime=eventTime, eventSummary=e.summary.value, eventLocation=1))
