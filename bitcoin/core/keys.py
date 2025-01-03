# core/keys.py

from hashlib import sha256
import os


class CKey:
    def __init__(self):
        self.private_key = None
        self.public_key = None

    def make_new_key(self):
        # Simulate key generation
        self.private_key = os.urandom(32).hex()
        self.public_key = sha256(self.private_key.encode("utf-8")).hexdigest()

    def get_pub_key(self):
        return self.public_key

    def get_priv_key(self):
        return self.private_key
