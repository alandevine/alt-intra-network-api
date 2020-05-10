#!/usr/bin/python3

from threading import Thread

import json
import socket


class Server:

    def __init__(self, server_config_file):
        """Constructor Class

        :param server_config_file: path to json config file
        :type server_config_file: str
        """

        print("Initializing Server...")
        self.connected_devices = {}
        self.shutdown = False

        self.server_config_file = server_config_file

        with open(self.server_config_file) as config_file:
            config = json.load(config_file)
            self.host = config["settings"]["host"]
            self.port = config["settings"]["port"]
            self.client_limit = config["settings"]["client_limit"]

        print(f"Host ip address     : {self.host}")
        print(f"Port number         : {self.port}")
        print(f"Server client limit : {self.client_limit}")

        self.soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.soc.bind((self.host, self.port))
        self.soc.listen(self.client_limit)

    def start_client_thread(self, client, addr):
        """Method for creating client threads
        :param client:
        :param addr:
        """
        th = Thread(target=self._client_thread, args=(client, addr))
        th.start()
        self.connected_devices[client]["thread"] = th

    def _client_thread(self, client, addr):
        """

        :param client: New client socket
        :type client: socket
        :param addr: ip address for newly connected client
        :type addr: str
        """
        client.send("Connection to server established.".encode())
        connected = True

        while connected and not self.shutdown:
            try:
                i = 0
                client.send(f"{i}".encode())
            except Exception as e:
                print(f"Exception \"{e}\" detected from {addr}")
                continue
        client.close()

    def start_server(self):
        """

        """
        try:
            while True:
                connection, ip_addr = self.soc.accept()
                connection.settimeout(60)
                print(f"Device connected: {ip_addr}")
                self.start_client_thread(connection, ip_addr)

        except KeyboardInterrupt:

            print("\nServer shutting down")
            self.shutdown = True
            for connection in self.connected_devices:
                connection.close()
            print("Clients disconnected")
            self.soc.close()


if __name__ == '__main__':
    serv = Server("server_config.json")
    serv.start_server()
