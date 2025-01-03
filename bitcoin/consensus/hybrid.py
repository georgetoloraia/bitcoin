# consensus/hybrid.py

from .pow import ProofOfWork
from .pos import ProofOfStake


class HybridConsensus:
    def __init__(self, difficulty, staking_wallets):
        self.pow = ProofOfWork(difficulty)
        self.pos = ProofOfStake(staking_wallets)

    def validate_and_mine_block(self, block):
        """
        Hybrid consensus:
        - Validator is chosen by PoS.
        - Block is mined using PoW.
        """
        validator = self.pos.select_validator()
        if not self.pos.validate_block(block, validator):
            raise ValueError("Invalid block or validator.")

        self.pow.mine_block(block)
        return block
