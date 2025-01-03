# core/wallet.py

from .keys import CKey
from .transaction import CTransaction


class Wallet:
    def __init__(self):
        self.mapWallet = {}  # A dictionary mapping transaction IDs to transactions
        self.keys = {}

    def add_key(self, key):
        pub_key = key.get_pub_key()
        priv_key = key.get_priv_key()
        self.keys[pub_key] = priv_key

    def add_to_wallet(self, tx):
        tx_id = tx.get_hash()
        self.mapWallet[tx_id] = tx

    def generate_new_key(self):
        key = CKey()
        key.make_new_key()
        self.add_key(key)
        return key.get_pub_key()

    def get_balance(self):
        balance = 0
        for tx_id, tx in self.mapWallet.items():
            for tx_out in tx.vout:
                balance += tx_out.nValue
        return balance
