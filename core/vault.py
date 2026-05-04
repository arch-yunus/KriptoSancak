import json
import base64
import os
from core.crypto_engine import CryptoEngine

class SancakVault:
    """Secure Container for sensitive data and metadata"""

    def __init__(self, key: bytes):
        self.key = key

    def seal(self, data: dict) -> bytes:
        """Serializes and encrypts a dictionary into a vault package"""
        raw_json = json.dumps(data).encode()
        encrypted = CryptoEngine.aes_encrypt(self.key, raw_json)
        
        vault_package = {
            "version": "1.0",
            "type": "SancakVault",
            "payload": base64.b64encode(encrypted).decode(),
            "kdf": "Argon2id"
        }
        return json.dumps(vault_package).encode()

    @staticmethod
    def open(vault_data: bytes, key: bytes) -> dict:
        """Decrypts and parses a vault package"""
        package = json.loads(vault_data.decode())
        if package.get("type") != "SancakVault":
            raise ValueError("Invalid vault format")
            
        encrypted_payload = base64.b64decode(package["payload"])
        decrypted_json = CryptoEngine.aes_decrypt(key, encrypted_payload)
        return json.loads(decrypted_json.decode())

    @staticmethod
    def create_secure_container(password: str, secret_data: dict) -> bytes:
        """Helper to create a container from a password"""
        salt = os.urandom(16)
        key = CryptoEngine.derive_key(password, salt)
        vault = SancakVault(key)
        sealed = vault.seal(secret_data)
        
        # Prepend salt for storage
        return salt + sealed

    @staticmethod
    def unlock_secure_container(password: str, container_data: bytes) -> dict:
        """Helper to unlock a container with a password"""
        salt = container_data[:16]
        sealed_data = container_data[16:]
        key = CryptoEngine.derive_key(password, salt)
        return SancakVault.open(sealed_data, key)
