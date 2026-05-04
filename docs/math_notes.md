# 📐 Kriptoloji Mühendisliği: Matematiksel Notlar

Bu döküman, projemizde kullanılan ileri düzey algoritmaların matematiksel temellerini derinlemesine açıklar.

## 1. Eliptik Eğri Matematiği (ECC)
Eliptik eğriler, $y^2 = x^3 + ax + b$ formülüne dayanan geometrik yapılardır.

### Skaler Çarpım ve Zorluk
ECC'nin güvenliği, **Eliptik Eğri Diskret Logaritma Problemi (ECDLP)** üzerine kuruludur.
- Bir $P$ noktası ve bir $k$ skaleri için $Q = kP$ işlemini yapmak kolaydır (Double-and-Add algoritması).
- Ancak $Q$ ve $P$ verildiğinde $k$ değerini bulmak, klasik bilgisayarlar için üstel zaman alır.

### Curve25519 (X25519)
Montgomery eğrisi formundadır: $y^2 = x^3 + 486662x^2 + x$. Side-channel saldırılarına karşı doğal direnci ve yüksek hızıyla bilinir.

---

## 2. Kafes Tabanlı Kriptografi ve LWE
Kuantum sonrası güvenliğin temelidir.

### Learning With Errors (LWE) Problemi
$n$ boyutlu bir $s$ gizli vektörü, bir $A$ matrisi ve bir $e$ hata vektörü (gürültü) için:
$$b = As + e \pmod q$$
- $(A, b)$ verildiğinde $s$'yi bulmak, hata vektörü $e$ nedeniyle "En Yakın Vektör Problemi"ne (CVP) dönüşür ve bu işlem çok zordur.
- **Kuantum Direnci:** Kuantum bilgisayarlar, kafes tabanlı bu problemleri çözmekte klasik bilgisayarlardan çok daha hızlı değildir.

### Regev'in Şifreleme Şeması
LWE probleminin doğrudan bir şifreleme uygulamasıdır. `post_quantum/lwe_poc.py` içinde bu mantığın basitleştirilmiş bir simülasyonu yer almaktadır.

---
👉 [README'ye Dön](../README.md)
