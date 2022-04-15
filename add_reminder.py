
from datetime import datetime, timedelta, time
import caldav
from ical_helpers import *
import pw


# Main
# client = caldav.DAVClient(url=pw.url, username=username, password=password)
# try:
#     client = caldav.DAVClient(pw.url + pw.calendar_name + "/")
# except caldav.lib.error.AuthorizationError:


if pw.create_new_calendar:
    client = caldav.DAVClient(pw.url)
    principal = client.principal()
    calendars = principal.calendars()

    calendar = create_new_calendar(principal, pw.calendar_name)

else:
    client = caldav.DAVClient(pw.url + pw.calendar_name + "/")
# client = caldav.DAVClient(pw.url)
    principal = client.principal()
calendars = principal.calendars()
# print(calendars)

# def add_reminder(dtstart, dtend, dtstamp, summary, )


# cal, dtstart, dtend, dtstamp = today, summary = "Test", publisher = "me", method = "PUBLISH", location = None, description = None, rrule = {'FREQ': 'YEARLY'}
if len(calendars) > 0:

    calendar = calendars[0]

    insert_event(calendar, True, datetime(2022, 4, 15, 2, 0, 1), datetime(
        2022, 4, 15, 8, 0, 1), datetime(2022, 4, 15, 0, 0, 1), summary="test")
