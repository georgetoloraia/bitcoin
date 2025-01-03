# wallet/wallet_binary.py

import os
import struct
from utils.crypto import KeyPair


class BinaryWallet:
    def __init__(self, wallet_file="wallet.dat"):
        self.wallet_file = wallet_file
        self.keypair = None
        self.load_wallet()

    def load_wallet(self):
        if os.path.exists(self.wallet_file):
            with open(self.wallet_file, "rb") as file:
                private_key_size = struct.unpack("I", file.read(4))[0]
                private_key = file.read(private_key_size)
                self.keypair = KeyPair(private_key=private_key)
        else:
            self.generate_wallet()

    def generate_wallet(self):
        self.keypair = KeyPair()
        self.save_wallet()

    def save_wallet(self):
        with open(self.wallet_file, "wb") as file:
            private_key = self.keypair.private_key
            file.write(struct.pack("I", len(private_key)))  # Private key size
            file.write(private_key)

    def get_balance(self):
        # Placeholder for balance retrieval logic
        return 0
