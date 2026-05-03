import time
import sys
import os

# Add core to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from core.crypto_engine import CryptoEngine

def benchmark_algorithm(name, encrypt_func, decrypt_func, data_size_mb=50):
    print(f"\n--- Benchmarking {name} ({data_size_mb} MB) ---")
    data = os.urandom(data_size_mb * 1024 * 1024)
    key = CryptoEngine.generate_key()

    # Encryption
    start_time = time.time()
    encrypted = encrypt_func(key, data)
    end_time = time.time()
    enc_time = end_time - start_time
    print(f"Encryption: {enc_time:.4f}s ({data_size_mb / enc_time:.2f} MB/s)")

    # Decryption
    start_time = time.time()
    decrypted = decrypt_func(key, encrypted)
    end_time = time.time()
    dec_time = end_time - start_time
    print(f"Decryption: {dec_time:.4f}s ({data_size_mb / dec_time:.2f} MB/s)")

    if data == decrypted:
        print("Integrity Check: PASSED")
    else:
        print("Integrity Check: FAILED")

if __name__ == "__main__":
    print("KriptoSancak Performance Analysis Tool")
    print("=" * 40)
    
    benchmark_algorithm("AES-256-GCM", CryptoEngine.aes_encrypt, CryptoEngine.aes_decrypt)
    benchmark_algorithm("ChaCha20-Poly1305", CryptoEngine.chacha_encrypt, CryptoEngine.chacha_decrypt)
