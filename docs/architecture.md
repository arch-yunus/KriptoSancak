# 🏗️ Mimari Prensipler: Security by Design

KriptoSancak, güvenlik mekanizmalarını sonradan eklenen bir katman olarak değil, sistemin en temel yapı taşı olarak görür.

## 1. Katmanlı Savunma (Defense in Depth)
Proje, veriyi korumak için birden fazla bağımsız güvenlik katmanı kullanır. Bir katmanın aşılması durumunda diğer katmanlar korumayı sürdürür.

## 2. Sabit Zamanlı Operasyonlar (Constant-Time Implementation)
Zamanlama saldırılarını (timing attacks) önlemek için tüm kritik kriptografik işlemler veriden bağımsız olarak aynı sürede tamamlanır. Bellek erişim modelleri ve dallanma tahminleri (branch prediction) bu doğrultuda optimize edilir.

## 3. Yan Kanal Direnci (Side-Channel Resistance)
Sadece matematiksel doğruluk değil, aynı zamanda güç analizi (DPA/SPA) ve elektromanyetik sızıntılara karşı dirençli implementasyonlar hedeflenir.

## 4. Matematiksel İspat ve Doğrulama
Kullanılan her yeni protokol (özellikle ZKP ve PQC alanında), implementasyon öncesinde matematiksel olarak doğrulanır ve mümkünse formal verification yöntemleri uygulanır.

## 5. Minimum Ayrıcalık İlkesi
Kriptografik anahtarlar ve hassas veriler, sadece ihtiyaç duyulan sürede ve ihtiyaç duyulan modüller tarafından erişilebilir kılınır. Bellek güvenliği (Memory Safety) bu süreçte kritik rol oynar.
