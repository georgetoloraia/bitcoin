# wallet/address.py

from utils.crypto import hash160, double_sha256


def create_address(public_key):
    """
    Creates a Bitcoin-like address from a public key.
    """
    hashed_key = hash160(public_key)
    checksum = double_sha256(hashed_key)[:8]
    return hashed_key + checksum
