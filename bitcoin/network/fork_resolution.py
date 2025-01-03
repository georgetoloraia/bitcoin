# network/fork_resolution.py
"""
Handles chain forks and ensures nodes converge on the longest valid chain.
"""


class ForkResolution:
    def __init__(self, blockchain):
        self.blockchain = blockchain

    def handle_fork(self, incoming_chain):
        """
        Resolves a fork by comparing the local chain with the incoming chain.
        """
        if len(incoming_chain) > len(self.blockchain.chain):
            if self.validate_chain(incoming_chain):
                print("Replacing local chain with the incoming longer chain.")
                self.blockchain.replace_chain(incoming_chain)
            else:
                print("Incoming chain is invalid. Fork rejected.")
        else:
            print("Local chain is already the longest.")

    def validate_chain(self, chain):
        """
        Validates the integrity and continuity of a blockchain.
        """
        for i in range(1, len(chain)):
            if chain[i]["previous_hash"] != chain[i - 1]["hash"]:
                return False
        return True
