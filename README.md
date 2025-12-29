# Multi-Branch Adaptive Collatz Random Number Generator (MBAC-RNG)

Bu proje, klasik **Collatz sanrısını** temel alarak geliştirilmiş,
ancak onu **çok dallı dönüşümler**, **adaptif geri besleme** ve
**hafıza tabanlı kaos mekanizması** ile genişleten
özgün bir rastgele sayı üreteci algoritmasını içermektedir.

Amaç, 0 ve 1 bitlerinin dağılımını mümkün olduğunca dengeli tutarken,
her çalıştırmada farklı ve öngörülemez sonuçlar üretmektir.

---

## 🔍 Collatz Sanrısının Kısa Özeti

Bir pozitif tam sayı için:

- Sayı çift ise → `n / 2`
- Sayı tek ise → `3n + 1`

Bu adımlar tekrarlandığında sayının 1’e ulaştığı varsayılır.
Bu çalışma, bu deterministik yapıyı genişleterek
rastgelelik üretiminde kullanmayı hedefler.

---

## 🧠 Algoritmanın Özgün Yaklaşımı

Bu algoritma, klasik Collatz yaklaşımından şu yönleriyle ayrılır:

### 🔹 1. Çok Dallı Dönüşüm Mekanizması
Tek bir tek-sayı kuralı yerine birden fazla dönüşüm uygulanır:

| Durum | Dönüşüm |
|-----|--------|
| n çift | `n = n / 2` |
| n % 4 == 1 | `n = 3n + 1` |
| n % 4 == 3 | `n = 5n + 1` |

Bu yapı, sayı uzayında daha karmaşık ve öngörülemez bir hareket sağlar.

---

### 🔹 2. Geliştirilmiş Bit Üretim Mantığı

| Durum | Üretilen Bit |
|-----|-------------|
| Çift sayı | 1 |
| n % 4 == 1 | 0 |
| n % 4 == 3 | Rastgele (0 veya 1) |

Bu sayede bit dizisinin entropisi artırılmıştır.

---

### 🔹 3. Adaptif Geri Besleme (Feedback)

Algoritma, üretilen bitleri sürekli analiz eder:

- 0’lar fazla ise → çiftliğe yönlendirme
- 1’ler fazla ise → tekliğe yönlendirme

Bu mekanizma, bit dengesini dinamik olarak korur.

---

### 🔹 4. Hafıza (Memory) Tabanlı Kaos

Eğer ardışık olarak aynı bitlerden oluşan bir desen tespit edilirse,
algoritma kendi durumunu bozarak
yeni bir sayı uzayına geçiş yapar.

Bu özellik, periyodik döngülerin oluşmasını engeller.

---

## 🔐 Rastgelelik ve Güvenlik Açısından Değerlendirme

- Deterministik bir matematiksel yapı içerir
- Rastgele sapmalarla öngörülebilirlik azaltılmıştır
- Geniş anahtar uzayı sayesinde brute-force saldırılara karşı dirençlidir
- Eğitim, simülasyon ve temel kriptografi deneyleri için uygundur


## ▶️ Kullanım

```bash
python mbac_rng.py
