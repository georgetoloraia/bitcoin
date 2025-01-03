# network/p2p.py

import socket
import threading
import json
from core.blockchain import Blockchain, CBlock


class P2PNode:
    def __init__(self, host="127.0.0.1", port=8333):
        self.host = host
        self.port = port
        self.peers = []
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.blockchain = Blockchain()

    def start_node(self):
        """
        Starts the P2P node and listens for incoming connections.
        """
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)
        print(f"Node running at {self.host}:{self.port}")

        threading.Thread(target=self.mine_blocks, daemon=True).start()

        while True:
            client_socket, address = self.server_socket.accept()
            print(f"Connected to {address}")
            threading.Thread(target=self.handle_client, args=(client_socket,)).start()

    def handle_client(self, client_socket):
        """
        Handles incoming messages from a peer.
        """
        try:
            while True:
                message = client_socket.recv(1024).decode()
                if not message:
                    break
                self.handle_message(message)
        finally:
            client_socket.close()

    def handle_message(self, message):
        """
        Processes incoming messages.
        """
        try:
            data = json.loads(message)
            if data["type"] == "transaction":
                self.blockchain.add_transaction(data["data"])
                print(f"New transaction received: {data['data']}")
                self.broadcast(message)
            elif data["type"] == "block":
                print(f"New block received: {data['data']}")
                # Process the received block (not implemented here)
        except json.JSONDecodeError:
            print("Invalid message received")

    def broadcast(self, message):
        """
        Broadcasts a message to all connected peers.
        """
        for peer in self.peers:
            try:
                peer.send(message.encode())
            except:
                self.peers.remove(peer)

    def connect_to_peer(self, host, port):
        """
        Connects to another P2P node.
        """
        try:
            peer_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            peer_socket.connect((host, port))
            self.peers.append(peer_socket)
            print(f"Connected to peer {host}:{port}")
        except Exception as e:
            print(f"Could not connect to peer {host}:{port}: {e}")

    def mine_blocks(self):
        """
        Continuously mines blocks if there are pending transactions.
        """
        while True:
            if self.blockchain.pending_transactions:
                print("Mining a new block...")
                self.blockchain.mine_block()
                block = self.blockchain.chain[-1]
                block_data = {
                    "prev_hash": block.hashPrevBlock,
                    "merkle_root": block.hashMerkleRoot,
                    "transactions": block.vtx,
                    "timestamp": block.nTime,
                    "bits": block.nBits,
                    "nonce": block.nNonce,
                }
                message = json.dumps({"type": "block", "data": block_data})
                self.broadcast(message)
            threading.Event().wait(10)  # Adjust mining frequency if needed
