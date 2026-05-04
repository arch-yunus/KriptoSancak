import numpy as np
import random

class LWE_POC:
    """
    Learning With Errors (LWE) Proof of Concept.
    LWE is the foundation of many lattice-based post-quantum cryptographic schemes.
    
    The security relies on the hardness of finding a secret vector 's' 
    given (A, b) where b = As + e (mod q) and 'e' is a small error vector.
    """

    def __init__(self, n=128, q=2**15, std_dev=2.0):
        self.n = n          # Dimension of the secret vector
        self.q = q          # Modulus
        self.std_dev = std_dev # Standard deviation for noise
        self.m = n * 4      # Number of samples

    def generate_samples(self):
        """Generates the public key (A, b) and secret key s"""
        A = np.random.randint(0, self.q, size=(self.m, self.n))
        s = np.random.randint(0, self.q, size=self.n)
        e = np.round(np.random.normal(0, self.std_dev, size=self.m)).astype(int)
        
        b = (np.dot(A, s) + e) % self.q
        return A, b, s

    def encrypt_bit(self, A, b, bit):
        """Encrypts a single bit using the public key (A, b)"""
        # Select a random subset of samples
        indices = random.sample(range(self.m), self.n)
        
        u = np.sum(A[indices], axis=0) % self.q
        v = (np.sum(b[indices]) + bit * (self.q // 2)) % self.q
        
        return u, v

    def decrypt_bit(self, u, v, s):
        """Decrypts a ciphertext (u, v) using secret key s"""
        # Result = v - u*s (mod q)
        res = (v - np.dot(u, s)) % self.q
        
        # If result is closer to q/2 than 0, it's a 1, else 0
        if res > self.q // 4 and res < 3 * self.q // 4:
            return 1
        return 0

class RLWE_POC:
    """
    Ring-LWE POC. More efficient than standard LWE 
    as it uses polynomial rings instead of matrices.
    """
    def __init__(self, n=256, q=7681):
        self.n = n
        self.q = q
        
    def poly_mul(self, p1, p2):
        """Multiplication in the ring R_q = Z_q[x]/(x^n + 1)"""
        res = np.polymul(p1, p2)
        # Reduction modulo x^n + 1
        # Simplified for POC: just wrap around
        wrapped = np.zeros(self.n)
        for i, val in enumerate(res):
            if (i // self.n) % 2 == 0:
                wrapped[i % self.n] += val
            else:
                wrapped[i % self.n] -= val
        return wrapped % self.q
