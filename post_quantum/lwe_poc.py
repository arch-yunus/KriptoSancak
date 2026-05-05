import numpy as np

class LWE_POC:
    """
    Learning With Errors (LWE) POC.
    A simplified lattice-based encryption demonstration.
    """
    def __init__(self, n=10, q=1024, std_dev=1.0):
        self.n = n
        self.q = q
        self.std_dev = std_dev

    def generate_keys(self):
        # Secret key s
        s = np.random.randint(0, self.q, size=self.n)
        # Public key (A, b) where b = As + e
        A = np.random.randint(0, self.q, size=(2*self.n, self.n))
        e = np.random.normal(0, self.std_dev, size=2*self.n).astype(int)
        b = (A @ s + e) % self.q
        return s, (A, b)

    def encrypt(self, public_key, bit):
        A, b = public_key
        # Small random subset
        m = A.shape[0]
        indices = np.random.choice(m, m // 2, replace=False)
        u = np.sum(A[indices], axis=0) % self.q
        v = np.sum(b[indices]) % self.q
        
        # Add message (bit) scaled to q/2
        v = (v + bit * (self.q // 2)) % self.q
        return u, v

    def decrypt(self, s, ciphertext):
        u, v = ciphertext
        # bit = v - s.u
        res = (v - s @ u) % self.q
        # If res is closer to q/2 than 0, bit is 1
        if res > self.q // 4 and res < 3 * self.q // 4:
            return 1
        return 0
