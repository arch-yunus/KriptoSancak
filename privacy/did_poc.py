import hashlib
from core.asymmetric import AsymmetricEngine

class DID_POC:
    """
    Decentralized Identity (DID) POC.
    Generates a DID based on a public key.
    """
    @staticmethod
    def create_did(public_key_bytes):
        # did:sancak:<hash(pubkey)>
        pub_hash = hashlib.sha256(public_key_bytes).hexdigest()
        return f"did:sancak:{pub_hash}"

    @staticmethod
    def resolve_did(did_str):
        # Mock resolver
        return {
            "id": did_str,
            "verificationMethod": [{
                "id": f"{did_str}#keys-1",
                "type": "Ed25519VerificationKey2018",
                "controller": did_str
            }]
        }
