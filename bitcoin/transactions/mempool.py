# transactions/mempool.py


class Mempool:
    def __init__(self):
        self.transactions = {}

    def add_transaction(self, transaction):
        if transaction.get_hash() not in self.transactions:
            self.transactions[transaction.get_hash()] = transaction
            print(f"Transaction added to mempool: {transaction.get_hash()}")

    def remove_transaction(self, txid):
        if txid in self.transactions:
            del self.transactions[txid]
            print(f"Transaction removed from mempool: {txid}")

    def list_transactions(self):
        return list(self.transactions.values())
