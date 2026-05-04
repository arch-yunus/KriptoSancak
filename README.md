# <p align="center">🎓 KriptoSancak: Kriptoloji Mühendisliği Müfredatı 🎓</p>

<p align="center">
  <img src="assets/banner_v2.png" alt="KriptoSancak Banner" width="100%">
</p>

<p align="center">
  <strong>Bu depo, dijital dünyada veri güvenliğini inşa edecek olan "Kriptoloji Mühendisleri" için hazırlanmış kapsamlı bir eğitim müfredatı, teknik dökümantasyon arşivi ve mühendislik uygulama merkezidir.</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Security-Hardened-red?style=for-the-badge" alt="Security">
  <img src="https://img.shields.io/badge/Tests-Passing-brightgreen?style=for-the-badge" alt="Tests">
  <img src="https://img.shields.io/badge/Field-Cryptography-blue?style=for-the-badge" alt="Field">
  <img src="https://img.shields.io/badge/Whitepaper-Available-gold?style=for-the-badge" alt="Whitepaper">
</p>

---

## 📐 Mühendislik Prensiplerimiz

KriptoSancak, **"Gözlem yoluyla güvenlik"** yerine **"Tasarım yoluyla güvenlik" (Security by Design)** ilkesini benimser.

1.  **Sabit Zamanlı Kodlama (Constant-Time):** Gizli veriye dayalı dallanmalardan ve bellek erişim modellerinden kaçınarak zamanlama saldırılarını (timing attacks) imkansız kılıyoruz.
2.  **Yan Kanal Direnci:** Güç analizi (DPA) ve elektromanyetik sızıntılara karşı algoritmik maskeleme tekniklerini araştırıyoruz.
3.  **Sıfır Güven (Zero-Trust) Mimarisi:** Anahtarların sadece ihtiyaç anında ve izole edilmiş bellek alanlarında (TEE/HSM simülasyonları) var olmasını sağlıyoruz.

---

## 🧬 Teknik Çekirdek ve Spesifikasyonlar

### 1. Simetrik Katman (Symmetric Layer)
*   **AES-256-GCM:** NIST SP 800-38D standardına uygun, kimlik doğrulamalı şifreleme (AEAD). 96-bit nonce ve 128-bit authentication tag ile veri bütünlüğü ve gizliliği eşzamanlı sağlanır.
*   **ChaCha20-Poly1305:** RFC 8439 uyumlu, özellikle donanım hızlandırması olmayan sistemlerde (IoT/Mobil) yüksek performans sunan akış şifreleyici.

### 2. Asimetrik Katman (Asymmetric Layer)
*   **Ed25519 (EdDSA):** RFC 8032 standardında, Curve25519 üzerinde yüksek performanslı ve güvenli dijital imza mekanizması.
*   **X25519 (ECDH):** Eliptik eğri Diffie-Hellman anahtar değişimi ile kuantum öncesi en güvenli anahtar mutabakatı.

### 3. Araştırma ve Gelecek Vizyonu (Research POCs)
*   **ZKP (Pedersen Commitments):** $C = g^m h^r \pmod p$ formülüyle veri gizliliğini koruyan taahhüt mekanizması.
*   **HE (Homomorphic Encryption):** Şifreli metinler üzerinde toplama işlemi yapabilen pedagojik Paillier benzeri implementasyon.
*   **PQC (LWE):** "Learning With Errors" problemi üzerine kurulu, kuantum saldırılarına dirençli kafes tabanlı şifreleme simülasyonu.

---

## 🔍 Araştırma Odağı: Kuantum Sonrası Kriptografi (PQC)

Kuantum bilgisayarlar, mevcut asimetrik algoritmalarımızı (RSA, ECC, Diffie-Hellman) **Shor's Algorithm** kullanarak saniyeler içinde kırabilecektir. KriptoSancak, NIST'in Ağustos 2024'te yayınladığı yeni standartlara odaklanır:

| Kategori | Standart | Algoritma | Durum |
| :--- | :--- | :--- | :--- |
| **KEM (Encryption)** | **FIPS 203** | **ML-KEM (Kyber)** | Finalize Edildi |
| **Signature** | **FIPS 204** | **ML-DSA (Dilithium)** | Finalize Edildi |
| **Signature** | **FIPS 205** | **SLH-DSA (SPHINCS+)** | Finalize Edildi |
| **Alternative Sig** | **FIPS 206** | **FN-DSA (Falcon)** | Geliştirme Aşamasında |

> **⚠️ Q-Day Öngörüsü:** NIST, mevcut kuantum-vulnerable algoritmaların 2030 yılına kadar kullanımdan kaldırılmasını önermektedir.

---

## 🛡️ Güvenlik Matrisi: ZKP SNARK vs STARK

Mahremiyet teknolojilerinde kullanılan iki ana kanıt sisteminin karşılaştırması:

| Özellik | zk-SNARKs | zk-STARKs |
| :--- | :--- | :--- |
| **Trusted Setup** | Gerekli (Genellikle) | Gerekli Değil (Transparent) |
| **Kanıt Boyutu** | Çok Küçük (~288 bytes) | Büyük (~45–150 KB) |
| **Doğrulama Hızı** | Çok Hızlı (Constant) | SNARK'tan Yavaş |
| **Kuantum Direnci** | Hayır (ECC Tabanlı) | **Evet (Hash Tabanlı)** |
| **Güvenlik Temeli** | Eliptik Eğriler (ECC) | Çakışma Dirençli Hashler |

