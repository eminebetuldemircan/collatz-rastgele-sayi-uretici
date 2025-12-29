"""
COLLATZ DENGESİ - RASTGELE SAYI ÜRETİCİ
=======================================
Collatz dizilerinde 0 (çift) ve 1 (tek) adımların
sayısını eşit tutan rastgele sayılar üretir.

Collatz Kuralı:
- Sayı çift: sayı/2
- Sayı tek: 3*sayı+1
- 1 olana kadar tekrarla
"""

import random
import matplotlib.pyplot as plt

# 1. Collatz dizisi hesaplama
def collatz(n):
    """Sayının Collatz dizisini döndürür."""
    dizi = []
    while n != 1:
        dizi.append(n)
        n = n//2 if n%2==0 else 3*n+1
    dizi.append(1)
    return dizi

# 2. Denge hesaplama
def denge_hesapla(dizi):
    """Dizideki çift/tek adımların dengesini hesaplar."""
    cift = sum(1 for x in dizi[:-1] if x%2==0)  # Son eleman hariç
    tek = len(dizi)-1 - cift                    # Toplam adım - çift
    toplam = cift + tek
    return cift, tek, abs(cift-tek)/toplam if toplam>0 else 1

# 3. Dengeli sayı üretme
def dengeli_sayi_uret(adet=50, min_sayi=1, max_sayi=1000, esik=0.7):
    """Dengeli rastgele sayılar üretir."""
    sayilar = []
    denge_oranlari = []
    cift_adimlar = []
    tek_adimlar = []
    
    print(f"Hedef: {adet} sayı | Aralık: [{min_sayi},{max_sayi}] | Eşik: {esik}")
    
    while len(sayilar) < adet:
        # Rastgele sayı üret
        sayi = random.randint(min_sayi, max_sayi)
        
        # Collatz dizisini hesapla
        dizi = collatz(sayi)
        
        # Dengeyi kontrol et
        c, t, d = denge_hesapla(dizi)
        
        # Eşik altındaysa kabul et
        if d <= esik:
            sayilar.append(sayi)
            denge_oranlari.append(d)
            cift_adimlar.append(c)
            tek_adimlar.append(t)
    
    return sayilar, denge_oranlari, cift_adimlar, tek_adimlar

# 4. Basit görselleştirme
def grafik_goster(sayilar, denge_oranlari, cift_adimlar, tek_adimlar):
    """Sonuçları 3 grafikle gösterir."""
    fig, axes = plt.subplots(1, 3, figsize=(15, 4))
    
    # Grafik 1: Sayıların dağılımı
    axes[0].hist(sayilar, bins=20, edgecolor='black', alpha=0.7, color='lightblue')
    axes[0].set_title('Üretilen Sayılar')
    axes[0].set_xlabel('Sayı Değeri')
    axes[0].set_ylabel('Frekans')
    axes[0].grid(True, alpha=0.3)
    
    # Grafik 2: Çift vs Tek adımlar
    axes[1].scatter(cift_adimlar, tek_adimlar, alpha=0.6, color='purple')
    maks = max(max(cift_adimlar), max(tek_adimlar))
    axes[1].plot([0, maks], [0, maks], 'r--', label='İdeal')
    axes[1].set_title('Çift vs Tek Adımlar')
    axes[1].set_xlabel('Çift Adım')
    axes[1].set_ylabel('Tek Adım')
    axes[1].legend()
    axes[1].grid(True, alpha=0.3)
    
    # Grafik 3: Denge dağılımı
    axes[2].hist(denge_oranlari, bins=15, edgecolor='black', alpha=0.7, color='lightgreen')
    axes[2].axvline(x=sum(denge_oranlari)/len(denge_oranlari), color='red', linestyle='--')
    axes[2].set_title('Denge Oranları')
    axes[2].set_xlabel('Denge (0=İyi)')
    axes[2].set_ylabel('Frekans')
    axes[2].grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()

# 5. Ana program
if __name__ == "__main__":
    print("="*50)
    print("COLLATZ DENGELİ SAYI ÜRETECİ")
    print("="*50)
    
    # Parametreler
    ADET = 50          # Üretilecek sayı adedi
    MIN_SAYI = 1       # En küçük sayı
    MAX_SAYI = 1000    # En büyük sayı
    ESIK = 0.7         # Denge eşiği (0-1 arası)
    
    # Sayıları üret
    sayilar, denge_oranlari, cift_adimlar, tek_adimlar = dengeli_sayi_uret(
        adet=ADET,
        min_sayi=MIN_SAYI,
        max_sayi=MAX_SAYI,
        esik=ESIK
    )
    
    # Sonuçları göster
    print(f"\n✓ {len(sayilar)} sayı üretildi")
    print(f"  İlk 5 sayı: {sayilar[:5]}")
    print(f"  Ortalama denge: {sum(denge_oranlari)/len(denge_oranlari):.3f}")
    print(f"  Çift/Tek oranı: {sum(cift_adimlar)/sum(tek_adimlar):.3f}")
    
    # Grafikleri göster
    grafik_goster(sayilar, denge_oranlari, cift_adimlar, tek_adimlar)
