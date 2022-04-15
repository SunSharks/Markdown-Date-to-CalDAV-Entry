class iCal:
    def __init__(self, alarmmode):
        self.alarmmode = alarmmode

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
        if self.alarmmode:
            self.alarmstr = """BEGIN:VALARM
            {trigger}
            REPEAT:{repeat}
            DURATION:PT15M
            ACTION:DISPLAY
            DESCRIPTION:{alarm_description}
            END:VALARM"""
        else:
            self.alarmstr = ""

    def fill_alarmstr(self, trigger, repeat, alarm_description):
        """
        Fills alarmstr with alarm information.
        @param isalarm: bool if there should be a alarm.
        @param trigger: Time of trigger
        @param repeat: repitition of alarm
        @param alarm_description: description of alarm
        """
        if self.alarmmode:
            self.alarmstr = self.alarmstr.format(trigger=trigger,
                                                 repeat=repeat,
                                                 alarm_description=alarm_description
                                                 )
        else:
            self.alarmstr = ""
        return self.alarmstr

    def fill_icalstr(self, start, end, stamp, summary, publisher, method="PUBLISH", location=None, description=None, cls="PUBLIC", rule=None):
        """
        Fills icalstr with event information.
        @param isalarm: bool if there should be a alarm.
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
        if rule is not None:
            rrule = "FREQ={}\n".format(rule)
        else:
            rrule = ""
        if not description:
            description = ""
        if not location:
            location = ""
        finalstr = icalstr.format(
            publisher=publisher,
            location=location,
            summary=summary,
            description=description,
            cls=cls,
            start=start,
            end=end,
            stamp=stamp,
            trigger=trigger,
            repeat=repeat,
            alarm_description=alarm_description,
            rrule=rrule)
        return finalstr


# if __name__ == "__main__()":
# publisher, method, location, summary, description, cls, dtstart, dtend, dtstamp, rule=None
# eg_publisher = "//Example Corp.//CalDAV Client//EN"
# eg_method = "PUBLISH"
# eg_location = "Nowhere"
# eg_summary = "Do the needful"
# eg_description = "Describe"
# eg_cls = "PRIVATE"
# eg_uid = "20200516T060000Z-123401@example.com"
# eg_dtimestamp = "20200516T060000Z"
# eg_dtstart = "20220517T060000Z"
# eg_dtend = "20220517T230000Z"
# eg_rrule = "FREQ=YEARLY"
#
# fill_icalstr(eg_publisher, eg_method, eg_location, eg_summary, eg_description, eg_cls, eg_dtstart, eg_dtend, eg_dtimestamp)

#
# BEGIN:VCALENDAR: Damit wird jede iCalendar-Datei eröffnet.
# VERSION: Angegeben wird hier die Version des Formats, aktuell "2.0".
# PRODID: Hier wird der Name oder die Adresse des Erstellers bzw. der verwendeten Anwendung eingetragen.
# METHOD: Zeigt an, wie dem Empfänger der Eintrag übermittelt wird. Dabei gibt es zwei Arten: Mit PUBLISH erscheint ein Eintrag sofort, während man den Termin mit REQUEST in eine Anfrage verpackt.
# BEGIN:VEVENT: Diese Zeile markiert den Beginn des Bereichs, der die relevanten Daten des Termins enthält.
# UID: Jede ics-File und damit jeder Kalendereintrag benötigt einen unverwechselbaren Unique Identifier.
# LOCATION: An dieser Stelle nennt man den Veranstaltungsort, wobei man selbst entscheiden kann, wie genau.
# SUMMARY: Der Eintrag vermittelt eine kurze Zusammenfassung zum Termin.
# DESCRIPTION: An dieser Stelle erfolgt eine ausführliche Beschreibung, die nur zu sehen ist, wenn der Termineintrag geöffnet wird.
# CLASS: Hier entscheidet sich, ob der Termin öffentlich (PUBLIC) oder privat (PRIVATE) gespeichert werden soll.
# DTSTART: Gibt den Startzeitpunkt des Termins an.
# DTEND: Gibt an, bis wann der Termin eingeplant ist.
# DTSTAMP: Der Zeitstempel enthält die Information, wann der Kalendereintrag erstellt wurde.
# END:VEVENT: Die vorletzte Zeile beendet den Bereich mit Termininformationen.
# END:VCALENDAR: Schließt die Datei ab.
# Auch die Zeitangaben folgen einem normierten Format:
#
# Die ersten vier Ziffern entsprechen dem Jahr (YYYY): 2019
# Die nächsten zwei dem Monat (MM): 201910
# Die letzten beiden definieren den Tag (DD): 20191027
# Mit dem Buchstaben T trennen Sie Datum von Uhrzeit ab: 20191027T
# Die Uhrzeit wiederum besteht aus 6 Zahlen:
# zwei für die Stunde: 20191027T15
# zwei für die Minute: 20191027T1559
# zwei für die Sekunde: 20191027T155954
# Mit einem Z wird die Datumseingabe geschlossen: 20191027T155954Z


# Im folgenden Beispiel sind alle Zeilen entsprechend ausgefüllt.
#
# BEGIN:VCALENDAR
# VERSION:2.0
# PRODID:Cal_App//Daily@Planet
# METHOD:PUBLISH
# BEGIN:VEVENT
# UID:123456789@example.com
# LOCATION:Metropolis
# SUMMARY:Meeting
# DESCRIPTION:Kick-off Meeting
# CLASS:PUBLIC
# DTSTART:20191101T100000Z
# DTEND: 20191101T120000Z
# DTSTAMP: 20191027T155954Z
# END:VEVENT
# END:VCALENDAR
