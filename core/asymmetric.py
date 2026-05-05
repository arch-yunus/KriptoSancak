from cryptography.hazmat.primitives.asymmetric import ed25519, x25519
from cryptography.hazmat.primitives import serialization

class AsymmetricEngine:
    @staticmethod
    def generate_ed25519_keys():
        private_key = ed25519.Ed25519PrivateKey.generate()
        public_key = private_key.public_key()
        return private_key, public_key

    @staticmethod
    def sign_ed25519(private_key, data):
        return private_key.sign(data)

    @staticmethod
    def verify_ed25519(public_key, data, signature):
        try:
            public_key.verify(signature, data)
            return True
        except Exception:
            return False

    @staticmethod
    def generate_x25519_keys():
        private_key = x25519.X25519PrivateKey.generate()
        public_key = private_key.public_key()
        return private_key, public_key

    @staticmethod
    def exchange_x25519(private_key, peer_public_key):
        return private_key.exchange(peer_public_key)
