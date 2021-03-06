from flask import Flask, request
import os
import json
import sqlite3
import datetime
import requests

"""
    TODO:
        + Add table, device settings
"""

app = Flask(__name__)
database = "dispenser.db"


@app.route("/", methods=["GET"])
def index():
    pass


@app.route("/api/devices/dispense_vol/<int:device_id> <int:vol>", methods=["POST"])
def set_dispense_vol(device_id, vol):
    with sqlite3.connect(database) as conn:
        cursor = conn.cursor()
        query = "SELECT ip FROM devices WHERE id == ?"
        val = (device_id, )
        cursor.execute(query, val)
        ip = cursor.fetchall()[0][0]

    requests.post(f"http://{ip}", str(vol))


@app.route("/api/devices/", methods=["GET"])
def get_all_devices():
    with sqlite3.connect(database) as conn:
        cursor = conn.cursor()
        query = "SELECT * FROM devices"
        cursor.execute(query)
        device = cursor.fetchall()

    return str(device), 201


@app.route("/api/devices/<int:device_id>", methods=["GET"])
def get_device(device_id):
    with sqlite3.connect(database) as conn:
        cursor = conn.cursor()
        query = "SELECT * FROM devices WHERE id == ?"
        entry = (device_id, )
        cursor.execute(query, entry)
        device = cursor.fetchall()

    return str(device), 201


@app.route("/api/devices", methods=["POST"])
def add_new_device():
    msg = json.loads(request.get_data())
    device_ip = msg["ip"]

    # Check to see if ip exists in database
    with sqlite3.connect(database) as conn:
        cursor = conn.cursor()
        query = "SELECT id FROM devices WHERE ip == ?"
        val = (device_ip, )
        cursor.execute(query, val)
        # because id is a unique value only one row should be retrieved
        data = cursor.fetchone()
        print(data)

    device_id = data
    if device_id is not None:
        return str(device_id), 201

    # find highest id number
    with sqlite3.connect(database) as conn:
        cursor = conn.cursor()
        query = "SELECT MAX(id) FROM devices WHERE ip == ?"
        val = (device_ip,)
        cursor.execute(query, val)
        # because id is a unique value only one row should be retrieved
        data = cursor.fetchone()
    device_id = data[0]

    if device_id is not None:
        device_id = int(data[0]) + 1
    else:
        device_id = 1

    # add device to database
    with sqlite3.connect(database) as conn:
        cursor = conn.cursor()
        query = """
                INSERT INTO devices
                    (
                         id,
                         ip,
                         dateTimeOfRegistration,
                         location,
                         dateLastMaintenance
                    )
                    VALUES (?, ?, ?, ?, ?)
            """

        entry = (device_id, device_ip, datetime.datetime.now().isoformat(), "SET DEVICE LOCATION", "N/A")
        cursor.execute(query, entry)
        conn.commit()

    return str(device_id), 201


@app.route("/api/activity", methods=["POST"])
def add_new_entry():
    msg = json.loads(request.get_data())
    device_id = msg["device_id"]
    date_time_iso = msg["date_time"]
    activity = msg["activity"]
    print("------")

    with sqlite3.connect(database) as conn:
        cursor = conn.cursor()
        query = """
                INSERT INTO deviceActivity
                    (
                        id, 
                        dateTime, 
                        type
                    )
                VALUES(?, ?, ?)
                """

        entry = (device_id, date_time_iso, activity)
        cursor.execute(query, entry)
        conn.commit()
        cursor.close()

    return "Successfully added entry", 201


def create_database():
    """
    Creates Tables for database
    """

    with sqlite3.connect(database) as conn:
        cursor = conn.cursor()
        cursor.execute(
            """
                CREATE TABLE deviceActivity
                    (
                       id       TEXT,
                       dateTime TEXT,
                       type     TEXT
                    )  
            """
        )

        cursor.execute(
            """
                CREATE TABLE devices
                  (
                     id                      TEXT   UNIQUE,
                     ip                      TEXT   UNIQUE,
                     dateTimeOfRegistration  TEXT,
                     location                TEXT,
                     dateLastMaintenance     TEXT
                  ) 
            """
        )

        conn.commit()
        cursor.close()
        print("Created Database with tables:")
        print("\tdeviceActivity")
        print("\t\tid                  TEXT")
        print("\t\tdateTime            TEXT")
        print("\t\ttype                TEXT")
        print("\tdevices")
        print("\t\tid                  TEXT")
        print("\t\tdataOfRegistration  TEXT")
        print("\t\ttimeOfRegistration  TEXT")
        print("\t\tlocation            TEXT")
        print("\t\tbatteryLevel        FLOAT")
        print("\t\tfluidLevel          FLOAT")
        print("\t\tdateLastMaintenance TEXT")


def main():
    if not os.path.exists(database):
        create_database()

    app.run(debug=True)


if __name__ == "__main__":
    main()
