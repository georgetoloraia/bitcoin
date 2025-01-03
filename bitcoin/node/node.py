# node/node.py
"""
The central class to manage communication, blockchain, and consensus mechanisms.
"""

from network.connection_pool import ConnectionPool
from network.transaction_pool import TransactionPool
from network.peer_discovery import PeerDiscovery
from consensus.proof_of_stake import ProofOfStake
from blockchain.blockchain import Blockchain


class Node:
    def __init__(self, node_id, known_peers=None):
        self.node_id = node_id
        self.blockchain = Blockchain()
        self.transaction_pool = TransactionPool()
        self.connection_pool = ConnectionPool()
        self.peer_discovery = PeerDiscovery(known_peers or [])
        self.stakes = {}  # To manage Proof-of-Stake validators
        self.consensus_mechanism = ProofOfStake(self.blockchain)

    def start(self):
        """
        Starts the node by connecting to peers and syncing the blockchain.
        """
        print(f"Node {self.node_id} started")
        self.sync_blockchain()
        self.listen_for_messages()

    def sync_blockchain(self):
        """
        Syncs the blockchain with peers.
        """
        for peer in self.peer_discovery.get_random_peers():
            print(f"Requesting blockchain from peer {peer}")
            # Placeholder for actual sync logic

    def listen_for_messages(self):
        """
        Starts listening for incoming messages from peers.
        """
        print("Listening for messages...")
        # Placeholder for actual socket communication logic

    def broadcast_transaction(self, transaction):
        """
        Adds and broadcasts a transaction.
        """
        self.transaction_pool.add_transaction(transaction)
        self.connection_pool.broadcast(f"New Transaction: {transaction}")

    def mine_block(self):
        """
        Mines a block if no Proof-of-Stake is in use.
        """
        new_block = self.blockchain.create_new_block(
            self.transaction_pool.get_transactions()
        )
        if new_block:
            self.blockchain.add_block(new_block)
            self.connection_pool.broadcast(f"New Block: {new_block}")

    def validate_stake(self):
        """
        Executes the Proof-of-Stake mechanism to select a validator.
        """
        validator = self.consensus_mechanism.select_validator(self.stakes)
        print(f"Validator selected: {validator}")
        # Additional logic for block validation

    def handle_incoming_block(self, block):
        """
        Handles an incoming block from the network.
        """
        if self.consensus_mechanism.validate_block(block, block["validator"]):
            self.blockchain.add_block(block)
            print("Block accepted into the blockchain")
        else:
            print("Block rejected: validation failed")

    # Extend Node class in node/node.py

    def sync_blockchain(self):
        """
        Fetch the latest blockchain state from peers.
        """
        for peer in self.peer_discovery.get_random_peers():
            peer_blockchain = self.fetch_blockchain_from_peer(peer)
            if len(peer_blockchain) > len(self.blockchain.chain):
                print(f"Updating blockchain with peer {peer}'s state")
                self.blockchain.replace_chain(peer_blockchain)

    def fetch_blockchain_from_peer(self, peer):
        """
        Placeholder for fetching blockchain from a peer.
        """
        # Simulate a fetched chain for now
        return []
