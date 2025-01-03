# wallet/transactions.py

from utils.crypto import sign_transaction, verify_signature


class Transaction:
    def __init__(self, sender, recipient, amount, private_key):
        self.sender = sender
        self.recipient = recipient
        self.amount = amount
        self.signature = None
        self.private_key = private_key

    def create_transaction(self):
        """
        Creates a signed transaction.
        """
        transaction_data = f"{self.sender}:{self.recipient}:{self.amount}"
        self.signature = sign_transaction(transaction_data, self.private_key)
        return {
            "sender": self.sender,
            "recipient": self.recipient,
            "amount": self.amount,
            "signature": self.signature,
        }

    @staticmethod
    def verify_transaction(transaction):
        """
        Verifies the authenticity of a transaction.
        """
        transaction_data = f"{transaction['sender']}:{transaction['recipient']}:{transaction['amount']}"
        return verify_signature(
            transaction_data,
            transaction["signature"],
            transaction["sender"],  # Assuming sender holds the public key
        )
