# 🌿 Bitki Hastalığı Teşhis Sistemi

Flutter tabanlı yapay zeka destekli bitki hastalığı teşhis uygulaması.

## 📱 Özellikler

- **%95 Doğruluk Oranı**: Derin öğrenme (CNN) modeli ile yüksek doğrulukta hastalık tespiti
- **23 Hastalık Sınıfı**: 5 farklı bitkide toplam 23 hastalık kategorisi
- **Desteklenen Bitkiler**:
  - 🍎 Elma (Apple)
  - 🌽 Mısır (Corn/Maize)
  - 🌶️ Biber (Pepper)
  - 🥔 Patates (Potato)
  - 🍅 Domates (Tomato)

## 🚀 Kurulum

### Gereksinimler
- Flutter SDK (3.9.2 veya üzeri)
- Dart SDK
- Android Studio / VS Code

### Adımlar

1. **Bağımlılıkları yükleyin**
```bash
flutter pub get
```

2. **Uygulamayı çalıştırın**
```bash
flutter run
```

## 🎨 Uygulama Özellikleri

### Ana Sayfa
- Uygulama ve model hakkında bilgi
- Desteklenen bitkiler
- %95 model doğruluğu göstergesi

### Tespit Sayfası
- Kameradan fotoğraf çekme
- Galeriden fotoğraf seçme
- Yapay zeka analizi

### Sonuç Sayfası
- Hastalık teşhisi
- Güven skoru
- Tedavi önerileri
- İlaçlama tavsiyeleri

## 🤖 Model Bilgileri

- **Model Tipi**: CNN
- **Test Doğruluğu**: %94.99
- **Model Boyutu**: 12.37 MB (TFLite)

## 📸 Kullanım

1. "Teşhise Başla" butonuna tıklayın
2. Fotoğraf çekin veya galeriden seçin
3. "Analiz Et" butonuna basın
4. Sonuçları inceleyin

---

**Not**: Bu uygulama eğitim amaçlıdır. Profesyonel tarımsal kararlar için uzman görüşü alınmalıdır.
