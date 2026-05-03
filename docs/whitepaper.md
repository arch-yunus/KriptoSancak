# KriptoSancak: Tasarım Yoluyla Güvenlik ve Mühendislik Manifestosu

**Sürüm:** 1.0 (Alpha)  
**Yazar:** KriptoSancak Araştırma Grubu  
**Tarih:** Mayıs 2026

## 1. Giriş
KriptoSancak, dijital çağın veri egemenliği ve gizlilik sorunlarına karşı geliştirilmiş, mühendislik disiplini odaklı bir kriptoloji merkezidir. Bu döküman, projenin teknik altyapısını, kullanılan matematiksel modelleri ve gelecek vizyonunu özetler.

## 2. Mimari Prensipler
Proje, **Security by Design** ilkesi üzerine inşa edilmiştir. Bu, güvenliğin bir eklenti değil, sistemin çekirdeği olduğu anlamına gelir.

### 2.1 Sabit Zamanlı Uygulama (Constant-Time Implementation)
Tüm `core` modülleri, zamanlama saldırılarına karşı dirençli olacak şekilde tasarlanmıştır. Dallanma (branching) ve bellek erişim modelleri, gizli veriden bağımsız olarak sabit tutulur.

### 2.2 Kuantum Sonrası Hazırlık (PQC)
Kuantum bilgisayarların Shor algoritması ile RSA ve ECC'yi kırma potansiyeline karşı, KriptoSancak "Kafes Tabanlı" (Lattice-based) yapıları araştırmakta ve test etmektedir.

## 3. Teknik Spesifikasyonlar

### 3.1 Simetrik Katman
AES-256-GCM ve ChaCha20-Poly1305, AEAD (Authenticated Encryption with Associated Data) gereksinimlerini karşılamak üzere seçilmiştir. Bu yapılar hem gizliliği hem de verinin değiştirilmediğini (bütünlük) garanti eder.

### 3.2 Asimetrik Katman
Ed25519 ve X25519 eğrileri, yüksek performans ve güvenli implementasyon kolaylığı nedeniyle tercih edilmiştir. 128-bit güvenlik seviyesi hedeflenmiştir.

### 3.3 Gizlilik ve Sıfır Bilgi Kanıtları (ZKP)
Pedersen Commitment şeması, sistemin mahremiyet temelini oluşturur. 
$C = g^m h^r \pmod p$ formülü ile veriyi ifşa etmeden doğruluğunu ispatlama yeteneği POC olarak sunulmuştur.

## 4. Eğitim Müfredatı
Müfredat, bir kriptoloji mühendisinin ihtiyaç duyacağı teorik derinliği (Sayılar Teorisi, Soyut Cebir) ve pratik yetkinliği (Zamanlama Analizi, Güvenli Kodlama) birleştirir.

## 5. Sonuç
KriptoSancak, bilginin şifrelendiği bir gelecekte, bu şifrelerin anahtarlarını mühendislik disipliniyle korumayı hedefler.

---
> *"Vincit qui se vincit." (Kendini fatih olan, dünyayı fetheder.)*
