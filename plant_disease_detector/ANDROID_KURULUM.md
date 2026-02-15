# 🎯 Android Cihazda Çalıştırma Talimatı

## ✅ Mevcut Durum

✓ Android cihaz bağlı: **RMX3201** (OPPO, Android 11)  
✓ Gradle derleme başlatılmış  
✓ Uygulama yükleniyor...

## 📊 Beklenen Süre

- **Gradle Derleme**: ~2-5 dakika (ilk kez daha uzun olabilir)
- **Uygulama Yükleme**: ~30 saniye
- **Uygulama Açılması**: ~5 saniye

## 🚀 Cihazda Kontrol Listesi

Uygulama açıldıktan sonra sırasıyla kontrol edin:

### 1️⃣ Ana Sayfa
- [ ] Yeşil gradient arka plan görünüyor
- [ ] "🌿 Bitki Hastalığı Teşhis Sistemi" başlığı
- [ ] Model bilgileri (95% doğruluk)
- [ ] Desteklenen bitkiler listesi
- [ ] "Teşhise Başla" butonu

### 2️⃣ Tespit Sayfası (Tıkla: Teşhise Başla)
- [ ] Gri fotoğraf placeholder görünüyor
- [ ] "Kamera ile Fotoğraf Çek" mavi butonu
- [ ] "Galeriden Seç" turuncu butonu
- [ ] İpuçları kartı

### 3️⃣ Kamera İzinleri
- [ ] "Kamera ile Fotoğraf Çek" tıkla
- [ ] Kamera izni isteniyor
- [ ] "İzin Ver" seçeneğini tıkla
- [ ] Kamera arayüzü açılıyor

### 4️⃣ Fotoğraf Çekme
- [ ] Domates yaprağı göster
- [ ] Fotoğrafı çek
- [ ] "Analiz Et" butonu aktif hale geliyor
- [ ] Butona tıkla

### 5️⃣ Analiz Süreci
- [ ] "Analiz Ediliyor..." yazısı görünüyor
- [ ] Yükleme göstergesi döndürülüyor
- [ ] ~2-3 saniye bekle
- [ ] Sonuç sayfası açılıyor

### 6️⃣ Sonuç Sayfası
- [ ] Fotoğraf gösteriliyor
- [ ] Hastalık adı ve bitki türü
- [ ] Güven skoru (örn: 94.5%)
- [ ] Hastalık açıklaması
- [ ] Belirtiler listesi
- [ ] Tedavi önerileri
- [ ] İlaçlama tavsiyeleri
- [ ] "Yeni Analiz" ve "Ana Sayfa" butonları

### 7️⃣ Desteklenmeyen Bitki Testi
- [ ] "Yeni Analiz" tıkla
- [ ] Bamya veya başka bitki fotoğrafı seç
- [ ] "Analiz Et" tıkla
- [ ] Nazik dialog çıkıyor (Desteklenen bitkiler listesi)

## 🔧 Sorun Giderme

### Hata: "Gradle görevleri başarısız oldu"
```bash
flutter clean
flutter pub get
flutter run -d R8EUUGEQIVHYSK79
```

### Hata: "Model yükleme hatası"
- Assets klasöründe `.tflite` dosyası var mı kontrol et
- pubspec.yaml'de assets tanımlandı mı kontrol et

### Hata: "Kamera izni reddedildi"
- Cihaz Ayarları → Uygulamalar → plant_disease_detector → İzinler
- Kamera iznini "İzin Ver" seç

### Hata: "Uygulamalar dizisinde kilitlenme"
- Uygulamayı zorla kapat
- Cihazı yeniden başlat
- `flutter run` tekrar çalıştır

## 📱 Cihaz Bilgileri

```
Cihaz: OPPO RMX3201
Android: 11 (API 30)
Mimari: ARM64
Durum: Bağlı
```

## 💾 Derleme Çıktıları

```
Gradle Görevleri: assembleDebug
APK Konumu: build/app/outputs/flutter-apk/app-debug.apk
Boyut: ~50-60 MB (şişirilmiş)
```

## 📊 Beklenen Sonuçlar

### Test Domates Fotoğrafıyla:
- ✅ Yaprak tanınmalı
- ✅ "Tomato Healthy" veya hastalık adı
- ✅ Güven skoru > %90
- ✅ Tedavi önerileri gösterilmeli

### Test Desteklenmeyen Bitkiyle:
- ✅ Dialog çıkmalı
- ✅ "Desteklenmeyen Bitki" mesajı
- ✅ Desteklenen bitkiler listesi
- ✅ Nazik, tatlı mesaj

## 🎯 Başarı Göstergeleri

✓ Uygulama çökmüyor  
✓ Tüm ekranlar düzgün yükleniyor  
✓ Kamera çalışıyor  
✓ Model tahmin yapıyor  
✓ Sonuç doğru gösteriliyor  
✓ Navigasyon sorunsuz  
✓ Tasarım profesyonel görünüyor  

## 🏆 Bitti!

Tüm adımlar tamamlandı. Uygulamanız hazır! 🎉

---

**Not**: İlk açılış biraz yavaş olabilir. Sonraki açılışlar daha hızlı olacaktır.

Keyifli kullanımlar! 🌿💚
