from datetime import datetime, timedelta, time
import caldav
from ical_helpers import ical_helpers
from icalinfos import icalinfos
import pw
from search_remindmes import search_remindmes


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

        self.set_helper()
        self.searcher = search_remindmes()
        self.searcher.walk()
        self.run()

    def set_helper(self):
        self.helper = ical_helpers(self.principal, self.calendar)
        self.info = icalinfos(self.helper)

    def run(self):
        for f in self.searcher.searchables:
            suc = self.info.get_md_info(self.searcher.searchables[f])
            print(suc)
            if suc:
                print("ja")
                self.helper.set_infos(self.info)
                if f != "/home/lyse/Nextcloud/obsidian/zeugs/Templates/REMINDME.md":
                    self.helper.insert_event()
            # try:
            #     self.helper.insert_event()
            # except:
            #     print("could not create event")  # TODO

    def process_file(self, file):
        self.info.get_md_info(file=file)
        self.helper.set_infos(self.info)


remindme()
