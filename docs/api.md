# KriptoSancak Teknik API Rehberi

Bu döküman, projedeki kriptografik modüllerin teknik yapısını ve kullanım detaylarını özetler.

## 1. Çekirdek Katmanı (Core)

### `CryptoEngine`
Simetrik şifreleme ve anahtar türetme işlemlerinden sorumludur.
- `generate_key(length)`: Verilen uzunlukta rastgele anahtar üretir.
- `derive_key(password, salt)`: Argon2id kullanarak şifreden anahtar türetir.
- `aes_encrypt(key, data)`: AES-256-GCM ile şifreleme yapar.
- `chacha_encrypt(key, data)`: ChaCha20-Poly1305 ile şifreleme yapar.

### `AsymmetricEngine`
Asimetrik kriptografi işlemlerinden sorumludur.
- `generate_ed25519_keys()`: Ed25519 imza anahtar çifti üretir.
- `sign_ed25519(priv, data)`: Veriyi imzalar.
- `verify_ed25519(pub, sig, data)`: İmzayı doğrular.
- `generate_x25519_keys()`: ECDH için anahtar çifti üretir.

### `HashEngine`
Bütünlük ve özetleme işlemlerinden sorumludur.
- `sha3_256(data)`: SHA3-256 özeti üretir.
- `hmac_sha3_256(key, data)`: HMAC-SHA3-256 kimlik doğrulaması sağlar.

---

## 2. Gizlilik ve Gelecek Katmanı (Privacy & Research)

### `PedersenCommitment`
ZKP temelleri için veri taahhüt mekanizması.
- `commit(message)`: Veri için taahhüt ve körleme faktörü üretir.
- `verify(commitment, message, r)`: Taahhüdün geçerliliğini kontrol eder.

### `HomomorphicPOC`
Şifreli veri üzerinde toplama işlemi yapılmasını sağlar.
- `encrypt(m)`: Additive Homomorphic şifreleme yapar.
- `add_encrypted(c1, c2)`: İki şifreli metni toplayarak yeni bir şifreli metin üretir.

### `LWE_POC` (Post-Quantum)
Kafes tabanlı kuantum sonrası şifreleme simülasyonu.
- `encrypt_bit(A, b, bit)`: Bir biti LWE yöntemiyle şifreler.

---
👉 [README'ye Dön](../README.md)
