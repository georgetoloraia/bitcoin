# network/connection_pool.py

import socket
import threading


class ConnectionPool:
    def __init__(self, max_connections=50):
        self.max_connections = max_connections
        self.connections = []
        self.lock = threading.Lock()

    def add_connection(self, host, port):
        """
        Adds a new peer connection to the pool.
        """
        if len(self.connections) >= self.max_connections:
            print("Connection pool is full. Cannot add more peers.")
            return False

        try:
            peer_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            peer_socket.connect((host, port))
            with self.lock:
                self.connections.append(peer_socket)
            print(f"Connected to peer {host}:{port}")
            return True
        except Exception as e:
            print(f"Failed to connect to {host}:{port}: {e}")
            return False

    def broadcast(self, message):
        """
        Sends a message to all connected peers.
        """
        with self.lock:
            for conn in self.connections:
                try:
                    conn.send(message.encode())
                except:
                    self.connections.remove(conn)

    def close_all(self):
        """
        Closes all peer connections.
        """
        with self.lock:
            for conn in self.connections:
                conn.close()
            self.connections = []
