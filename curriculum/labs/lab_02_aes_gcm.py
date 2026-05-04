from core.crypto_engine import CryptoEngine
import os

def aes_lab():
    """
    Lab 02: AES-GCM ve Kimlik Doğrulamalı Şifreleme (AEAD)
    Öğrenci Hedefi: Veri gizliliği ile bütünlüğü arasındaki farkı anlamak.
    """
    print("--- KriptoSancak Lab 02: AES-GCM AEAD ---")
    
    # 1. Anahtar Üretimi
    key = CryptoEngine.generate_key(32) # 256-bit
    data = b"Cok Gizli Veri"
    
    # 2. Şifreleme
    ciphertext = CryptoEngine.aes_encrypt(key, data)
    print(f"Sifreli Veri (HEX): {ciphertext.hex()}")
    
    # 3. Manipülasyon (Saldırı Simülasyonu)
    # Şifreli metnin bir bitini değiştirelim
    modified_ciphertext = bytearray(ciphertext)
    modified_ciphertext[-1] ^= 0x01 # Son biti boz
    
    print("\n[SALDIRI] Sifreli metin yolda modifiye edildi...")
    
    # 4. Deşifre Etme Denemesi
    try:
        decrypted = CryptoEngine.aes_decrypt(key, bytes(modified_ciphertext))
        print(f"Desifre Edilen: {decrypted}")
    except Exception as e:
        print(f"[BASARILI] GCM Integrity Check hatayı yakaladı: {e}")
        print("Sonuç: AEAD sayesinde verinin modifiye edildiği anlaşıldı ve işlem reddedildi.")

if __name__ == "__main__":
    aes_lab()
