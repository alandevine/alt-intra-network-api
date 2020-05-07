#!/usr/bin/python3

from threading import Thread

import json
import socket

# flag that is changed upon server shutdown
SHUTDOWN = False

# dictionary containing client connections
CONNECTED_DEVICES = {}


def client_thread(client, addr):
    client.send("Connection to server established.".encode())
    connected = True

    while connected and not SHUTDOWN:
        try:
            # Main logic here
            pass
        except OSError as e:
            print(f"Exception \"{e}\" detected from {addr}")
            continue
    client.close()


def start_client_thread(client, addr):
    """Method for creating client threads"""
    th = Thread(target=client_thread, args=(client, addr))
    th.start()
    CONNECTED_DEVICES[client]["thread"] = th


def main():

    with open("./server_config.json") as config_file:
        config = json.load(config_file)
        host = config["settings"]["host"]
        port = config["settings"]["port"]
        client_limit = config["settings"]["client_limit"]

    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    soc.bind((host, port))
    soc.listen(client_limit)

    try:
        while True:
            connection, ip_addr = soc.accept()
            connection.settimeout(60)
            print(f"Device connected: {ip_addr}")
            start_client_thread(connection, ip_addr)

    except KeyboardInterrupt:
        print("Server shutting down")
        SHUTDOWN = True
        for connection in CONNECTED_DEVICES:
            connection.close()
        print("Clients disconnected")
        soc.close()


if __name__ == "__main__":
    main()
