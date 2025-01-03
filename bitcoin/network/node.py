# network/node.py


class Node:
    def __init__(self, node_id, address, port):
        self.node_id = node_id
        self.address = address
        self.port = port
        self.peers = []  # List of connected peer nodes
        self.blockchain = None

    def connect_peer(self, peer_node):
        if peer_node not in self.peers:
            self.peers.append(peer_node)
            print(f"Connected to peer: {peer_node.address}:{peer_node.port}")

    def disconnect_peer(self, peer_node):
        if peer_node in self.peers:
            self.peers.remove(peer_node)
            print(f"Disconnected from peer: {peer_node.address}:{peer_node.port}")

    def broadcast_block(self, block):
        for peer in self.peers:
            peer.receive_block(block)

    def receive_block(self, block):
        print(f"Received block with hash: {block.get_hash()}")
        # Placeholder for block validation and addition to the blockchain

    def broadcast_transaction(self, transaction):
        for peer in self.peers:
            peer.receive_transaction(transaction)

    def receive_transaction(self, transaction):
        print(f"Received transaction with hash: {transaction.get_hash()}")
        # Placeholder for transaction validation and mempool addition
