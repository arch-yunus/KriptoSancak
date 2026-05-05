import random
import hashlib

class SchnorrZKP:
    """
    Non-interactive Schnorr Proof of Knowledge of Discrete Log.
    Proves knowledge of x such that y = g^x (mod p).
    """
    def __init__(self, p=None, g=None):
        self.p = p or 2**255 - 19
        self.g = g or 2

    def generate_keypair(self):
        x = random.randint(1, self.p - 1)
        y = pow(self.g, x, self.p)
        return x, y

    def prove(self, x, y):
        # r = random nonce
        r = random.randint(1, self.p - 1)
        t = pow(self.g, r, self.p)
        
        # c = hash(g, y, t)
        h = hashlib.sha256()
        h.update(str(self.g).encode())
        h.update(str(y).encode())
        h.update(str(t).encode())
        c = int(h.hexdigest(), 16) % self.p
        
        # s = r + c*x (mod q) - simplified q = p-1
        s = (r + c * x) % (self.p - 1)
        
        return c, s, t

    def verify(self, y, proof):
        c, s, t = proof
        
        # Verify g^s == t * y^c (mod p)
        lhs = pow(self.g, s, self.p)
        rhs = (t * pow(y, c, self.p)) % self.p
        
        # Also re-calculate c to ensure non-interactivity
        h = hashlib.sha256()
        h.update(str(self.g).encode())
        h.update(str(y).encode())
        h.update(str(t).encode())
        c_expected = int(h.hexdigest(), 16) % self.p
        
        return lhs == rhs and c == c_expected
