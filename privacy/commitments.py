import hashlib
import os

class PedersenCommitment:
    """
    Pedersen Commitment Scheme (POC)
    Used as a foundational building block for Zero-Knowledge Proofs (ZKP).
    
    Commitment = (g^m * h^r) mod p
    Where:
    - m: The message (data to commit to)
    - r: A random blinding factor
    - g, h: Generators of the group
    - p: A large prime
    """

    # Example parameters (Not for production use, simplified for POC)
    P = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F
    G = 2
    H = 3 # In a real implementation, H should be g^x where x is unknown (nothing-up-my-sleeve)

    @classmethod
    def commit(cls, message: int):
        """Creates a commitment and returns (commitment, blinding_factor)"""
        r = int.from_bytes(os.urandom(32), 'big') % cls.P
        # c = (g^m * h^r) mod p
        commitment = (pow(cls.G, message, cls.P) * pow(cls.H, r, cls.P)) % cls.P
        return commitment, r

    @classmethod
    def verify(cls, commitment: int, message: int, blinding_factor: int):
        """Verifies if the message and blinding factor match the commitment"""
        check = (pow(cls.G, message, cls.P) * pow(cls.H, blinding_factor, cls.P)) % cls.P
        return check == commitment

if __name__ == "__main__":
    # POC Test
    msg = 12345
    print(f"Original Message: {msg}")
    
    comm, r = PedersenCommitment.commit(msg)
    print(f"Commitment: {comm}")
    print(f"Blinding Factor: {r}")
    
    is_valid = PedersenCommitment.verify(comm, msg, r)
    print(f"Verification (Correct Data): {'PASSED' if is_valid else 'FAILED'}")
    
    is_invalid = PedersenCommitment.verify(comm, msg + 1, r)
    print(f"Verification (Modified Data): {'FAILED' if not is_invalid else 'PASSED'}")
