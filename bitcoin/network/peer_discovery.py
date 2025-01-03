# network/peer_discovery.py

import random


class PeerDiscovery:
    def __init__(self, known_peers):
        self.known_peers = known_peers

    def discover_peers(self, new_peers):
        """
        Adds new peers to the known list.
        """
        self.known_peers.update(new_peers)

    def get_random_peers(self, count=5):
        """
        Retrieves a random subset of peers for connection.
        """
        return random.sample(self.known_peers, min(count, len(self.known_peers)))
