from flask import Flask, request
from Database import Database as DB
import json

app = Flask(__name__)
database = DB("test.db")


@app.route("/", methods=["GET"])
def index():
    pass


@app.route("/api/devices", methods=["GET"])
def get_all_devices():
    pass


@app.route("/api/devices/<int:device_id>", methods=["GET"])
def get_device(device_id):
    pass


@app.route("/api/devices", methods=["POST"])
def add_new_device():
    pass


@app.route("/api/activity", methods=["POST"])
def add_new_entry():
    msg = json.loads(request.get_data())
    device_id = msg["device_id"]
    date_time_iso = msg["date_time"]
    activity = msg["activity"]

    print(f"{device_id}\t{date_time_iso}\t{activity}")
    return "success"


if __name__ == "__main__":
    app.run(debug=True)
