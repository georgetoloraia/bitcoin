# consensus/proof_of_stake.py
"""
Implements a basic PoS mechanism as an alternative to Proof-of-Work.
"""

import random


class ProofOfStake:
    def __init__(self, blockchain):
        self.blockchain = blockchain

    def select_validator(self, stakes):
        """
        Selects a validator based on their stake.
        """
        total_stake = sum(stakes.values())
        rand = random.uniform(0, total_stake)
        current = 0
        for validator, stake in stakes.items():
            current += stake
            if current > rand:
                return validator

    def validate_block(self, block, validator):
        """
        Validates a block created by a validator.
        """
        last_block = self.blockchain.get_last_block()
        if last_block and block["previous_hash"] != last_block["hash"]:
            return False
        if validator not in self.blockchain.stakes:
            return False
        return True
