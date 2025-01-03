# network/transaction_pool.py
"""
Maintains a pool of unconfirmed transactions.
"""
import threading


class TransactionPool:
    def __init__(self):
        self.transactions = []
        self.lock = threading.Lock()

    def add_transaction(self, transaction):
        """
        Adds a transaction to the pool.
        """
        with self.lock:
            self.transactions.append(transaction)

    def get_transactions(self):
        """
        Retrieves and clears the pool of transactions.
        """
        with self.lock:
            txs = self.transactions[:]
            self.transactions = []
        return txs

    def prioritize_transactions(self):
        """
        Sorts transactions by fee in descending order.
        """
        with self.lock:
            self.transactions.sort(key=lambda tx: tx["fee"], reverse=True)
