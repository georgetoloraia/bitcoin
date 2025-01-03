# utils/storage.py

import os
import json


class Storage:
    def __init__(self, data_dir="data"):
        self.data_dir = data_dir
        os.makedirs(data_dir, exist_ok=True)

    def save_block(self, block):
        block_file = os.path.join(self.data_dir, f"block_{block.get_hash()}.json")
        with open(block_file, "w") as f:
            json.dump(block.__dict__, f)
        print(f"Block saved: {block_file}")

    def load_block(self, block_hash):
        block_file = os.path.join(self.data_dir, f"block_{block_hash}.json")
        if os.path.exists(block_file):
            with open(block_file, "r") as f:
                return json.load(f)
        return None
