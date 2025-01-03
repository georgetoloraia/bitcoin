# network/consensus.py


class Consensus:
    def __init__(self, blockchain):
        self.blockchain = blockchain

    def validate_block(self, block):
        """
        Validates a new block before adding it to the chain.
        """
        previous_block = self.blockchain.get_last_block()
        if previous_block and block["previous_hash"] != previous_block["hash"]:
            return False
        # Add further validations (e.g., Proof-of-Work)
        return True

    def resolve_conflicts(self, peer_chains):
        """
        Resolves conflicts by selecting the longest valid chain.
        """
        longest_chain = self.blockchain.chain
        for chain in peer_chains:
            if len(chain) > len(longest_chain) and self.validate_chain(chain):
                longest_chain = chain
        self.blockchain.replace_chain(longest_chain)

    def validate_chain(self, chain):
        """
        Validates an entire blockchain.
        """
        for i in range(1, len(chain)):
            if not self.validate_block(chain[i]):
                return False
        return True
