# 🏗️ Core Module

Bu dizin, KriptoSancak projesinin temel taşlarını oluşturan standart kriptografik algoritmaları ve matematiksel kütüphaneleri içerir.

## 🛠️ İçerik
- **Symmetric:** AES (GCM/CBC), ChaCha20, Poly1305.
- **Asymmetric:** Ed25519, NIST Curves, RSA (Legacy support).
- **Hashing:** SHA-2, SHA-3 (Keccak), BLAKE3.
- **Key Exchange:** ECDH, Argon2 (KDF).

## 🛡️ Güvenlik Prensipleri
Tüm implementasyonlar sabit zamanlı (constant-time) operasyonlar hedeflenerek geliştirilir ve yan kanal saldırılarına karşı optimize edilir.
