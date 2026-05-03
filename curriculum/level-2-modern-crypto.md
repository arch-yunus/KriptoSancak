# 📘 Seviye 2: Modern Kriptografi ve Standartlar

Günümüz dijital dünyasını ayakta tutan algoritma ve protokollerin mühendislik perspektifiyle incelenmesi.

## 🔐 1. Simetrik Kriptografi (Symmetric Cryptography)
- **Blok Şifreler (Block Ciphers):**
    - **AES (Advanced Encryption Standard):** SPN yapısı, AddRoundKey, SubBytes, ShiftRows, MixColumns aşamaları.
    - **Modlar:** ECB, CBC, CTR ve **AEAD** (GCM, Poly1305) modlarının güvenlik farkları.
- **Akış Şifreler (Stream Ciphers):**
    - ChaCha20 mimarisi ve Nonce yönetimi.
- **Hash Fonksiyonları:**
    - SHA-2 vs SHA-3 mimarisi.
    - **MAC ve HMAC:** Veri bütünlüğü ve kimlik doğrulama.

## 🔑 2. Asimetrik Kriptografi (Asymmetric Cryptography)
- **Temel Protokoller:**
    - Diffie-Hellman Anahtar Değişimi ve MITM saldırıları.
    - RSA: OAEP padding önemi ve PKCS#1 v1.5 zafiyetleri.
- **Eliptik Eğri Kriptografisi (ECC):**
    - Weierstrass vs Edwards eğrileri.
    - Ed25519 ve NIST P-256 standartları.
- **Altyapı:**
    - **PKI & TLS:** Sertifika otoriteleri (CA), Revocation (CRL, OCSP) ve TLS 1.3 el sıkışması.

## 🛠️ Uygulama ve Ödevler
- [ ] **Kodlama:** AES-GCM kullanarak güvenli bir dosya şifreleme aracı geliştirin.
- [ ] **Protokol:** RSA ile basit bir mesaj imzalama ve doğrulama akışı kurun.
- [ ] **Analiz:** Wireshark ile bir TLS el sıkışmasını (Handshake) paket bazında inceleyin.

## 📖 Önerilen Okumalar
- Niels Ferguson, Bruce Schneier - *Cryptography Engineering*
- Dan Boneh, Victor Shoup - *A Graduate Course in Applied Cryptography*

---
[⬅️ Seviye 1](level-1-foundations.md) | [Seviye 3 ➡️](level-3-cryptanalysis.md)
