import time
import sys
import os

# Add core to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from core.crypto_engine import CryptoEngine
from core.asymmetric import AsymmetricEngine
from core.hashing import HashEngine

def benchmark_symmetric(name, encrypt_func, decrypt_func, data_size_mb=50):
    print(f"\n--- Benchmarking {name} ({data_size_mb} MB) ---")
    data = os.urandom(data_size_mb * 1024 * 1024)
    key = CryptoEngine.generate_key()
    start_time = time.time()
    encrypted = encrypt_func(key, data)
    enc_time = time.time() - start_time
    print(f"Encryption: {enc_time:.4f}s ({data_size_mb / enc_time:.2f} MB/s)")

def benchmark_hashing(name, hash_func, data_size_mb=100):
    print(f"\n--- Benchmarking {name} ({data_size_mb} MB) ---")
    data = os.urandom(data_size_mb * 1024 * 1024)
    start_time = time.time()
    hash_func(data)
    h_time = time.time() - start_time
    print(f"Hashing Speed: {h_time:.4f}s ({data_size_mb / h_time:.2f} MB/s)")

def benchmark_asymmetric(name, count=1000):
    print(f"\n--- Benchmarking {name} ({count} operations) ---")
    priv, pub = AsymmetricEngine.generate_ed25519_keys()
    data = b"KriptoSancak Security Benchmark"
    
    # Signing
    start_time = time.time()
    for _ in range(count):
        AsymmetricEngine.sign_ed25519(priv, data)
    s_time = time.time() - start_time
    print(f"Signing Speed: {count / s_time:.2f} op/s")

    # Verification
    sig = AsymmetricEngine.sign_ed25519(priv, data)
    start_time = time.time()
    for _ in range(count):
        AsymmetricEngine.verify_ed25519(pub, sig, data)
    v_time = time.time() - start_time
    print(f"Verification Speed: {count / v_time:.2f} op/s")

if __name__ == "__main__":
    print("KriptoSancak Comprehensive Performance Analysis")
    print("=" * 50)
    
    benchmark_symmetric("AES-256-GCM", CryptoEngine.aes_encrypt, CryptoEngine.aes_decrypt)
    benchmark_hashing("SHA3-256", HashEngine.sha3_256)
    benchmark_asymmetric("Ed25519 Sign/Verify")
