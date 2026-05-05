import pytest
import os
from core.crypto_engine import CryptoEngine
from core.hashing import HashEngine
from core.asymmetric import AsymmetricEngine
from core.vault import SancakVault
from privacy.commitments import PedersenCommitment
from privacy.zkp_discrete_log import SchnorrZKP
from post_quantum.lwe_poc import LWE_POC

def test_aes_gcm():
    key = CryptoEngine.generate_key()
    data = b"Sensitive Data"
    encrypted = CryptoEngine.aes_encrypt(key, data)
    decrypted = CryptoEngine.aes_decrypt(key, encrypted)
    assert decrypted == data

def test_chacha20():
    key = CryptoEngine.generate_key()
    data = b"Sensitive Data"
    encrypted = CryptoEngine.chacha_encrypt(key, data)
    decrypted = CryptoEngine.chacha_decrypt(key, encrypted)
    assert decrypted == data

def test_sha3():
    data = b"Hello"
    h256 = HashEngine.sha3_256(data)
    assert len(h256) == 32
    h512 = HashEngine.sha3_512(data)
    assert len(h512) == 64

def test_ed25519():
    priv, pub = AsymmetricEngine.generate_ed25519_keys()
    data = b"Sign this"
    sig = AsymmetricEngine.sign_ed25519(priv, data)
    assert AsymmetricEngine.verify_ed25519(pub, data, sig) is True

def test_vault():
    password = "SuperSecretPassword"
    data = {"secret": "data"}
    container = SancakVault.create_secure_container(password, data)
    unlocked = SancakVault.unlock_secure_container(password, container)
    assert unlocked == data

def test_pedersen():
    pc = PedersenCommitment()
    m = 123
    commitment, r = pc.commit(m)
    assert pc.verify(commitment, m, r) is True
    assert pc.verify(commitment, m + 1, r) is False

def test_schnorr():
    zkp = SchnorrZKP()
    x, y = zkp.generate_keypair()
    proof = zkp.prove(x, y)
    assert zkp.verify(y, proof) is True

def test_lwe():
    lwe = LWE_POC(n=10, q=1024)
    s, pk = lwe.generate_keys()
    
    # Test 0
    c0 = lwe.encrypt(pk, 0)
    assert lwe.decrypt(s, c0) == 0
    
    # Test 1
    c1 = lwe.encrypt(pk, 1)
    assert lwe.decrypt(s, c1) == 1
