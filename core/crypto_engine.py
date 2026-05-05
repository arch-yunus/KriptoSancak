import os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM, ChaCha20Poly1305

class CryptoEngine:
    @staticmethod
    def generate_key(algo="aes"):
        """Generates a 256-bit key (32 bytes)."""
        return os.urandom(32)

    @staticmethod
    def aes_encrypt(key, data, aad=None):
        """AES-256-GCM encryption."""
        aesgcm = AESGCM(key)
        nonce = os.urandom(12)
        ciphertext = aesgcm.encrypt(nonce, data, aad)
        return nonce + ciphertext

    @staticmethod
    def aes_decrypt(key, data, aad=None):
        """AES-256-GCM decryption."""
        aesgcm = AESGCM(key)
        nonce = data[:12]
        ciphertext = data[12:]
        return aesgcm.decrypt(nonce, ciphertext, aad)

    @staticmethod
    def chacha_encrypt(key, data, aad=None):
        """ChaCha20-Poly1305 encryption."""
        chacha = ChaCha20Poly1305(key)
        nonce = os.urandom(12)
        ciphertext = chacha.encrypt(nonce, data, aad)
        return nonce + ciphertext

    @staticmethod
    def chacha_decrypt(key, data, aad=None):
        """ChaCha20-Poly1305 decryption."""
        chacha = ChaCha20Poly1305(key)
        nonce = data[:12]
        ciphertext = data[12:]
        return chacha.decrypt(nonce, ciphertext, aad)
