import unittest
import sys
import os

# Add core and privacy to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from core.crypto_engine import CryptoEngine
from core.asymmetric import AsymmetricEngine
from core.hashing import HashEngine
from privacy.commitments import PedersenCommitment

class TestKriptoSancak(unittest.TestCase):

    def test_aes_gcm(self):
        key = CryptoEngine.generate_key()
        data = b"Sensitive Data"
        encrypted = CryptoEngine.aes_encrypt(key, data)
        decrypted = CryptoEngine.aes_decrypt(key, encrypted)
        self.assertEqual(data, decrypted)

    def test_chacha20(self):
        key = CryptoEngine.generate_key()
        data = b"Stream Data"
        encrypted = CryptoEngine.chacha_encrypt(key, data)
        decrypted = CryptoEngine.chacha_decrypt(key, encrypted)
        self.assertEqual(data, decrypted)

    def test_sha3(self):
        data = b"Hash Me"
        h1 = HashEngine.sha3_256(data)
        h2 = HashEngine.sha3_256(data)
        self.assertEqual(h1, h2)
        self.assertEqual(len(h1), 32)

    def test_ed25519(self):
        priv, pub = AsymmetricEngine.generate_ed25519_keys()
        data = b"Sign Me"
        sig = AsymmetricEngine.sign_ed25519(priv, data)
        self.assertTrue(AsymmetricEngine.verify_ed25519(pub, sig, data))

    def test_pedersen_commitment(self):
        msg = 42
        comm, r = PedersenCommitment.commit(msg)
        self.assertTrue(PedersenCommitment.verify(comm, msg, r))
        self.assertFalse(PedersenCommitment.verify(comm, msg + 1, r))

if __name__ == '__main__':
    unittest.main()
