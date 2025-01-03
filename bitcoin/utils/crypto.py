# utils/crypto.py

# import hashlib
from hashlib import sha256
from hashlib import new


# Placeholder for KeyPair class
class KeyPair:
    def __init__(self, private_key=None):
        self.private_key = private_key or b"fake_private_key"


def double_sha256(data):
    return sha256(sha256(data.encode("utf-8")).digest()).hexdigest()


def hash160(data):
    sha = sha256(data.encode("utf-8")).digest()
    ripemd160 = new("ripemd160")
    ripemd160.update(sha)
    return ripemd160.hexdigest()
