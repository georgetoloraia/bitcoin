# core/transaction.py


class CTxIn:
    def __init__(self, prevout_hash, index):
        self.prevout = {"hash": prevout_hash, "index": index}

    def is_coinbase(self):
        # A coinbase transaction has no previous output
        return self.prevout["hash"] == "0" * 64 and self.prevout["index"] == -1


class CTxOut:
    def __init__(self, value, script_pub_key):
        self.nValue = value
        self.scriptPubKey = script_pub_key


class CTransaction:
    def __init__(self):
        self.vin = []  # List of inputs
        self.vout = []  # List of outputs

    def add_input(self, tx_in):
        self.vin.append(tx_in)

    def add_output(self, tx_out):
        self.vout.append(tx_out)

    def is_coinbase(self):
        # Check if this transaction is a coinbase transaction
        return len(self.vin) == 1 and self.vin[0].is_coinbase()

    def get_value_out(self):
        return sum(tx_out.nValue for tx_out in self.vout)


class CMerkleTx(CTransaction):
    def __init__(self):
        super().__init__()
        self.hashBlock = None
        self.vMerkleBranch = []

    def set_merkle_branch(self):
        # Placeholder for setting the merkle branch
        pass
