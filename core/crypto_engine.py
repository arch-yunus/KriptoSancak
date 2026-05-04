import os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM, ChaCha20Poly1305
from cryptography.hazmat.primitives.kdf.argon2 import Argon2id
from cryptography.exceptions import InvalidTag
import io

class CryptoEngine:
    """KriptoSancak Core Cryptographic Engine"""

    @staticmethod
    def generate_key(length=32):
        """Generates a random key of specified length (default 256-bit)"""
        return os.urandom(length)

    @staticmethod
    def derive_key(password: str, salt: bytes, length=32):
        """Derives a key from a password using Argon2id"""
        kdf = Argon2id(
            salt=salt,
            length=length,
            iterations=2,
            memory_cost=65536,
            parallelism=4,
        )
        return kdf.derive(password.encode())

    @staticmethod
    def aes_encrypt(key: bytes, data: bytes, associated_data: bytes = None):
        """AES-256-GCM Encryption"""
        aesgcm = AESGCM(key)
        nonce = os.urandom(12)
        ciphertext = aesgcm.encrypt(nonce, data, associated_data)
        return nonce + ciphertext

    @staticmethod
    def aes_decrypt(key: bytes, encrypted_data: bytes, associated_data: bytes = None):
        """AES-256-GCM Decryption"""
        aesgcm = AESGCM(key)
        nonce = encrypted_data[:12]
        ciphertext = encrypted_data[12:]
        try:
            return aesgcm.decrypt(nonce, ciphertext, associated_data)
        except InvalidTag:
            raise ValueError("Decryption failed: Invalid tag or modified data.")

    @staticmethod
    def chacha_encrypt(key: bytes, data: bytes, associated_data: bytes = None):
        """ChaCha20-Poly1305 Encryption"""
        chacha = ChaCha20Poly1305(key)
        nonce = os.urandom(12)
        ciphertext = chacha.encrypt(nonce, data, associated_data)
        return nonce + ciphertext

    @staticmethod
    def chacha_decrypt(key: bytes, encrypted_data: bytes, associated_data: bytes = None):
        """ChaCha20-Poly1305 Decryption"""
        chacha = ChaCha20Poly1305(key)
        nonce = encrypted_data[:12]
        ciphertext = encrypted_data[12:]
        try:
            return chacha.decrypt(nonce, ciphertext, associated_data)
        except InvalidTag:
            raise ValueError("Decryption failed: Invalid tag or modified data.")

    @staticmethod
    def encrypt_stream(key: bytes, input_stream, output_stream, chunk_size=64*1024):
        """Stream-based encryption (AES-GCM for each chunk)"""
        aesgcm = AESGCM(key)
        while True:
            chunk = input_stream.read(chunk_size)
            if not chunk:
                break
            nonce = os.urandom(12)
            ciphertext = aesgcm.encrypt(nonce, chunk, None)
            # Write chunk size, nonce, and ciphertext
            output_stream.write(len(ciphertext).to_bytes(4, 'big'))
            output_stream.write(nonce)
            output_stream.write(ciphertext)

    @staticmethod
    def decrypt_stream(key: bytes, input_stream, output_stream):
        """Stream-based decryption"""
        aesgcm = AESGCM(key)
        while True:
            size_bytes = input_stream.read(4)
            if not size_bytes:
                break
            size = int.from_bytes(size_bytes, 'big')
            nonce = input_stream.read(12)
            ciphertext = input_stream.read(size)
            try:
                decrypted = aesgcm.decrypt(nonce, ciphertext, None)
                output_stream.write(decrypted)
            except InvalidTag:
                raise ValueError("Stream decryption failed: Invalid tag.")
