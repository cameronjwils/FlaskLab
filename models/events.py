from models.event import *

event1 = Event("29/5/22", "CodeClan Bingo", 20, "3B", "Bingo event for 20 people", True, False)
event2 = Event("13/2/21", "UWS confrence", 100,"5C", "Confrence for UWS lecturers", False, True)

events = [event1, event2]

def add_new_event(event):
    events.append(event)