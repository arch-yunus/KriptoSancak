# 📙 Seviye 3: Kriptoanaliz ve Saldırı Vektörleri

Güvenli sistemler tasarlamak için algoritmaların nasıl kırıldığını bilmek zorunludur.

## ⚔️ 1. Matematiksel Saldırılar
- **Blok Şifre Analizi:** Diferansiyel ve Lineer Kriptoanaliz yöntemleri.
- **Hash Saldırıları:** Birthday Attack ve Rainbow Tables.
- **Asimetrik Analiz:** Index Calculus, Pollard's Rho, Weiner's Attack (RSA).

## 🕵️ 2. Yan Kanal Saldırıları (Side-Channel Attacks)
Modern sistemlerde zafiyet genellikle matematikte değil, implementasyondadır.

- **Zamanlama (Timing):** Cache-timing saldırıları (Spectre/Meltdown bağlantısı).
- **Güç Analizi:** SPA ve DPA saldırılarına karşı koruma yöntemleri (Masking, Hiding).
- **Hata Enjeksiyonu (Fault Injection):** Bellcore Attack (RSA-CRT zafiyeti).

## 🛡️ 3. Güvenli Implementasyon (Secure Coding)
- **Constant-Time Code:** Karşılaştırma ve matematiksel işlemlerde zamanlama sızıntısını önleme.
- **Güvenli Bellek Yönetimi:** Hassas verilerin bellekten temizlenmesi (Zeroing memory).
- **Side-channel resistance:** Yazılım seviyesinde dirençli kodlama teknikleri.

## 🛠️ Uygulama ve Ödevler
- [ ] **CTF:** Basit bir RSA zafiyetini (Small e) kullanarak mesajı deşifre edin.
- [ ] **Kodlama:** Zamanlama saldırısına açık bir string karşılaştırma fonksiyonu yazın ve bunu saptayan bir script geliştirin.
- [ ] **Araştırma:** Rowhammer saldırısının kriptografik anahtarlar üzerindeki etkisini inceleyin.

## 📖 Önerilen Okumalar
- Richard A. Mollin - *An Introduction to Cryptography*
- Stefan Mangard - *Power Analysis Attacks*

---
[⬅️ Seviye 2](level-2-modern-crypto.md) | [Seviye 4 ➡️](level-4-advanced-topics.md)
