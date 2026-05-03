from cryptography.hazmat.primitives.asymmetric import ed25519, x25519
from cryptography.hazmat.primitives import serialization

class AsymmetricEngine:
    """KriptoSancak Asymmetric Cryptography Engine"""

    @staticmethod
    def generate_ed25519_keys():
        """Generates Ed25519 private and public keys"""
        private_key = ed25519.Ed25519PrivateKey.generate()
        public_key = private_key.public_key()
        return private_key, public_key

    @staticmethod
    def sign_ed25519(private_key, data: bytes):
        """Signs data using Ed25519"""
        return private_key.sign(data)

    @staticmethod
    def verify_ed25519(public_key, signature: bytes, data: bytes):
        """Verifies Ed25519 signature"""
        try:
            public_key.verify(signature, data)
            return True
        except Exception:
            return False

    @staticmethod
    def generate_x25519_keys():
        """Generates X25519 keys for ECDH"""
        private_key = x25519.X25519PrivateKey.generate()
        public_key = private_key.public_key()
        return private_key, public_key

    @staticmethod
    def exchange_x25519(private_key, peer_public_key):
        """Performs X25519 Diffie-Hellman exchange"""
        return private_key.exchange(peer_public_key)

    @staticmethod
    def serialize_public_key(public_key):
        """Serializes public key to Raw/PEM format"""
        return public_key.public_bytes(
            encoding=serialization.Encoding.Raw,
            format=serialization.PublicFormat.Raw
        )
