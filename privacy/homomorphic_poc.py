import random

class HomomorphicPOC:
    """
    Partially Homomorphic Encryption (PHE) - Additive POC
    Demonstrates computing the sum of encrypted values without decryption.
    
    Simplified Paillier-like mechanism for educational purposes.
    """

    def __init__(self, p=17, q=19):
        # Simplified parameters for POC
        self.n = p * q
        self.g = self.n + 1
        self.lam = (p - 1) * (q - 1)
        self.mu = pow(self.lam, -1, self.n)

    def encrypt(self, m):
        """Encrypts a message m: c = (g^m * r^n) mod n^2"""
        r = random.randint(1, self.n - 1)
        n2 = self.n * self.n
        c = (pow(self.g, m, n2) * pow(r, self.n, n2)) % n2
        return c

    def decrypt(self, c):
        """Decrypts a ciphertext c"""
        n2 = self.n * self.n
        l = (pow(c, self.lam, n2) - 1) // self.n
        m = (l * self.mu) % self.n
        return m

    def add_encrypted(self, c1, c2):
        """Homomorphic addition: c_sum = (c1 * c2) mod n^2"""
        n2 = self.n * self.n
        return (c1 * c2) % n2

if __name__ == "__main__":
    he = HomomorphicPOC()
    
    m1, m2 = 10, 20
    print(f"Original Messages: {m1}, {m2}")
    
    c1 = he.encrypt(m1)
    c2 = he.encrypt(m2)
    print(f"Ciphertexts: {c1}, {c2}")
    
    # Compute sum on encrypted data
    c_sum = he.add_encrypted(c1, c2)
    
    decrypted_sum = he.decrypt(c_sum)
    print(f"Decrypted Sum: {decrypted_sum}")
    print(f"Status: {'SUCCESS' if decrypted_sum == (m1 + m2) else 'FAILED'}")
