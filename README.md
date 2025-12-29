# Collatz Dengeli Sayı Üreteci

Bu proje, Collatz varsayımına göre diziler üretirken, 0 (çift sayılar) ve 1 (tek sayılar) işlemlerinin sayısını olabildiğince eşit tutan rastgele sayılar üreten bir algoritma içerir.

## 📖 Collatz Varsayımı Nedir?

Collatz varsayımı (Collatz Conjecture), herhangi bir pozitif tam sayı ile başlayarak:
- Sayı çift ise: 2'ye böl
- Sayı tek ise: 3 ile çarp ve 1 ekle

Bu işlem tekrarlanarak her zaman 1 sayısına ulaşılacağını öne süren matematiksel bir varsayımdır.

## 🎯 Projenin Amacı

Bu algoritmanın amacı, Collatz dizilerindeki:
- **0'lar (çift sayı adımları)** ve
- **1'ler (tek sayı adımları)**

sayılarını olabildiğince eşit tutan başlangıç sayılarını bulmaktır.

## 🚀 Özellikler

- **Akıllı Üretim**: Rastgele sayı üretir ve Collatz dengesini kontrol eder
- **Parametrik Esneklik**: Minimum/maksimum sayı aralığı ve denge eşiği ayarlanabilir
- **Görselleştirme**: 6 farklı grafikle sonuç analizi
- **İstatistik Kaydı**: Üretim istatistikleri JSON formatında kaydedilir
- **Kullanıcı Dostu Arayüz**: Komut satırından kolay kullanım

## 📁 Dosya Yapısı
collatz-dengeli-sayi-uretici/
├── collatz_dengeli_uretici.py # Ana program
├── requirements.txt # Gerekli kütüphaneler
├── README.md # Bu dosya
├── LICENSE # MIT Lisansı
└── .gitignore # Git ignore dosyası

## 🔧 Kurulum

1. Python 3.7 veya üzeri yüklü olduğundan emin olun
2. Proje dizininde terminal açın
3. Gerekli kütüphaneleri yükleyin:

```bash
pip install -r requirements.txt
