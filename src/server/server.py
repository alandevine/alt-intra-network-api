from flask import Flask, request
import os
import json
import sqlite3

app = Flask(__name__)
database = "dispenser.db"


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
                     id                  TEXT,
                     dataOfRegistration  TEXT,
                     timeOfRegistration  TEXT,
                     location            TEXT,
                     batteryLevel        FLOAT,
                     fluidLevel          FLOAT,
                     dateLastMaintenance TEXT
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
