import os
import json
import base64
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from core.crypto_engine import CryptoEngine

class SancakVault:
    @staticmethod
    def derive_key(password, salt=None):
        if salt is None:
            salt = os.urandom(16)
        
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
        )
        key = kdf.derive(password.encode())
        return key, salt

    @staticmethod
    def create_secure_container(password, data):
        """Creates a secure container with encrypted data and salt."""
        key, salt = SancakVault.derive_key(password)
        serialized_data = json.dumps(data).encode()
        encrypted_data = CryptoEngine.aes_encrypt(key, serialized_data)
        
        # Format: SALT (16) + ENCRYPTED_DATA
        return salt + encrypted_data

    @staticmethod
    def unlock_secure_container(password, container):
        """Decrypts a secure container using the password."""
        salt = container[:16]
        encrypted_data = container[16:]
        
        key, _ = SancakVault.derive_key(password, salt)
        decrypted_data = CryptoEngine.aes_decrypt(key, encrypted_data)
        
        return json.loads(decrypted_data.decode())
