# wallet/secure_storage.py

import os
from cryptography.fernet import Fernet


class SecureStorage:
    def __init__(self, storage_file="secure_wallet.dat", key_file="wallet.key"):
        self.storage_file = storage_file
        self.key_file = key_file
        self.key = self.load_encryption_key()

    def load_encryption_key(self):
        """
        Loads or generates an encryption key.
        """
        if os.path.exists(self.key_file):
            with open(self.key_file, "rb") as f:
                return f.read()
        else:
            key = Fernet.generate_key()
            with open(self.key_file, "wb") as f:
                f.write(key)
            return key

    def save_secure_data(self, data):
        """
        Encrypts and saves wallet data.
        """
        cipher = Fernet(self.key)
        encrypted_data = cipher.encrypt(data.encode())
        with open(self.storage_file, "wb") as f:
            f.write(encrypted_data)

    def load_secure_data(self):
        """
        Decrypts and loads wallet data.
        """
        cipher = Fernet(self.key)
        with open(self.storage_file, "rb") as f:
            encrypted_data = f.read()
        return cipher.decrypt(encrypted_data).decode()
