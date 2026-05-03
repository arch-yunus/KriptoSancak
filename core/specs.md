# 🛠️ Kriptografik Spesifikasyonlar

KriptoSancak bünyesinde kullanılan algoritmaların teknik parametreleri ve uyumlu oldukları standartlar aşağıda listelenmiştir.

## 1. Simetrik Şifreleme (Symmetric Encryption)

### AES-GCM (Advanced Encryption Standard - Galois/Counter Mode)
- **Anahtar Uzunluğu:** 256-bit.
- **Standart:** [NIST SP 800-38D](https://csrc.nist.gov/publications/detail/sp/800-38d/final).
- **Nonce Uzunluğu:** 96-bit (Önerilen).
- **Tag Uzunluğu:** 128-bit.

### ChaCha20-Poly1305
- **Standart:** [RFC 8439](https://tools.ietf.org/html/rfc8439).
- **Kullanım:** Düşük donanım kaynaklı sistemlerde yüksek performanslı akış şifreleme.

---

## 2. Asimetrik Şifreleme ve Anahtar Değişimi

### Ed25519 (Edwards-curve Digital Signature Algorithm)
- **Eğri:** Curve25519.
- **Standart:** [RFC 8032](https://tools.ietf.org/html/rfc8032).
- **Güvenlik Seviyesi:** ~128-bit.

### ECDH (Elliptic Curve Diffie-Hellman)
- **Eğriler:** X25519 (Curve25519 tabanlı), NIST P-256.
- **Amaç:** Güvenli olmayan kanallar üzerinden paylaşımlı sır (shared secret) oluşturma.

---

## 3. Özetleme Fonksiyonları (Hashing)

### SHA-3 (Keccak)
- **Varyantlar:** SHA3-256, SHA3-512.
- **Standart:** [FIPS 202](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.202.pdf).

### HMAC (Hash-based Message Authentication Code)
- **Temel:** SHA-256 veya SHA-3.
- **Amaç:** Veri bütünlüğü ve kimlik doğrulama.

---

## 4. Anahtar Türetme (KDF)
- **Argon2id:** Bellek-sert (memory-hard) parola hashleme ve anahtar türetme.
- **PBKDF2:** Geriye dönük uyumluluk için (Legacy).
