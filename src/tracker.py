from pysolar import solar as sol
import datetime
import json


if __name__ == '__main__':
    params = {}
    with open("params.json") as f:
        params = json.load(f)
    for k, v in params.items():
        print(k, v, type(v))
