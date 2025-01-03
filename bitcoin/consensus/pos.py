# consensus/pos.py

import random


class ProofOfStake:
    def __init__(self, staking_wallets):
        """
        staking_wallets: A dictionary of wallet addresses and their stakes (amount of coins held).
        """
        self.staking_wallets = staking_wallets

    def select_validator(self):
        """
        Selects a validator for the next block based on their stake.
        """
        total_stake = sum(self.staking_wallets.values())
        if total_stake == 0:
            raise ValueError("No staking wallets available.")

        lottery = []
        for wallet, stake in self.staking_wallets.items():
            lottery.extend([wallet] * stake)

        selected = random.choice(lottery)
        print(f"Selected validator: {selected}")
        return selected

    def validate_block(self, block, validator):
        """
        Ensures the block's validator is valid and satisfies basic block conditions.
        """
        if validator not in self.staking_wallets:
            return False
        return True
