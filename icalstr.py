
class icalstr:
    def __init__(self, icalinfos):
        self.icalstr = """BEGIN:VCALENDAR
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

        self.alarmstr = """
        BEGIN:VALARM
        {trigger}{repeat}
        DURATION:PT15M
        ACTION:DISPLAY
        {alarm_description}
        END:VALARM
        """
        self.info = icalinfos
        if self.info.mode == "calit":
            self.alarmmode = False
        elif self.info.mode == "remindme":
            self.alarmmode = True
        self.alarm = self.fill_alarmstr(self.info.trigger, self.info.repeat, self.info.aldesc)

    def fill_alarmstr(self, trigger, repeat=None, alarm_description=None):
        """
        Fills alarmstr with alarm information.
        @param isalarm: bool if there should be a alarm.
        @param trigger: Time of trigger
        @param repeat: repitition of alarm
        @param alarm_description: description of alarm
        """

        if repeat:
            repeat = "\nREPEAT:" + repeat
        else:
            repeat = ""
        if alarm_description:
            alarm_description = "\nDESCRIPTION:" + alarm_description
        if self.alarmmode:
            alertstr = self.alarmstr.format(trigger=trigger,
                                            repeat=repeat,
                                            alarm_description=alarm_description
                                            )
        else:
            self.alarm = ""
            return
        self.alarm = alertstr
        return

    def fill_icalstr(self):
        """
        Fills icalstr with event information.
        @param start: start time of event
        @param end: end time of event
        @param stamp: timestamp of publication
        @param summary: Summary of event (that occurs as its name in calendar)

        @param publisher: App or Name that published the event. (seperated by //)
        @param method: PUBLISH (post event immediately) / REQUEST (send a event request) (Default is PUBLISH)
        @param location: Location of event (Default is None)
        @param description: Description of event (Default is None)
        @param cls: PUBLIC / PRIVATE (Default is PUBLIC)
        @param rule: repitition rule (Default is None)
        """
        # if rule is not None:
        #     rrule = "FREQ={}\n".format(self.info.rule)
        # else:
        #     rrule = ""
        # if not description:
        #     description = ""
        # if not location:
        #     location = ""
        finalstr = self.icalstr.format(
            publisher=self.info.publisher,
            location=self.info.location,
            summary=self.info.summary,
            description=self.info.description,
            cls=self.info.cls,
            start=self.info.begin,
            end=self.info.end,
            stamp=self.info.stamp,
            alarm=self.alarm,
            rrule=self.info.rrule)
        return finalstr
