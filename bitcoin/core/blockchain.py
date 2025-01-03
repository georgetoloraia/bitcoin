# core/blockchain.py

import time
from hashlib import sha256


class CBlock:
    def __init__(self, prev_hash, merkle_root, transactions, timestamp, bits, nonce):
        self.hashPrevBlock = prev_hash
        self.hashMerkleRoot = merkle_root
        self.vtx = transactions
        self.nTime = timestamp
        self.nBits = bits
        self.nNonce = nonce

    def get_hash(self):
        block_header = f"{self.hashPrevBlock}{self.hashMerkleRoot}{self.nTime}{self.nBits}{self.nNonce}"
        return sha256(block_header.encode("utf-8")).hexdigest()

    def check_block(self):
        if not self.vtx:
            raise ValueError("Block must contain transactions")
        if not self.hashMerkleRoot:
            raise ValueError("Merkle root missing")
        return True


class Blockchain:
    def __init__(self):
        self.chain = []
        self.difficulty_target = "00000fffffffffffffffffffffffffffffffffffffffffffffffffffffffffff"
        self.pending_transactions = []
        self.create_genesis_block()

    def create_merkle_root(self, transactions):
        if not transactions:
            return sha256(b"").hexdigest()
        merkle_tree = [sha256(tx.encode("utf-8")).hexdigest() for tx in transactions]
        while len(merkle_tree) > 1:
            temp_tree = []
            for i in range(0, len(merkle_tree), 2):
                left = merkle_tree[i]
                right = merkle_tree[i + 1] if i + 1 < len(merkle_tree) else left
                temp_tree.append(sha256((left + right).encode("utf-8")).hexdigest())
            merkle_tree = temp_tree
        return merkle_tree[0]

    def create_genesis_block(self):
        prev_hash = "0" * 64
        transactions = ["Genesis Block Transaction"]
        timestamp = 1231006505  # Fixed timestamp for Bitcoin genesis block
        bits = "1d00ffff"
        nonce = 0

        merkle_root = self.create_merkle_root(transactions)
        genesis_block = CBlock(prev_hash, merkle_root, transactions, timestamp, bits, nonce)

        # Simulate mining
        while not genesis_block.get_hash().startswith(self.difficulty_target[:5]):
            genesis_block.nNonce += 1

        self.chain.append(genesis_block)

    def add_transaction(self, transaction):
        self.pending_transactions.append(transaction)

    def mine_block(self):
        if not self.pending_transactions:
            print("No transactions to mine.")
            return

        prev_block = self.chain[-1]
        prev_hash = prev_block.get_hash()
        timestamp = int(time.time())
        bits = self.difficulty_target
        nonce = 0

        merkle_root = self.create_merkle_root(self.pending_transactions)
        new_block = CBlock(prev_hash, merkle_root, self.pending_transactions, timestamp, bits, nonce)

        print("Mining started...")
        start_time = time.time()

        # Mining process
        while not new_block.get_hash().startswith(self.difficulty_target[:5]):
            new_block.nNonce += 1

        self.chain.append(new_block)
        self.pending_transactions = []  # Clear pending transactions
        mining_duration = time.time() - start_time

        print(f"Block mined! Hash: {new_block.get_hash()}")
        print(f"Mining took {mining_duration:.2f} seconds.")

    def validate_chain(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            prev_block = self.chain[i - 1]

            if current_block.hashPrevBlock != prev_block.get_hash():
                return False

            if not current_block.get_hash().startswith(self.difficulty_target[:5]):
                return False

        return True
