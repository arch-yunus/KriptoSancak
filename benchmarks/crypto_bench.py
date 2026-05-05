import time
import os
from core.crypto_engine import CryptoEngine
from core.hashing import HashEngine
from core.asymmetric import AsymmetricEngine

def benchmark_symmetric():
    print("\n--- Symmetric Encryption Benchmarks ---")
    key = CryptoEngine.generate_key()
    data = os.urandom(1024 * 1024) # 1 MB
    
    start = time.time()
    for _ in range(100):
        CryptoEngine.aes_encrypt(key, data)
    end = time.time()
    print(f"AES-256-GCM (100MB total): {end - start:.4f}s ({100 / (end - start):.2f} MB/s)")

    start = time.time()
    for _ in range(100):
        CryptoEngine.chacha_encrypt(key, data)
    end = time.time()
    print(f"ChaCha20-Poly1305 (100MB total): {end - start:.4f}s ({100 / (end - start):.2f} MB/s)")

def benchmark_hashing():
    print("\n--- Hashing Benchmarks ---")
    data = os.urandom(1024 * 1024) # 1 MB
    
    start = time.time()
    for _ in range(100):
        HashEngine.sha3_256(data)
    end = time.time()
    print(f"SHA3-256 (100MB total): {end - start:.4f}s ({100 / (end - start):.2f} MB/s)")

    start = time.time()
    for _ in range(100):
        HashEngine.blake2b(data)
    end = time.time()
    print(f"BLAKE2b (100MB total): {end - start:.4f}s ({100 / (end - start):.2f} MB/s)")

def benchmark_asymmetric():
    print("\n--- Asymmetric Benchmarks ---")
    priv, pub = AsymmetricEngine.generate_ed25519_keys()
    data = b"Hello, Sancak!"
    
    start = time.time()
    for _ in range(1000):
        sig = AsymmetricEngine.sign_ed25519(priv, data)
    end = time.time()
    print(f"Ed25519 Signing (1000 ops): {end - start:.4f}s ({1000 / (end - start):.2f} ops/s)")

    sig = AsymmetricEngine.sign_ed25519(priv, data)
    start = time.time()
    for _ in range(1000):
        AsymmetricEngine.verify_ed25519(pub, data, sig)
    end = time.time()
    print(f"Ed25519 Verifying (1000 ops): {end - start:.4f}s ({1000 / (end - start):.2f} ops/s)")

if __name__ == "__main__":
    benchmark_symmetric()
    benchmark_hashing()
    benchmark_asymmetric()
