import markdown

from datetime import datetime, timedelta, time
import caldav
from ical_helpers import ical_helpers
import pw


class calit:
    def __init__(self):

        self.client = caldav.DAVClient(pw.url)
        self.principal = self.client.principal()
        new_calendar = None
        if pw.create_new_calendar:
            new_calendar = self.create_new_calendar(self.principal, pw.calendar_name)
            self.calendar = new_calendar
        self.calendars = self.principal.calendars()

# cal, dtstart, dtend, dtstamp = today, summary = "Test", publisher = "me", method = "PUBLISH", location = None, description = None, rrule = {'FREQ': 'YEARLY'}
        if len(self.calendars) > 0 and not new_calendar:
            self.calendar = self.calendars[0]
        self.helper = ical_helpers(self.principal, self.calendar, False)

        self.helper.insert_event(datetime(2022, 4, 15, 2, 0, 1), datetime(
            2022, 4, 15, 8, 0, 1), datetime(2022, 4, 15, 0, 0, 1))

    def get_md_info(self):
        with open('calit_test.md', 'r') as f:
            self.cmdmd = markdown.markdown(f.read())
            print(self.cmdmd)


calit()
