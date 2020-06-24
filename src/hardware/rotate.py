#!/usr/bin/env python3

import os
import sys
import time
from datetime import datetime
import json
import logging
import pytz
import pifacedigitalio as pfio
from dotenv import load_dotenv


is_running = False
is_piface = False
is_listening = False

piface = None
relay = None
input_listener = None

start_dt = None


def get_json(path):
    with open(path, 'r') as f:
        json_data = json.load(f)
    return json_data


def get_params(path):
    return get_json(path)


def get_hourly_checklist(path):
    return get_json(path)


def update_checklist(checklist, hour):
    checklist[hour] = True
    logging.debug("Updating hourly checklist for hour: %s (%d).", hour, int(checklist[hour]))
    with open(os.getenv("CHECKLIST"), 'w') as f:
        json.dump(checklist, f, indent=4)
    logging.debug("Checklist updated.")


def start_rotating():
    global is_running
    is_running = True
    logging.info("Starting rotation...")
    global input_listener
    input_listener.activate()
    global is_listening
    is_listening = True
    logging.debug("Input listener active...")
    global relay
    relay.turn_on()
    logging.info("Relay ON.")

 
def stop_rotating():
    global is_running
    is_running = False
    logging.info("Stopping rotation...")
    # listener.deactivate()
    # logging.debug("No longer listening for input events...")
    global relay
    relay.turn_off()
    logging.info("Relay OFF.")


def update_position(event):
    # sensor has triggered
    # increment the counter
    global current_position
    global planned_position
    
    current_position += 1
    logging.info("Position: %d (%d)", current_position, planned_position)
    if current_position >= planned_position:
        stop_rotating()


def cleanup():  # !!! NOT DONE !!!
    if is_piface:
        global piface
        piface.relays[0].turn_off()
    if is_listening:
        global input_listener
        input_listener.deactivate()
    sys.exit(1)


def abort(code):
    if code == 1:
        logging.warning("ROTATION ALREADY COMPLETED FOR THIS HOUR.\nAborting...(%d)", code)
        cleanup()
    elif code == 2:
        global planned_position
        global params
        logging.error("PLANNED POSITION: %d EXCEEDS MAX_POSITION: %d.\nAborting...(%d)", planned_position, params["MAX_POSITION"], code)
        cleanup()


def get_current_dt():
    """
    Returns a tuple of datetime objects, both utc[0] and local[1]
    """

    utc_dt = pytz.utc.localize(datetime.utcnow())
    local_dt = utc_dt.astimezone(pytz.timezone(os.getenv(LOCAL_TIMEZONE)))  # TODO: add local timezone to env

    return utc_dt, local_dt


def setup_piface():
    global is_piface
    is_piface = True
    return pfio.PiFaceDigital()


if __name__ == "__main__":
    load_dotenv()
    logging.basicConfig(filename=os.getenv("LOGFILE"), filemode='a', format="(%(process)d) %(asctime)s - %(message)s", level=logging.INFO)
    start_dt = get_current_dt()[1]

    logging.info("Started.")

    hourly_checklist = get_hourly_checklist(os.getenv("CHECKLIST"))
    logging.debug("Checklist aquired.")
    current_hour = str(start_dt.hour)
    logging.debug("Attempting rotation for hour: %s .", current_hour)
    if hourly_checklist[current_hour] == True:
        abort(1)

    logging.info("Checklist in order, moving on...")
    params = get_params(os.getenv("ROTATION_PARAMS"))
    time_map = params["time_map"]
    logging.debug("Parameters aquired.")

    # TODO: add try-except in case the board is missing
    # also move the initialisation in its own function
    logging.debug("Initialising PiFace...")
    piface = setup_piface()
    relay = piface.relays[0]  # TODO: add relay var to .env or params
    logging.info("PiFace initialised.")

    logging.debug("Creating event listener...")
    input_listener = pfio.InputEventListener(chip=piface)
    input_listener.register(0, pfio.IODIR_ON, update_position)  # TODO: add pin_num var to .env or params
    logging.info("Listening for input events on pin: %d", 0)

    logging.debug("Getting current position...")
    current_position = time_map[current_hour]
    logging.info("Current position is: %d", current_position)
    logging.debug("Calculating planned position...")
    planned_position = current_position + params["ROT_AMOUNT"]
    logging.info("Planned position is: %d", planned_position)

    if planned_position <= params["MAX_POSITION"]:
        start_rotating()
    else:
        abort(2)

    while is_running:
        # dt = get_current_dt()
        logging.debug("In progress... waiting for sensor event.")
        time.sleep(1)

    input_listener.deactivate()
    logging.debug("No longer listening for input events...")
    update_checklist(hourly_checklist, current_hour)
    logging.info("Rotation finished successfully.")
    logging.shutdown()
