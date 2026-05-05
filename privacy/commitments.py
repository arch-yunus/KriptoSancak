import random
import hashlib

class PedersenCommitment:
    """
    Pedersen Commitment implementation over a large prime field.
    C = g^m * h^r (mod p)
    """
    def __init__(self, p=None, g=None, h=None):
        # Default parameters (simplified for POC)
        self.p = p or 2**255 - 19
        self.g = g or 2
        self.h = h or 3

    def commit(self, m):
        r = random.randint(1, self.p - 1)
        commitment = (pow(self.g, m, self.p) * pow(self.h, r, self.p)) % self.p
        return commitment, r

    def verify(self, commitment, m, r):
        expected = (pow(self.g, m, self.p) * pow(self.h, r, self.p)) % self.p
        return commitment == expected
