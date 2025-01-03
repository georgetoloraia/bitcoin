# main.py
from bitcoin.network.p2p import P2PNode

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Run a Bitcoin node.")
    parser.add_argument("--host", default="127.0.0.1", help="Host to bind the node to")
    parser.add_argument("--port", type=int, default=8333, help="Port to bind the node to")
    args = parser.parse_args()

    print(f"Starting Bitcoin Node at {args.host}:{args.port}...")

    node = P2PNode(host=args.host, port=args.port)  # Create an instance
    node.start_node()  # Start the node
