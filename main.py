from bitcoin.blockchain.blockchain import Blockchain
from bitcoin.mining.mining import Miner
from bitcoin.network.p2p import P2PNode
import threading
import argparse

def main():
    parser = argparse.ArgumentParser(description="Blockchain Node")
    parser.add_argument("--host", type=str, default="127.0.0.1", help="Node host")
    parser.add_argument("--port", type=int, default=8333, help="Node port")
    parser.add_argument("--mine", action="store_true", help="Enable mining")
    args = parser.parse_args()

    blockchain = Blockchain()
    node = P2PNode(args.host, args.port)

    node_thread = threading.Thread(target=node.start_node)
    node_thread.start()

    if args.mine:
        Miner.start_mining(blockchain)

if __name__ == "__main__":
    main()
