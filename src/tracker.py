from pysolar import solar as sol
import pytz
import sys
import os
import time
import datetime
import json


def get_date():
    utc_date = pytz.utc.localize(datetime.datetime.utcnow())
    return utc_date


def get_data(lat, lon, date_):
    data = {
        'altitude': sol.get_altitude(lat, lon, date_),
        'azimuth': sol.get_azimuth(lat, lon, date_),
        'timestamp': date_.timestamp()
    }
    return data


def log_data(data_, log_file):
    path_ = os.path.join('..', 'logs', log_file)
    with open(path_, 'a') as f:
        f.write(f"{data_['altitude']},{data_['azimuth']},{data_['timestamp']}\n")


if __name__ == '__main__':
    # command line argument sets a delay between measurements
    delay = float(sys.argv[1])

    params = {}
    with open("params.json") as f:
        params = json.load(f)

    while 1:
        date = get_date()
        data = get_data(params['latitude'], params['longitude'], date)
        log_data(data, 'tracking.csv')
        time.sleep(delay)
