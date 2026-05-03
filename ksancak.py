import argparse
import sys
import base64
import json
import os

# Add parent to path for imports
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from core.crypto_engine import CryptoEngine
from core.asymmetric import AsymmetricEngine
from core.hashing import HashEngine
from privacy.commitments import PedersenCommitment

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

    sign_parser = subparsers.add_parser("sign", help="Ed25519 Signing")
    sign_parser.add_argument("-d", "--data", required=True)

    # --- Experimental POC Commands ---
    commit_parser = subparsers.add_parser("commit", help="Pedersen Commitment (ZKP POC)")
    commit_parser.add_argument("-m", "--message", type=int, required=True)

    did_parser = subparsers.add_parser("did", help="Generate DID Document")
    did_parser.add_argument("-n", "--name", required=True)

    ael_parser = subparsers.add_parser("ael", help="Autonomous Encryption Layer simulation")
    ael_parser.add_argument("-t", "--threat", choices=["LOW", "MEDIUM", "HIGH"], default="LOW")
    ael_parser.add_argument("-d", "--data", required=True)

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

    elif args.command == "sign":
        priv, pub = AsymmetricEngine.generate_ed25519_keys()
        sig = AsymmetricEngine.sign_ed25519(priv, args.data.encode())
        print(f"Public Key (HEX): {AsymmetricEngine.serialize_public_key(pub).hex()}\nSignature (HEX): {sig.hex()}")

    elif args.command == "commit":
        comm, r = PedersenCommitment.commit(args.message)
        print(f"Commitment: {comm}\nBlinding Factor (r): {r}")

    elif args.command == "pqc":
        lwe = LWE_POC()
        A, b = lwe.generate_samples()
        u, v = lwe.encrypt_bit(A, b, args.bit)
        print(f"Encrypted Bit: {args.bit}\nVector U: {u.tolist()[:5]}...\nValue V: {v}")

    elif args.command == "did":
        did_id, doc, priv = DID_POC.create_did_document(args.name)
        print(f"DID ID: {did_id}\nDocument:\n{json.dumps(doc, indent=2)}")

    elif args.command == "ael":
        ael = AutonomousEncryptionLayer(args.threat)
        res = ael.protect_data(args.data.encode())
        print(f"Threat Level: {args.threat}\nSelected Algo: {res['meta']['algo'].upper()}\nCiphertext (B64): {base64.b64encode(res['ciphertext']).decode()}")

    else:
        parser.print_help()

if __name__ == "__main__":
    main()
