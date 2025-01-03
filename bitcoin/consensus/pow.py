# consensus/pow.py

from time import time
from utils.crypto import double_sha256


class ProofOfWork:
    def __init__(self, difficulty):
        self.difficulty = difficulty

    def mine_block(self, block):
        """
        Mines a block by finding a nonce such that the block hash has a required number of leading zeros.
        """
        target = "0" * self.difficulty
        start_time = time()
        while not block.hash.startswith(target):
            block.nonce += 1
            block.hash = block.calculate_hash()
        end_time = time()

        print(f"Block mined: {block.hash}")
        print(f"Time taken: {end_time - start_time:.2f} seconds")
        return block

    def validate_proof(self, block):
        """
        Validates that a block's hash satisfies the difficulty requirement.
        """
        target = "0" * self.difficulty
        return block.hash.startswith(target)
