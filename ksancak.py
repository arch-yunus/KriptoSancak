import argparse
import sys
import base64
from core.crypto_engine import CryptoEngine

def main():
    parser = argparse.ArgumentParser(description="KriptoSancak Cryptology CLI Tool")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Encrypt command
    enc_parser = subparsers.add_parser("encrypt", help="Encrypt data")
    enc_parser.add_argument("-a", "--algo", choices=["aes", "chacha"], default="aes", help="Algorithm to use")
    enc_parser.add_argument("-k", "--key", help="Hex encoded key (optional, will generate if missing)")
    enc_parser.add_argument("-d", "--data", required=True, help="Data to encrypt")

    # Decrypt command
    dec_parser = subparsers.add_parser("decrypt", help="Decrypt data")
    dec_parser.add_argument("-a", "--algo", choices=["aes", "chacha"], default="aes", help="Algorithm to use")
    dec_parser.add_argument("-k", "--key", required=True, help="Hex encoded key")
    dec_parser.add_argument("-d", "--data", required=True, help="Base64 encoded encrypted data")

    args = parser.parse_args()

    if args.command == "encrypt":
        key = bytes.fromhex(args.key) if args.key else CryptoEngine.generate_key()
        data = args.data.encode()
        
        if args.algo == "aes":
            encrypted = CryptoEngine.aes_encrypt(key, data)
        else:
            encrypted = CryptoEngine.chacha_encrypt(key, data)
            
        print(f"Algorithm: {args.algo.upper()}")
        print(f"Key (HEX): {key.hex()}")
        print(f"Encrypted (B64): {base64.b64encode(encrypted).decode()}")

    elif args.command == "decrypt":
        key = bytes.fromhex(args.key)
        try:
            encrypted_data = base64.b64decode(args.data)
            if args.algo == "aes":
                decrypted = CryptoEngine.aes_decrypt(key, encrypted_data)
            else:
                decrypted = CryptoEngine.chacha_decrypt(key, encrypted_data)
            print(f"Decrypted Data: {decrypted.decode()}")
        except Exception as e:
            print(f"Error: {e}")

    else:
        parser.print_help()

if __name__ == "__main__":
    main()
