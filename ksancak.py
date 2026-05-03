import argparse
import sys
import base64
from core.crypto_engine import CryptoEngine
from core.asymmetric import AsymmetricEngine
from core.hashing import HashEngine
from privacy.commitments import PedersenCommitment

def main():
    parser = argparse.ArgumentParser(description="KriptoSancak Cryptology CLI Tool")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Symmetric Commands (Already implemented)
    enc_parser = subparsers.add_parser("encrypt", help="Symmetric Encryption")
    enc_parser.add_argument("-a", "--algo", choices=["aes", "chacha"], default="aes")
    enc_parser.add_argument("-k", "--key", help="Hex encoded key")
    enc_parser.add_argument("-d", "--data", required=True)

    # Hashing Commands
    hash_parser = subparsers.add_parser("hash", help="SHA-3 Hashing")
    hash_parser.add_argument("-d", "--data", required=True)
    hash_parser.add_argument("-b", "--bits", choices=["256", "512"], default="256")

    # Asymmetric Commands (Ed25519)
    sign_parser = subparsers.add_parser("sign", help="Ed25519 Signing")
    sign_parser.add_argument("-d", "--data", required=True)

    # ZKP/Privacy POC
    commit_parser = subparsers.add_parser("commit", help="Pedersen Commitment (ZKP POC)")
    commit_parser.add_argument("-m", "--message", type=int, required=True, help="Numeric message to commit")

    args = parser.parse_args()

    if args.command == "encrypt":
        key = bytes.fromhex(args.key) if args.key else CryptoEngine.generate_key()
        data = args.data.encode()
        encrypted = CryptoEngine.aes_encrypt(key, data) if args.algo == "aes" else CryptoEngine.chacha_encrypt(key, data)
        print(f"Key (HEX): {key.hex()}\nEncrypted (B64): {base64.b64encode(encrypted).decode()}")

    elif args.command == "hash":
        data = args.data.encode()
        digest = HashEngine.sha3_256(data) if args.bits == "256" else HashEngine.sha3_512(data)
        print(f"SHA3-{args.bits} Hash: {digest.hex()}")

    elif args.command == "sign":
        priv, pub = AsymmetricEngine.generate_ed25519_keys()
        sig = AsymmetricEngine.sign_ed25519(priv, args.data.encode())
        print(f"Public Key (RAW-HEX): {AsymmetricEngine.serialize_public_key(pub).hex()}")
        print(f"Signature (HEX): {sig.hex()}")

    elif args.command == "commit":
        comm, r = PedersenCommitment.commit(args.message)
        print(f"Commitment: {comm}\nBlinding Factor (r): {r}")

    else:
        parser.print_help()

if __name__ == "__main__":
    main()
