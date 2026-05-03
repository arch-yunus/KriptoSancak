from core.crypto_engine import CryptoEngine

class AutonomousEncryptionLayer:
    """
    Autonomous Encryption Layer (AEL) - POC
    Dynamically selects algorithms based on 'Threat Levels'.
    """

    STRATEGIES = {
        "LOW": {"algo": "aes", "key_len": 32},     # Standard 256-bit AES
        "MEDIUM": {"algo": "chacha", "key_len": 32}, # High performance stream cipher
        "HIGH": {"algo": "aes", "key_len": 32}     # AES with extra padding (hypothetical)
    }

    def __init__(self, threat_level="LOW"):
        self.threat_level = threat_level
        self.config = self.STRATEGIES.get(threat_level, self.STRATEGIES["LOW"])

    def set_threat_level(self, level):
        if level in self.STRATEGIES:
            self.threat_level = level
            self.config = self.STRATEGIES[level]
            print(f"[AEL] Threat level updated to {level}. Strategy: {self.config['algo'].upper()}")

    def protect_data(self, data: bytes):
        """Encrypts data using the current strategy"""
        key = CryptoEngine.generate_key(self.config['key_len'])
        if self.config['algo'] == "aes":
            encrypted = CryptoEngine.aes_encrypt(key, data)
        else:
            encrypted = CryptoEngine.chacha_encrypt(key, data)
        
        return {
            "ciphertext": encrypted,
            "key": key,
            "meta": {"level": self.threat_level, "algo": self.config['algo']}
        }

if __name__ == "__main__":
    ael = AutonomousEncryptionLayer("LOW")
    res = ael.protect_data(b"Normal Traffic")
    print(f"Level LOW: {res['meta']}")
    
    ael.set_threat_level("MEDIUM")
    res = ael.protect_data(b"Critical Traffic")
    print(f"Level MEDIUM: {res['meta']}")
