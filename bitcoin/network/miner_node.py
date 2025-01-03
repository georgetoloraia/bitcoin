# miner_node.py

from mining.mining import Miner
from network.p2p import P2PNode
from blockchain.blockchain import Blockchain
import threading


class MinerNode:
    def __init__(self, host="127.0.0.1", port=8333):
        self.blockchain = Blockchain()
        self.miner = Miner(self.blockchain)
        self.p2p_node = P2PNode(host, port)

    def start(self):
        """
        Starts the miner and network communication.
        """
        threading.Thread(target=self.p2p_node.start_node).start()
        threading.Thread(target=self.miner.start_mining).start()


if __name__ == "__main__":
    miner_node = MinerNode()
    miner_node.start()
