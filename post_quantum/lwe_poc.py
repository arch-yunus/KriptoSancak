import numpy as np
import os

class LWE_POC:
    """
    Learning With Errors (LWE) - Pedagogical POC
    Foundational problem for Lattice-based Post-Quantum Cryptography.
    
    WARNING: This is a simplified educational implementation.
    """

    def __init__(self, n=10, q=97):
        self.n = n # Dimension
        self.q = q # Modulus
        self.secret_s = np.random.randint(0, self.q, size=self.n)

    def generate_samples(self, m=20):
        """Generates m LWE samples: (a, b = a*s + e) mod q"""
        A = np.random.randint(0, self.q, size=(m, self.n))
        e = np.random.randint(-2, 3, size=m) # Small error
        b = (np.dot(A, self.secret_s) + e) % self.q
        return A, b

    def encrypt_bit(self, A, b, bit):
        """Encrypts a single bit (0 or 1)"""
        m = A.shape[0]
        subset = np.random.choice([0, 1], size=m)
        u = (np.dot(subset, A)) % self.q
        v = (np.dot(subset, b) + bit * (self.q // 2)) % self.q
        return u, v

    def decrypt_bit(self, u, v):
        """Decrypts a single bit using the secret key s"""
        check = (v - np.dot(u, self.secret_s)) % self.q
        return 1 if check > (self.q // 4) and check < (3 * self.q // 4) else 0

if __name__ == "__main__":
    lwe = LWE_POC()
    A, b = lwe.generate_samples()
    
    test_bit = 1
    print(f"Original Bit: {test_bit}")
    
    u, v = lwe.encrypt_bit(A, b, test_bit)
    decrypted = lwe.decrypt_bit(u, v)
    print(f"Decrypted Bit: {decrypted}")
    print(f"Status: {'SUCCESS' if test_bit == decrypted else 'FAILED'}")
