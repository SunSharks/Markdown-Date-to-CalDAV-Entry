class icalstr:
    def __init__(self):
        self.data = {}
        alarm = fill_alarmstr(al_trig, al_rep, al_desc)

        publisher = publisher,
        location = location,
        summary = summary,
        description = description,
        cls = cls,
        start = start,
        end = end,
        stamp = stamp,
        ALARM = alarm,
        rrule = rrule)



self.alarmmode=alarmmode

self.icalstr="""BEGIN:VCALENDAR
VERSION:2.0
PRODID:{publisher}
BEGIN:VEVENT
UID:123456789@example.com
LOCATION:{location}
SUMMARY:{summary}
DESCRIPTION:{description}
CLASS:{cls}
DTSTART:{start}
DTEND:{end}
DTSTAMP:{stamp}{ALARM}
END:VEVENT
END:VCALENDAR"""
if self.alarmmode:
    self.alarmstr="""
    BEGIN:VALARM
    {trigger}
    REPEAT:{repeat}
    DURATION:PT15M
    ACTION:DISPLAY
    DESCRIPTION:{alarm_description}
    END:VALARM"""
else:
    self.alarmstr=""
