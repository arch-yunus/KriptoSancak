from cryptography.hazmat.primitives import hashes

class HashEngine:
    @staticmethod
    def sha3_256(data):
        digest = hashes.Hash(hashes.SHA3_256())
        digest.update(data)
        return digest.finalize()

    @staticmethod
    def sha3_512(data):
        digest = hashes.Hash(hashes.SHA3_512())
        digest.update(data)
        return digest.finalize()

    @staticmethod
    def hmac_sha3_256(key, data):
        from cryptography.hazmat.primitives import hmac
        h = hmac.HMAC(key, hashes.SHA3_256())
        h.update(data)
        return h.finalize()

    @staticmethod
    def blake2b(data):
        digest = hashes.Hash(hashes.BLAKE2b(64))
        digest.update(data)
        return digest.finalize()
