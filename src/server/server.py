#!/usr/bin/python3

import socket
import json


def main():
    with open("./server_config.json") as config_file:
        config = json.load(config_file)
        host = config["settings"]["host"]
        port = config["settings"]["port"]

    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    soc.bind((host, port))
    soc.listen(5)


if __name__ == "__main__":
    main()
