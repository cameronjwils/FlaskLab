from flask import render_template, request
from app import app
from models.events import *
from models.event import *

@app.route('/Home')
def index():
    return render_template('index.html', title = "Home", events=events)

@app.route('/Home', methods=['POST'])
def add_event():
    event_name = request.form['name']
    event_date = request.form['date']
    event_number_of_guests = request.form['number_of_guests']
    event_room_location = request.form['room_location']
    event_description = request.form['description']
    event_recurring = True if 'recurring' in request.form else False

    # completed = request.form['completed']
    # if (completed != "True"):
    #     event_completed = False
    # else:
    #     event_completed = True
    new_event = Event(event_name, event_date, event_number_of_guests, event_room_location, event_description, event_recurring)
    add_new_event(new_event)
    return render_template('index.html', title = "Home", events=events)
