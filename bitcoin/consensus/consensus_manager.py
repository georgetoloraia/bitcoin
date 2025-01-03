# consensus/consensus_manager.py

from .pow import ProofOfWork
from .pos import ProofOfStake
from .hybrid import HybridConsensus


class ConsensusManager:
    def __init__(self, mechanism="pow", difficulty=4, staking_wallets=None):
        self.mechanism = mechanism
        self.staking_wallets = staking_wallets or {}
        self.consensus = self.initialize_mechanism(mechanism, difficulty)

    def initialize_mechanism(self, mechanism, difficulty):
        if mechanism == "pow":
            return ProofOfWork(difficulty)
        elif mechanism == "pos":
            return ProofOfStake(self.staking_wallets)
        elif mechanism == "hybrid":
            return HybridConsensus(difficulty, self.staking_wallets)
        else:
            raise ValueError(f"Unknown consensus mechanism: {mechanism}")

    def process_block(self, block):
        """
        Processes a block using the chosen consensus mechanism.
        """
        if self.mechanism == "pow":
            return self.consensus.mine_block(block)
        elif self.mechanism == "pos":
            validator = self.consensus.select_validator()
            if not self.consensus.validate_block(block, validator):
                raise ValueError("Invalid block or validator.")
            print(f"Block validated by {validator}")
            return block
        elif self.mechanism == "hybrid":
            return self.consensus.validate_and_mine_block(block)
