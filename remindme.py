
from datetime import datetime, timedelta, time
import caldav
from ical_helpers import *
import pw


class remindme:
    def __init__(self):
        if pw.create_new_calendar:
            self.connect_caldav(pw.url)
            for name in pw.calendar_names:
                pass

            create_new_calendar(principal, pw.calendar_name)

    def connect_caldav(self, url):
        self.client = caldav.DAVClient(url)
        self.principal = client.principal()
        self.calendars = principal.calendars()

    def match_calendars(self):
        for cn in:
            if cn in pw.calendar_names:
                pass
