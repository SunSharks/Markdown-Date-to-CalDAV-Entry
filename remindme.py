from datetime import datetime, timedelta, time
import caldav
from ical_helpers import ical_helpers
from icalinfos import icalinfos
import pw


class remindme:
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
        self.helper = ical_helpers(self.principal, self.calendar)
        self.info = icalinfos(self.helper)
        self.info.get_md_info(file="calit_test.md")
        self.helper.set_infos(self.info)
        self.helper.insert_event()
# tstart, dtend, summary="Test", publisher="me", method="PUBLISH", location=None, description=None, cls="PUBLIC", rrule={'FREQ': 'YEARLY'},  al_trig=None, al_rep=None, al_desc=""


remindme()
