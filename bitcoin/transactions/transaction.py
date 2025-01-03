# transactions/transaction.py

from utils.crypto import double_sha256


class Transaction:
    def __init__(self, inputs, outputs):
        self.inputs = inputs  # List of dictionaries with "prev_tx" and "output_index"
        self.outputs = outputs  # List of dictionaries with "address" and "value"
        self.txid = self.calculate_hash()

    def calculate_hash(self):
        data = str(self.inputs) + str(self.outputs)
        return double_sha256(data)

    def get_hash(self):
        return self.txid

    def validate(self):
        # Placeholder for input/output validation
        input_total = sum(input["value"] for input in self.inputs)
        output_total = sum(output["value"] for output in self.outputs)
        if input_total >= output_total:
            return True
        return False
