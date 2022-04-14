icalstr = """BEGIN:VCALENDAR
VERSION:2.0
PRODID:{publisher}
METHOD:{method}
BEGIN:VEVENT
UID:123456789@example.com
LOCATION:{location}
SUMMARY:{summary}
DESCRIPTION:{description}
CLASS:{cls}
DTSTART:{dtstart}
DTEND:{dtend}
DTSTAMP:{dtstamp}
END:VEVENT
END:VCALENDAR"""


def fill_icalstr(dtstart, dtend, dtstamp, summary, publisher, method="PUBLISH", location=None, description=None, cls="PUBLIC", rule=None):
    """
    Fills icalstr with event information.
    @param dtstart: start time of event
    @param dtend: end time of event
    @param dtstamp: timestamp of publication
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

    ficalstr = icalstr.format(
        publisher=publisher,
        method=method,
        location=location,
        summary=summary,
        description=description,
        cls=cls,
        dtstart=dtstart,
        dtend=dtend,
        dtstamp=dtstamp,
        rrule=rrule)
    return ficalstr


def make_event_str(self, name, start, end, rule=None):
    tstamp = dt.now(tz=timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    start_utc = start.astimezone(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    end_utc = end.astimezone(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    _id = hashlib.sha1(bytes(tstamp+name, 'utf-8')).hexdigest()
    if rule is not None:
        rrule = "FREQ={}\n".format(rule)
    else:
        rrule = ""
    s = """BEGIN:VCALENDAR
    VERSION:2.0
    PRODID:-//Sabre//Sabre VObject 4.3.0//EN
    BEGIN:VEVENT
    UID:{}
    DTSTAMP:{}
    DTSTART:{}
    DTEND:{}
    {}SUMMARY:{}
    END:VEVENT
    END:VCALENDAR
    """.format(_id, tstamp, start_utc, end_utc, rrule, name)
    return ''.join(s.split('\t'))


def makeEvent(self, calendarObj, start, end, name, rule=None, owner='your'):
    eventString = self.makeEventString(name, start, end, rule=rule)
    try:
        _ = calendarObj.save_event(eventString)

    except Exception as e:
        self.log.error(e)

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
