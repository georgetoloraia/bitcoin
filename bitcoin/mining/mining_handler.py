# mining/mining_handler.py

"""
Handles mining logic and ties it to the node.
"""

import threading
import time


class MiningHandler:
    def __init__(self, node, mining_interval=10):
        self.node = node
        self.mining_interval = mining_interval
        self.is_mining = False

    def start_mining(self):
        """
        Starts the mining process.
        """
        self.is_mining = True
        threading.Thread(target=self.mine_blocks).start()

    def stop_mining(self):
        """
        Stops the mining process.
        """
        self.is_mining = False

    def mine_blocks(self):
        """
        Mines blocks periodically.
        """
        while self.is_mining:
            self.node.mine_block()
            time.sleep(self.mining_interval)
