import argparse
import sys
import base64
import json
import os
import io

# Add parent to path for imports
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from core.crypto_engine import CryptoEngine
from core.asymmetric import AsymmetricEngine
from core.hashing import HashEngine
from core.vault import SancakVault
from privacy.commitments import PedersenCommitment
from privacy.zkp_discrete_log import SchnorrZKP

# Dynamic imports for experimental modules
from post_quantum.lwe_poc import LWE_POC
from privacy.did_poc import DID_POC
from core.ael import AutonomousEncryptionLayer

def main():
    parser = argparse.ArgumentParser(description="KriptoSancak Cryptology CLI Tool")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # --- Standard Commands ---
    enc_parser = subparsers.add_parser("encrypt", help="Symmetric Encryption")
    enc_parser.add_argument("-a", "--algo", choices=["aes", "chacha"], default="aes")
    enc_parser.add_argument("-k", "--key", help="Hex encoded key")
    enc_parser.add_argument("-d", "--data", required=True)

    hash_parser = subparsers.add_parser("hash", help="SHA-3 Hashing")
    hash_parser.add_argument("-d", "--data", required=True)
    hash_parser.add_argument("-b", "--bits", choices=["256", "512"], default="256")

    # --- Vault Commands ---
    vault_parser = subparsers.add_parser("vault", help="Sancak Vault Operations")
    vault_parser.add_argument("action", choices=["create", "unlock"])
    vault_parser.add_argument("-p", "--password", required=True)
    vault_parser.add_argument("-d", "--data", help="JSON data for create")
    vault_parser.add_argument("-f", "--file", help="Vault file path")

    # --- Experimental POC Commands ---
    commit_parser = subparsers.add_parser("commit", help="Pedersen Commitment (ZKP POC)")
    commit_parser.add_argument("-m", "--message", type=int, required=True)

    zkp_parser = subparsers.add_parser("zkp", help="Schnorr ZKP Operations")
    zkp_parser.add_argument("action", choices=["prove", "verify"])
    
    bench_parser = subparsers.add_parser("bench", help="Run Performance Benchmarks")

    args = parser.parse_args()

    if args.command == "encrypt":
        key = bytes.fromhex(args.key) if args.key else CryptoEngine.generate_key()
        data = args.data.encode()
        encrypted = CryptoEngine.aes_encrypt(key, data) if args.algo == "aes" else CryptoEngine.chacha_encrypt(key, data)
        print(f"Algorithm: {args.algo.upper()}\nKey (HEX): {key.hex()}\nEncrypted (B64): {base64.b64encode(encrypted).decode()}")

    elif args.command == "hash":
        data = args.data.encode()
        digest = HashEngine.sha3_256(data) if args.bits == "256" else HashEngine.sha3_512(data)
        print(f"SHA3-{args.bits} Hash: {digest.hex()}")

    elif args.command == "vault":
        if args.action == "create":
            secret = json.loads(args.data) if args.data else {"note": "Empty Vault"}
            container = SancakVault.create_secure_container(args.password, secret)
            print(f"Vault created successfully.\nContainer (HEX): {container.hex()}")
        elif args.action == "unlock":
            container = bytes.fromhex(args.data)
            decrypted = SancakVault.unlock_secure_container(args.password, container)
            print(f"Vault unlocked:\n{json.dumps(decrypted, indent=2)}")

    elif args.command == "commit":
        pc = PedersenCommitment()
        commitment, r = pc.commit(args.message)
        print(f"Message: {args.message}\nCommitment: {commitment}\nBlinding Factor (r): {r}")

    elif args.command == "zkp":
        zkp = SchnorrZKP()
        if args.action == "prove":
            x, y = zkp.generate_keypair()
            proof = zkp.prove(x, y)
            print(f"Public Key (y): {y}\nSecret (x): {x}\nProof (c, s, t): {proof}")
        elif args.action == "verify":
            print("Please use the API for verification; parameters required.")

    elif args.command == "bench":
        import benchmarks.crypto_bench as bench
        bench.benchmark_symmetric()
        bench.benchmark_hashing()
        bench.benchmark_asymmetric()

    else:
        parser.print_help()

if __name__ == "__main__":
    main()
