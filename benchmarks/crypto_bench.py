import time
import os
from core.crypto_engine import CryptoEngine
from core.hashing import HashEngine
from core.asymmetric import AsymmetricEngine

def benchmark_symmetric():
    print("--- Symmetric Encryption Benchmarks ---")
    data = os.urandom(10 * 1024 * 1024) # 10MB
    key = CryptoEngine.generate_key()
    
    # AES-GCM
    start = time.time()
    enc = CryptoEngine.aes_encrypt(key, data)
    end = time.time()
    print(f"AES-256-GCM Encryption (10MB): {end - start:.4f}s (~{10/(end-start):.2f} MB/s)")
    
    # ChaCha20
    start = time.time()
    enc = CryptoEngine.chacha_encrypt(key, data)
    end = time.time()
    print(f"ChaCha20-Poly1305 Encryption (10MB): {end - start:.4f}s (~{10/(end-start):.2f} MB/s)")

def benchmark_hashing():
    print("\n--- Hashing Benchmarks ---")
    data = os.urandom(10 * 1024 * 1024) # 10MB
    
    start = time.time()
    HashEngine.sha3_256(data)
    end = time.time()
    print(f"SHA3-256 Hashing (10MB): {end - start:.4f}s (~{10/(end-start):.2f} MB/s)")

def benchmark_asymmetric():
    print("\n--- Asymmetric Benchmarks ---")
    priv, pub = AsymmetricEngine.generate_ed25519_keys()
    data = b"Sancak Signature Test"
    
    count = 1000
    start = time.time()
    for _ in range(count):
        AsymmetricEngine.sign_ed25519(priv, data)
    end = time.time()
    print(f"Ed25519 Signatures ({count} ops): {end - start:.4f}s ({count/(end-start):.2f} op/s)")

if __name__ == "__main__":
    benchmark_symmetric()
    benchmark_hashing()
    benchmark_asymmetric()
