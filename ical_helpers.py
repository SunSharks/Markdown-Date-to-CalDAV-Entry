# class datetime.datetime
# A combination of a date and a time.
# Attributes: year, month, day, hour, minute, second, microsecond, and tzinfo.
from datetime import datetime, timedelta, time
from ical import *


class ical_helpers:
    def __init__(self, principal, calendar, alarmmode):
        self.dt_today = datetime.today()
        self.today = self.get_time(self.dt_today)
        self.principal = principal
        self.calendar = calendar
        self.alarmmode = alarmmode

    def create_new_calendar(self, cal_name):
        """Creates new calendar with given name.
        @param principal
        @param cal_name: name of calendar"""
        self.calendar = self.principal.make_calendar(name=cal_name)
        return self.calendar

    def get_time(self, dt):
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

    def get_trigger_time(self, mode, value):
        """Returns iCal-formatted string for reminder trigger.
        @param mode: before/after/time
        @param value: <amount>H/M/S if mode is "before" or "after";
         datetime object if mode == "time"
         """
        if mode == "time":
            trigstr = "TRIGGER;VALUE=DATE-TIME:"
            trigstr += get_time(value)
        elif mode == "before":
            trigstr = "TRIGGER:-P" + value
        elif mode == "after":
            trigstr = "TRIGGER;RELATED=END:P" + value
        else:
            trigstr = ""
            print("mode has to be 'before', 'after' or 'time'.")
        return trigstr

    def insert_event(self, dtstart, dtend, summary="Test", publisher="me", method="PUBLISH", location=None, description=None, cls="PUBLIC", rrule={'FREQ': 'YEARLY'},  al_trig=None, al_rep=None, al_desc=""):
        # fill_icalstr(dtstart, dtend, dtstamp, summary, publisher, method="PUBLISH", location=None, description=None, cls="PUBLIC", rule=None)
        insert = fill_icalstr(self.alarmmode, self.get_time(dtstart), self.get_time(dtend), self.today, summary,
                              publisher, method, location, description, cls, rrule, al_trig, al_rep, al_desc)

        self.calendar.save_event(insert)
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
