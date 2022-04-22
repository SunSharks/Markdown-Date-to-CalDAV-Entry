import markdown
from datetime import datetime, timedelta, time
SUMMARY_KW = "Was"
BEGIN_KW = "Beginn"
END_KW = "Ende"
LOCATION_KW = "Ort"
DESCRIPTION_KW = "Beschreibung"
RRULE_KW = "Regelmäßigkeiten"
CALENDAR_KW = "Kalender"
TRIGGER_KW = "Trigger"
REPETITION_KW = "Repetition"
ALARM_DESCRIPTION_KW = "Description"
TIME_SPLIT = "-"

# Trigger: < before > / < after > / < time > 15M
# Repetition:
#     Description:


class icalinfos:
    def __init__(self, helper):
        self.summary = ""
        self.begin = ""
        self.end = ""
        self.location = ""
        self.description = ""
        self.publisher = "me"
        self.rrule = ""
        self.calendar = ""
        self.trigger = ""
        self.repeat = ""
        self.alarm_desc = ""
        self.helper = helper
        self.method = "PUBLISH"
        self.cls = "PUBLIC"  # "PRIVATE"

    def get_md_info(self, md):
        cmdlst = md.split("\n")
        for i in cmdlst:
            i = i.strip()
            if ":" in i:
                ilst = i.split(":")
                ilst[1] = ilst[1].strip()
                if i.startswith(SUMMARY_KW):
                    self.summary = ilst[1].strip()
                elif i.startswith(BEGIN_KW):
                    try:
                        self.begin = self.translate_md_timestamps_to_datetime(ilst[1].strip())
                        print(self.begin)
                    except:
                        return False
                elif i.startswith(END_KW):
                    try:
                        self.end = self.translate_md_timestamps_to_datetime(ilst[1].strip())
                    except:
                        return False
                elif i.startswith(LOCATION_KW):
                    self.location = ilst[1].strip()
                elif i.startswith(DESCRIPTION_KW):
                    self.description = ilst[1].strip()
                elif i.startswith(RRULE_KW):
                    self.rrule = ilst[1].strip()
                elif i.startswith(CALENDAR_KW):
                    self.calendar = ilst[1].strip()
                elif i.startswith(TRIGGER_KW):
                    if ilst[1].endswith("before"):
                        mode = "before"
                        val = ilst[1].strip()[:-6].strip()
                    elif ilst[1].endswith("after"):
                        mode = "after"
                        val = ilst[1].strip()[:-5].strip()
                    elif ilst[1].endswith("time"):
                        mode = "time"
                        val = ilst[1].strip()[:-4].strip()
                    print(val)
                    self.trigger = self.helper.get_trigger_time(mode, val)
                elif i.startswith(REPETITION_KW):
                    self.repeat = ilst[1].strip()  # TODO
                elif i.startswith(ALARM_DESCRIPTION_KW):
                    self.alarm_desc = ilst[1].strip()
        return True

    def translate_md_timestamps_to_datetime(self, timestr):
        datelst = timestr.split(TIME_SPLIT)
        datelst = [int(i) for i in datelst]
        return datetime(*datelst)
