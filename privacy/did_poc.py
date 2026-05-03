import json
import hashlib
from core.asymmetric import AsymmetricEngine

class DID_POC:
    """
    Decentralized Identity (DID) Simulation
    Focuses on 'Self-Sovereign Identity' concepts from the README.
    """

    @staticmethod
    def create_did_document(did_name):
        """Generates a simple DID document and its associated keypair"""
        priv, pub = AsymmetricEngine.generate_ed25519_keys()
        pub_hex = AsymmetricEngine.serialize_public_key(pub).hex()
        
        did_id = f"did:ksancak:{did_name}"
        
        doc = {
            "@context": "https://www.w3.org/ns/did/v1",
            "id": did_id,
            "verificationMethod": [{
                "id": f"{did_id}#key-1",
                "type": "Ed25519VerificationKey2018",
                "controller": did_id,
                "publicKeyHex": pub_hex
            }]
        }
        
        return did_id, doc, priv

    @staticmethod
    def sign_verifiable_credential(did_id, private_key, data):
        """Signs a claim to create a Verifiable Credential (VC)"""
        credential = {
            "issuanceDate": "2026-05-03T17:00:00Z",
            "issuer": did_id,
            "credentialSubject": data
        }
        msg = json.dumps(credential, sort_keys=True).encode()
        signature = AsymmetricEngine.sign_ed25519(private_key, msg)
        credential["proof"] = {
            "type": "Ed25519Signature2018",
            "signatureValue": signature.hex()
        }
        return credential

if __name__ == "__main__":
    did_id, doc, priv = DID_POC.create_did_document("yunus")
    print(f"Generated DID: {did_id}")
    print(json.dumps(doc, indent=2))
    
    vc = DID_POC.sign_verifiable_credential(did_id, priv, {"skill": "Cryptology Engineering"})
    print("\nVerifiable Credential:")
    print(json.dumps(vc, indent=2))
