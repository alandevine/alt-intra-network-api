#!/usr/bin/python3

import socket
import json


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


if __name__ == '__main__':
    cli = Client("client_config.json")

