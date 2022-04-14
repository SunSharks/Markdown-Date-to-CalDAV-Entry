from datetime import datetime, timedelta, time
from ical import *

today = datetime.combine(datetime.today(), time(0, 0))


def create_new_calendar(principal, cal_name):
    return principal.make_calendar(name=cal_name)


def insert_event(cal, dtstart=datetime(2022, 5, 17, 8), dtend=datetime(2022, 5, 18, 1), summary="Do the needful", rrule={'FREQ': 'YEARLY'}):

    eg_publisher = "me"
    eg_method = "PUBLISH"
    eg_location = "Nowhere"
    eg_summary = "Do the needful"
    eg_description = "Describe"
    eg_cls = "PRIVATE"
    eg_uid = "20200516T060000Z-123401@example.com"
    eg_dtimestamp = "20220516T060000Z"
    eg_dtstart = "20220517T060000Z"
    eg_dtend = "20220517T230000Z"
    eg_rrule = "FREQ=YEARLY"
# fill_icalstr(dtstart, dtend, dtstamp, summary, publisher, method="PUBLISH", location=None, description=None, cls="PUBLIC", rule=None)
    insert = fill_icalstr(eg_dtstart, eg_dtend, eg_dtimestamp, eg_summary,
                          eg_publisher, eg_method, eg_location, eg_description, eg_cls, eg_rrule)

    cal.save_event(insert)
    print("saved event.")
