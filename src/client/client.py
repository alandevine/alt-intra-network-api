import json
import requests
import os
import sys
import time
from datetime import datetime


class Client:

    def __init__(self, client_config_file):
        self.client_config_file = client_config_file

        with open(self.client_config_file) as config_file:
            config = json.load(config_file)

            # network settings
            self.host = config["network_settings"]["host"]
            self.port = config["network_settings"]["port"]

            # hardware settings
            self.dispense_amount_ml = config["hardware_settings"]["dispense_amount_ml"]
            self.minimum_amount_ml = config["hardware_settings"]["minimum_amount_ml"]
            self.sanitizer_threshold = config["hardware_settings"]["sanitizer_threshold"]

            self.sensor_path = config["hardware_settings"]["sensor_path"]

        self.sensor_file = f"{os.getcwd()}/src/client/{self.sensor_path}"
        self.id = 2

        self.msg_backlog = []

        debug_str = []
        debug_str.append("[Network Settings]")
        debug_str.append(f"Host : {self.host}")
        debug_str.append(f"Port : {self.port}")
        debug_str.append("[Hardware Settings]")
        debug_str.append(f"Dispense Amount (in ml) : {self.dispense_amount_ml}")
        debug_str.append(f"Minimum_amount (in ml)  : {self.minimum_amount_ml}")
        debug_str.append(f"Sanitizer Threshold     : {self.sanitizer_threshold * 100}%")
        debug_str.append("-" * len(max(debug_str, key=len)))
        print("\n".join(debug_str))

    def client_loop(self):
        i = 1
        while True:
            print("run:", i)
            i += 1
            if os.path.exists(self.sensor_file):
                with open(self.sensor_file) as f:
                    activity = f.read()
                    dt = datetime.now().isoformat()
                    msg = json.dumps({"device_id": self.id, "activity": activity, "date_time": dt})

                    url = f"http://{self.host}:{self.port}/api/activity"

                    try:
                        requests.post(url, msg)

                        if len(self.msg_backlog) > 0:
                            for old_msg in self.msg_backlog:
                                requests.post(url, old_msg)
                            self.msg_backlog.clear()

                    except ConnectionError as e:
                        print(e)
                        self.msg_backlog.append(msg)

            time.sleep(5)




if __name__ == '__main__':
    cli = Client("src/client/client_config.json")
    cli.client_loop()
