from datetime import datetime
from flask import Flask
import json
import requests
import socket
import threading

DEVICE_ID = None
CLIENT_CONFIG_FILE = "client_config.json"
MSG_BACKLOG = []

app = Flask(__name__)

with open(CLIENT_CONFIG_FILE) as config_file:
    config = json.load(config_file)

    # network settings
    host = config["network_settings"]["host"]
    port = config["network_settings"]["port"]

    # hardware settings
    dispense_amount_ml = config["hardware_settings"]["dispense_amount_ml"]
    minimum_amount_ml = config["hardware_settings"]["minimum_amount_ml"]
    sanitizer_threshold = config["hardware_settings"]["sanitizer_threshold"]

    sensor_file = config["hardware_settings"]["sensor_path"]

IP = socket.gethostbyname(socket.gethostname())
ID = requests.post(f"http://{host}:{port}/api/devices", json.dumps({"ip": IP})).text
print(f"Device ID: {ID}")

# this should be read from /dev/battery
BATTERY_LEVEL = 100
FLUID_LEVEL = 100


@app.route("/config/dispense_amount_ml/<float:val>", methods=["POST"])
def set_dispense_amount(val):
    update_config("dispense_amount_ml", val)


@app.route("/device/battery_level", methods=["GET"])
def get_battery_level():
    return str(BATTERY_LEVEL), 201


@app.route("/device/fluid_level", methods=["GET"])
def get_fluid_level():
    return str(FLUID_LEVEL), 201


def update_config(key, value):
    try:
        config["hardware_settings"][key] = value
    except ValueError:
        pass

    with open(CLIENT_CONFIG_FILE, "w") as conf:
        conf.write((json.dumps(config, indent=4)))


def client_loop():

    global FLUID_LEVEL

    while True:
        # client should not be able to send data before receiving id from server
        if DEVICE_ID is None:
            continue

        with open(sensor_file, "w+") as f:
            activity = f.read()
            # clear sensor file
            f.write("")
            if activity == "":
                continue

            if activity == "dispense":
                FLUID_LEVEL -= dispense_amount_ml
                # also update env variable

            dt = datetime.now().isoformat()
            msg = json.dumps({"device_id": DEVICE_ID, "activity": activity, "date_time": dt})

            url = f"http://{host}:{port}/api/activity"

            try:
                requests.post(url, msg)

                if len(MSG_BACKLOG) > 0:
                    for old_msg in MSG_BACKLOG:
                        requests.post(url, old_msg)
                    MSG_BACKLOG.clear()

            except ConnectionError as e:
                print(e)
                MSG_BACKLOG.append(msg)


def main():
    loop = threading.Thread(target=client_loop)
    loop.start()
    app.run(debug=True)


if __name__ == "__main__":
    main()
