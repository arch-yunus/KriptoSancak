# KriptoSancak Teknik API Rehberi

Bu döküman, projedeki kriptografik modüllerin teknik yapısını ve kullanım detaylarını özetler.

## 1. Çekirdek Katmanı (Core)

### `CryptoEngine`
Simetrik şifreleme işlemlerinden sorumludur.
- `generate_key()`: 256-bit rastgele anahtar üretir.
- `aes_encrypt(key, data)`: AES-256-GCM ile şifreleme yapar (Nonce dahildir).
- `chacha_encrypt(key, data)`: ChaCha20-Poly1305 ile şifreleme yapar (Nonce dahildir).

### `AsymmetricEngine`
Asimetrik kriptografi işlemlerinden sorumludur.
- `generate_ed25519_keys()`: Ed25519 imza anahtar çifti üretir.
- `sign_ed25519(priv, data)`: Veriyi imzalar.
- `verify_ed25519(pub, data, sig)`: İmzayı doğrular.
- `generate_x25519_keys()`: ECDH için anahtar çifti üretir.
- `exchange_x25519(priv, peer_pub)`: Paylaşılan sırrı (shared secret) hesaplar.

### `HashEngine`
Bütünlük ve özetleme işlemlerinden sorumludur.
- `sha3_256(data)`: SHA3-256 özeti üretir.
- `sha3_512(data)`: SHA3-512 özeti üretir.
- `hmac_sha3_256(key, data)`: HMAC-SHA3-256 kimlik doğrulaması sağlar.
- `blake2b(data)`: BLAKE2b özeti üretir.

### `SancakVault`
Güvenli veri saklama katmanı.
- `derive_key(password, salt)`: PBKDF2 kullanarak şifreden anahtar türetir.
- `create_secure_container(password, data)`: Veriyi şifreleyip salt ile paketler.
- `unlock_secure_container(password, container)`: Paketi açıp veriyi döner.

---

## 2. Gizlilik ve Gelecek Katmanı (Privacy & Research)

### `PedersenCommitment`
ZKP temelleri için veri taahhüt mekanizması.
- `commit(message)`: Veri için taahhüt ve körleme faktörü (r) üretir.
- `verify(commitment, message, r)`: Taahhüdün geçerliliğini kontrol eder.

### `SchnorrZKP`
Ayrık logaritma bilgisi için sıfır bilgi kanıtı.
- `prove(x, y)`: Gizli x bilgisi için kanıt üretir.
- `verify(y, proof)`: Kanıtı doğrular.

### `LWE_POC` (Post-Quantum)
Kafes tabanlı kuantum sonrası şifreleme simülasyonu.
- `encrypt(public_key, bit)`: Bir biti LWE yöntemiyle şifreler.
- `decrypt(s, ciphertext)`: Şifreli metni çözer.

---
👉 [README'ye Dön](../README.md)
