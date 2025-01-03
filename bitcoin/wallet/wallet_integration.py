# wallet/wallet_integration.py

from wallet.wallet import Wallet
from wallet.transactions import Transaction


class WalletIntegration:
    def __init__(self, blockchain):
        self.wallet = Wallet()
        self.blockchain = blockchain

    def send_transaction(self, sender, recipient, amount):
        """
        Creates and broadcasts a transaction to the blockchain.
        """
        private_key = self.wallet.keys[sender]["private_key"]
        transaction = Transaction(sender, recipient, amount, private_key)
        signed_tx = transaction.create_transaction()
        self.blockchain.add_transaction(signed_tx)

        print(f"Transaction sent from {sender} to {recipient} for {amount} coins.")
