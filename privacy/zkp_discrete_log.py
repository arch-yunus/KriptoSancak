import hashlib
import os
import random

class SchnorrZKP:
    """
    Schnorr Non-Interactive Zero-Knowledge Proof.
    Proves knowledge of 'x' such that y = g^x mod p without revealing x.
    """

    def __init__(self, p=None, g=None):
        # Using a small prime for POC, in production use NIST or 2048-bit primes
        self.p = p or 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFFFFFFFFFFFF
        self.g = g or 2

    def generate_keypair(self):
        """Generates secret x and public y"""
        x = random.randint(1, self.p - 1)
        y = pow(self.g, x, self.p)
        return x, y

    def prove(self, x, y):
        """Generates a proof (c, s)"""
        # 1. Commitment: pick random k, compute r = g^k mod p
        k = random.randint(1, self.p - 1)
        r = pow(self.g, k, self.p)

        # 2. Challenge: c = H(g, y, r)
        c_hash = hashlib.sha256(f"{self.g}{y}{r}".encode()).hexdigest()
        c = int(c_hash, 16) % self.p

        # 3. Response: s = k + c*x mod (p-1)
        s = (k + c * x) % (self.p - 1)

        return (c, s, r)

    def verify(self, y, proof):
        """Verifies the proof (c, s, r)"""
        c, s, r = proof
        
        # Check if g^s == r * y^c mod p
        lhs = pow(self.g, s, self.p)
        rhs = (r * pow(y, c, self.p)) % self.p
        
        # Also recompute c to ensure it's not a chosen challenge
        c_verify_hash = hashlib.sha256(f"{self.g}{y}{r}".encode()).hexdigest()
        c_verify = int(c_verify_hash, 16) % self.p
        
        return lhs == rhs and c == c_verify

if __name__ == "__main__":
    zkp = SchnorrZKP()
    x, y = zkp.generate_keypair()
    print(f"Secret x: [HIDDEN], Public y: {y}")
    
    proof = zkp.prove(x, y)
    print(f"Proof generated: c={proof[0]}, s={proof[1]}")
    
    is_valid = zkp.verify(y, proof)
    print(f"Is proof valid? {is_valid}")
