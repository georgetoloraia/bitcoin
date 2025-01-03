# network/network.py

from .node import Node
from .peer import Peer
import socket


class Network:
    def __init__(self):
        self.nodes = []

    def add_node(self, node):
        self.nodes.append(node)
        print(f"Node added: {node.address}:{node.port}")

    def connect_nodes(self, node1, node2):
        peer1 = Peer(node1)
        peer1.connect(node2)

    def broadcast_transaction(self, transaction):
        if self.nodes:
            for node in self.nodes:
                node.broadcast_transaction(transaction)

    def start_node(host, port):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((host, port))
        server.listen(5)
        print(f"Node started on {host}:{port}")

        while True:
            client, addr = server.accept()
            print(f"Connection from {addr}")
            data = client.recv(1024)
            print(f"Received: {data}")
            client.close()

