import os
from core.crypto_engine import CryptoEngine

class AutonomousEncryptionLayer:
    """
    POC for an autonomous layer that handles key rotation and 
    automated encryption without direct user intervention.
    """
    def __init__(self, master_key=None):
        self.master_key = master_key or CryptoEngine.generate_key()
        self.session_keys = {}

    def get_session_key(self, session_id):
        if session_id not in self.session_keys:
            # In a real scenario, this would be derived from master_key + session_id
            self.session_keys[session_id] = os.urandom(32)
        return self.session_keys[session_id]

    def encrypt_for_session(self, session_id, data):
        key = self.get_session_key(session_id)
        return CryptoEngine.aes_encrypt(key, data)

    def decrypt_for_session(self, session_id, encrypted_data):
        key = self.get_session_key(session_id)
        return CryptoEngine.aes_decrypt(key, encrypted_data)