---

## 📉 Tehdit Modellemesi: Kuantum Tehdidi

Kuantum bilgisayarların kriptografik etkileri iki ana koldan gelir:
1.  **Shor's Algorithm:** RSA ve ECC gibi çarpanlara ayırma ve diskret logaritma temelli algoritmaları tamamen etkisiz kılar.
2.  **Grover's Algorithm:** Simetrik şifreleme ve hash fonksiyonlarının güvenliğini karekök oranında azaltır. (Örn: AES-128, 64-bit seviyesine düşer). Bu yüzden KriptoSancak'ta **AES-256** standarttır.

---

## 🎓 Kriptoloji Mühendisliği Müfredatı

KriptoSancak Akademi bünyesinde, teorik matematiği pratik uygulama ile birleştiren 4 seviyeli bir uzmanlaşma yolu sunuyoruz.

### 🗺️ Eğitim Yol Haritası

| Seviye | Odak Noktası | Anahtar Kavramlar |
| :--- | :--- | :--- |
| **📘 Seviye 1** | **Matematiksel Temeller** | Sayılar Teorisi, Modüler Aritmetik, Soyut Cebir, Klasik Şifreler |
| **📗 Seviye 2** | **Modern Standartlar** | AES, RSA, ECC, Hash Fonksiyonları, PKI, TLS/SSL |
| **📙 Seviye 3** | **Kriptoanaliz** | Diferansiyel/Lineer Analiz, Yan Kanal Saldırıları, Güvenli Kodlama |
| **📕 Seviye 4** | **İleri Teknolojiler** | PQC (Kuantum Sonrası), ZKP, Homomorfik Şifreleme, MPC |

👉 **[Müfredatın Tamamını İncele ve Başla](curriculum/README.md)**

---

## 📄 Teknik Dökümantasyon
- 📘 [Teknik Whitepaper](docs/whitepaper.md) - Proje felsefesi ve mimari detaylar.
- ⚙️ [API Referans Rehberi](docs/api.md) - Yazılımcılar için modül kullanım rehberi.
- 📚 [Okuma Listesi](docs/reading_list.md) - Kriptoloji dünyasının temel eserleri.

---

## 🚀 Hızlı Başlangıç

### 1. Kurulum
```bash
git clone https://github.com/arch-yunus/KriptoSancak.git
cd KriptoSancak
pip install -r requirements.txt
```

### 2. CLI Kullanım Örnekleri
```bash
# Simetrik Şifreleme
python ksancak.py encrypt -a aes -d "Gizli Veri"

# Dijital İmza Üretimi
python ksancak.py sign -d "Döküman İçeriği"

# Homomorfik Toplama (HE)
python ksancak.py he -m1 15 -m2 25

# Performance Benchmarking
python ksancak.py bench
```

---

## 📊 Performans Verileri

| Algoritma | İşlem | Kapasite (Hız) |
| :--- | :--- | :--- |
| **AES-256-GCM** | Decryption | **~3200 MB/sn** |
| **ChaCha20** | Encryption | **~1800 MB/sn** |
| **SHA3-256** | Hashing | **~570 MB/sn** |
| **Ed25519** | Signing | **~35,000 op/sn** |

---

## 📂 Proje Mimarisi

```text
KriptoSancak/
├── core/             # Kriptografik çekirdek (AES, EdDSA, Hashing)
├── post_quantum/     # Kuantum sonrası (LWE, Lattice) çalışmaları
├── privacy/          # ZKP, DID ve Homomorfik Şifreleme modülleri
├── benchmarks/       # Hız ve performans analiz araçları
├── tests/            # Unit test suite (unittest)
├── docs/             # Whitepaper, API Docs, Okuma Listesi
└── curriculum/       # 4 Seviyeli Eğitim Müfredatı
```

---

## ❓ Sıkça Sorulan Sorular (SSS)

**S: Bu projeyi üretim ortamında kullanabilir miyim?**  
C: `core` modülleri standartlara uygun olsa da, `post_quantum` ve `privacy` modülleri araştırma amaçlı (POC) seviyesindedir. Üretim öncesi profesyonel denetim önerilir.

**S: Neden Python kullanıldı?**  
C: Müfredat odaklı bir proje olduğu için kodun okunabilirliği önceliğimizdir. Performans gerektiren çekirdek yapılar ileride Rust/C++ ile hibrit hale getirilecektir.

---

## 🤝 Katkıda Bulunma ve Komünite

KriptoSancak bir topluluk sancağıdır. Bu sancağı daha ileriye taşıyabilirsin:
1.  Yeni bir algoritma önerisi veya matematiksel iyileştirme için **Issue** açın.
2.  Geliştirmelerinizi **Feature Branch** üzerinde yapın.
3.  Güvenlik analizleri ve test senaryolarıyla birlikte **Pull Request** gönderin.

---

<p align="center">
  <i>"Gelecek, onu şifreleyenlerin elindedir."</i>
</p>