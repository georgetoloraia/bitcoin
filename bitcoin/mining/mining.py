# mining/mining.py
# Implements Proof-of-Work mining logic.

import hashlib
import time


class Miner:
    def __init__(self, blockchain, difficulty=4):
        self.blockchain = blockchain
        self.difficulty = difficulty

    def mine_block(self, previous_hash, transactions):
        """
        Mines a new block by solving the Proof-of-Work challenge.
        """
        nonce = 0
        timestamp = int(time.time())
        while True:
            block_data = f"{previous_hash}{transactions}{timestamp}{nonce}"
            block_hash = hashlib.sha256(block_data.encode()).hexdigest()
            if block_hash.startswith("0" * self.difficulty):
                print(f"Block mined: {block_hash}")
                return {
                    "previous_hash": previous_hash,
                    "transactions": transactions,
                    "timestamp": timestamp,
                    "nonce": nonce,
                    "hash": block_hash,
                }
            nonce += 1

    def start_mining(self):
        """
        Continuously mines new blocks and adds them to the blockchain.
        """
        while True:
            last_block = self.blockchain.get_last_block()
            previous_hash = last_block["hash"] if last_block else "0" * 64
            transactions = self.blockchain.get_pending_transactions()
            new_block = self.mine_block(previous_hash, transactions)
            self.blockchain.add_block(new_block)
