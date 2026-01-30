# 🫀 Kalp Hastalığı Tahmin Discord Botu

Bu proje, makine öğrenmesi kullanarak bir bireyin kalp hastalığı riski olup olmadığını tahmin eden
bir **Discord botudur**.

---

## 🚀 Özellikler

- 🤖 Random Forest tabanlı makine öğrenmesi modeli
- 📊 Tahmin güven oranı (%)
- 🧠 Tahmin açıklaması (en etkili faktörler)
- ✅ Giriş doğrulama ve hata kontrolü
- 💬 Discord üzerinden kolay kullanım

---

## 🧪 Kullanılan Veri Seti

- **Heart Disease Dataset**
- 300+ hasta verisi
- 11 özellik + 1 hedef değişken

Örnek özellikler:
- Yaş
- Cinsiyet
- Göğüs ağrısı tipi
- Kolesterol
- Maksimum kalp atış hızı

---

## 🛠 Kullanılan Teknolojiler

- Python
- discord.py
- scikit-learn
- pandas

---

## ▶️ Komut Kullanımı

```text
!kalp <age> <sex> <cp> <bp> <chol> <fbs> <ecg> <maxhr> <angina> <oldpeak> <slope>
