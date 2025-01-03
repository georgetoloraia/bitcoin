# utils/merkle.py

from .crypto import double_sha256


def build_merkle_tree(transactions):
    if not transactions:
        return None

    current_level = [tx.get_hash() for tx in transactions]

    while len(current_level) > 1:
        next_level = []
        for i in range(0, len(current_level), 2):
            left = current_level[i]
            right = current_level[i + 1] if i + 1 < len(current_level) else left
            next_level.append(double_sha256(left + right))
        current_level = next_level

    return current_level[0] if current_level else None
