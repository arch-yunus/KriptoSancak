import hmac
import hashlib
from cryptography.hazmat.primitives import hashes, hmac as crypto_hmac

class HashEngine:
    """KriptoSancak Hashing and Integrity Engine"""

    @staticmethod
    def sha3_256(data: bytes):
        """SHA3-256 Hashing"""
        digest = hashes.Hash(hashes.SHA3_256())
        digest.update(data)
        return digest.finalize()

    @staticmethod
    def sha3_512(data: bytes):
        """SHA3-512 Hashing"""
        digest = hashes.Hash(hashes.SHA3_512())
        digest.update(data)
        return digest.finalize()

    @staticmethod
    def hmac_sha256(key: bytes, data: bytes):
        """HMAC-SHA256 Implementation"""
        h = crypto_hmac.HMAC(key, hashes.SHA256())
        h.update(data)
        return h.finalize()

    @staticmethod
    def hmac_sha3_256(key: bytes, data: bytes):
        """HMAC-SHA3-256 Implementation"""
        h = crypto_hmac.HMAC(key, hashes.SHA3_256())
        h.update(data)
        return h.finalize()
