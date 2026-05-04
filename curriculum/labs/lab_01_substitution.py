import string
import collections

class CryptoLab01:
    """
    Lab 01: Klasik Kriptoanaliz ve Frekans Analizi
    Öğrenci Hedefi: Yerine koyma şifrelerini ve kırma yöntemlerini anlamak.
    """

    @staticmethod
    def encrypt_caesar(text, shift):
        result = ""
        for char in text.upper():
            if char in string.ascii_uppercase:
                idx = (string.ascii_uppercase.index(char) + shift) % 26
                result += string.ascii_uppercase[idx]
            else:
                result += char
        return result

    @staticmethod
    def frequency_analysis(ciphertext):
        # Sadece harfleri filtrele
        filtered = [c for c in ciphertext.upper() if c in string.ascii_uppercase]
        counts = collections.Counter(filtered)
        total = len(filtered)
        
        # Yüzdelik dağılım
        freqs = {char: round(count/total * 100, 2) for char, count in counts.items()}
        return sorted(freqs.items(), key=lambda x: x[1], reverse=True)

if __name__ == "__main__":
    print("--- KriptoSancak Lab 01: Frekans Analizi ---")
    message = "KRIPTOLOJI MUHENDISLIGI GELECEGIN GUVENLIK MIMARISIDIR"
    shift = 7
    
    encrypted = CryptoLab01.encrypt_caesar(message, shift)
    print(f"Şifreli Metin: {encrypted}")
    
    analysis = CryptoLab01.frequency_analysis(encrypted)
    print("\nEn Sık Karakterler:")
    for char, pct in analysis[:5]:
        print(f"{char}: %{pct}")
    
    print("\nİpucu: Türkçede en sık kullanılan harfler (A, E, İ, N) ile karşılaştırarak şifreyi çözmeyi deneyin.")
