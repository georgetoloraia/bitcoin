# db/blockchain_binary.py

import os
import struct
from blockchain.block import Block


class BlockchainBinaryDB:
    def __init__(self, db_file="blockchain.dat"):
        self.db_file = db_file
        self.initialize_db()

    def initialize_db(self):
        if not os.path.exists(self.db_file):
            with open(self.db_file, "wb") as file:
                file.write(b"")  # Create an empty file

    def add_block(self, block: Block):
        with open(self.db_file, "ab") as file:
            serialized_block = block.serialize()
            file.write(struct.pack("I", len(serialized_block)))  # Block size
            file.write(serialized_block)

    def get_block(self, offset):
        with open(self.db_file, "rb") as file:
            file.seek(offset)
            size = struct.unpack("I", file.read(4))[0]
            data = file.read(size)
            return Block.deserialize(data)

    def get_all_blocks(self):
        blocks = []
        offset = 0
        with open(self.db_file, "rb") as file:
            while True:
                try:
                    file.seek(offset)
                    size = struct.unpack("I", file.read(4))[0]
                    data = file.read(size)
                    blocks.append(Block.deserialize(data))
                    offset += 4 + size
                except:
                    break
        return blocks
