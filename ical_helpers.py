# class datetime.datetime
# A combination of a date and a time.
# Attributes: year, month, day, hour, minute, second, microsecond, and tzinfo.
from datetime import datetime, timedelta, time
from ical import *

dt_today = datetime.today()


def create_new_calendar(principal, cal_name):
    """Creates new calendar with given name.
    @param principal
    @param cal_name: name of calendar"""
    return principal.make_calendar(name=cal_name)


def get_time(dt):
    """
    Returns iCal time formatted string. "YYYYMMDDTHHMMSSZ"
    @param dt: daytime object
    """
    icaldtstr = "{year:04d}{month:02d}{day:02d}T{hour:02d}{minute:02d}{second:02d}Z".format(
        year=dt.year,
        month=dt.month,
        day=dt.day,
        hour=dt.hour,
        minute=dt.minute,
        second=dt.second
    )
    return icaldtstr


today = get_time(dt_today)


def insert_event(cal, dtstart, dtend, dtstamp=dt_today, summary="Test", publisher="me", method="PUBLISH", location=None, description=None, cls="PUBLIC", rrule={'FREQ': 'YEARLY'}):
    # fill_icalstr(dtstart, dtend, dtstamp, summary, publisher, method="PUBLISH", location=None, description=None, cls="PUBLIC", rule=None)
    insert = fill_icalstr(get_time(dtstart), get_time(dtend), get_time(dtstamp), summary,
                          publisher, method, location, description, cls, rrule)

    cal.save_event(insert)
    print("saved event.")


# print(today)
#print(datetime(2022, 5, 17, 18, 27).hour)


# eg_publisher = "me"
# eg_method = "PUBLISH"
# eg_location = "Nowhere"
# eg_summary = "Testitest"
# eg_description = "Describe"
# eg_cls = "PRIVATE"
# eg_uid = "20220516T060000Z-123401@example.com"
# eg_dtimestamp = "20220516T060000Z"
# eg_dtstart = "20220517T060000Z"
# eg_dtend = "20220517T230000Z"
# eg_rrule = "FREQ=YEARLY"
