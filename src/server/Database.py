import sqlite3
import os
import random


class Database:
    """Interface class between database and Server"""

    def __init__(self, db_path):

        if os.path.exists(f"{os.getcwd()}/{db_path}"):
            self.db = sqlite3.connect(db_path)
            self.cursor = self.db.cursor()

        else:
            self.db = sqlite3.connect(db_path)
            self.cursor = self.db.cursor()
            self._create_tables()

        self.cursor = self.db.cursor()

    def insert_device_activity(self, device_id, date, time, activity_type):
        """
        :param device_id: Unique Device ID
        :type device_id: integer
        :param date: Date of message in ISO format
        :type date: string
        :param time: Time of message
        :type time: string
        :param activity_type: Nature of message
        :type activity_type: string
        """
        query = """
                INSERT INTO deviceActivity
                    (
                        id, 
                        date, 
                        time, 
                        type
                    )
                VALUES(?, ?, ?, ?)
                """

        vals = (device_id, date, time, activity_type)
        self.cursor.execute(query, vals)
        self.db.commit()

    def get_device_activity(self, device_id):
        query = "SELECT * FROM deviceActivity WHERE id == :device_id"
        self.cursor.execute(query, {"device_id": device_id})
        device = self.cursor.fetchall()
        return device

    def get_all_device_activity(self):
        self.cursor.execute("SELECT * FROM deviceActivity")
        devices = self.cursor.fetchall()
        return devices

    def _create_tables(self):
        """
        Creates Tables for database
        """
        self.cursor.execute(
                """
                    CREATE TABLE deviceActivity
                        (
                           id   TEXT,
                           date TEXT,
                           time TEXT,
                           type TEXT
                        )  
                """
            )

        self.cursor.execute(
                """
                    CREATE TABLE devices
                      (
                         id                  INT,
                         dataOfRegistration  TEXT,
                         timeOfRegistration  TEXT,
                         location            TEXT,
                         batteryLevel        FLOAT,
                         fluidLevel          FLOAT,
                         dateLastMaintenance TEXT
                      ) 
                """
            )

        self.db.commit()


if __name__ == '__main__':
    db = Database("test.db")
    db.insert_device_activity(str(random.randint(5, 20)), "2020/06/10", "17:11", "Dispense")
    db.insert_device_activity("2", "2020/06/10", "17:11", "Dispense")

    print(db.get_all_device_activity())
    print("------------------")
    print(db.get_device_activity(2))


    db.db.close()
    os.remove("test.db")
