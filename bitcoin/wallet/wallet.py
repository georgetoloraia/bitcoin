# wallet/wallet.py

import os
import json
from utils.crypto import generate_private_key, private_to_public_key, public_to_address


class Wallet:
    def __init__(self, wallet_file="wallet.json"):
        self.wallet_file = wallet_file
        self.keys = {}
        self.load_wallet()

    def load_wallet(self):
        """
        Loads wallet data from a file.
        """
        if os.path.exists(self.wallet_file):
            with open(self.wallet_file, "r") as f:
                self.keys = json.load(f)

    def save_wallet(self):
        """
        Saves wallet data to a file.
        """
        with open(self.wallet_file, "w") as f:
            json.dump(self.keys, f)

    def generate_new_key(self):
        """
        Generates a new key pair and adds it to the wallet.
        """
        private_key = generate_private_key()
        public_key = private_to_public_key(private_key)
        address = public_to_address(public_key)
        self.keys[address] = {"private_key": private_key, "public_key": public_key}
        self.save_wallet()
        return address

    def get_balance(self, address):
        """
        Placeholder: Fetches balance for a given address.
        """
        # In real-world scenarios, fetch balance from the blockchain.
        print(f"Fetching balance for {address}...")
        return 0.0

    def list_addresses(self):
        """
        Lists all wallet addresses.
        """
        return list(self.keys.keys())
