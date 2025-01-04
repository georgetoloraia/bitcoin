# blockchain/block.py

from bitcoin.utils.merkle import build_merkle_tree
from bitcoin.utils.crypto import double_sha256


class Block:
    def __init__(self, transactions, previous_hash):
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.merkle_root = build_merkle_tree(transactions)
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        data = str(self.transactions) + self.previous_hash + str(self.nonce)
        return double_sha256(data)

    def mine_block(self, difficulty):
        target = "0" * difficulty
        while not self.hash.startswith(target):
            self.nonce += 1
            self.hash = self.calculate_hash()
        print(f"Block mined: {self.hash}")

    def get_hash(self):
        return self.hash
