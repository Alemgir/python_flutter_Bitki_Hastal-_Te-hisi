# 🚀 Uygulamayı Çalıştırma Rehberi

## Hızlı Başlangıç

### 1. Proje Klasörüne Gidin
```bash
cd d:\Users\alamg\Desktop\aaa\plant_disease_detector
```

### 2. Bağımlılıkları Kontrol Edin
```bash
flutter pub get
```

### 3. Bağlı Cihazları Görün
```bash
flutter devices
```

### 4. Uygulamayı Çalıştırın

#### Android Emülatör/Cihaz
```bash
flutter run
```

#### Belirli bir cihazı seçmek için:
```bash
flutter run -d <device-id>
```

#### Chrome (Web) için:
```bash
flutter run -d chrome
```

#### Windows için:
```bash
flutter run -d windows
```

## 📱 Test Senaryoları

### Senaryo 1: Sağlıklı Yaprak Tespiti
1. Uygulamayı açın
2. "Teşhise Başla" butonuna tıklayın
3. Sağlıklı bir domates yaprağı fotoğrafı seçin
4. "Analiz Et" butonuna basın
5. ✅ Sonuç: "Tomato Healthy" - Bakım önerileri gösterilmeli

### Senaryo 2: Hastalıklı Yaprak Tespiti
1. Hastalıklı bir yaprak fotoğrafı seçin (örn: domates erken yanıklığı)
2. "Analiz Et" butonuna basın
3. ✅ Sonuç: Hastalık adı, belirtiler, tedavi ve ilaç önerileri

### Senaryo 3: Desteklenmeyen Bitki
1. Bamya, salatalık veya başka bir bitki fotoğrafı seçin
2. "Analiz Et" butonuna basın
3. ✅ Sonuç: Nazik uyarı dialog'u - Desteklenen bitkilerin listesi

### Senaryo 4: Kamera Kullanımı
1. "Kamera" butonuna tıklayın
2. İzinleri kabul edin
3. Yaprak fotoğrafı çekin
4. "Analiz Et" butonuna basın
5. ✅ Sonuç görüntülenmeli

## 🔧 Sorun Giderme

### Hata: "Model yüklenemedi"
**Çözüm**: Assets dosyalarının doğru kopyalandığından emin olun
```bash
# Assets klasörünü kontrol edin
dir assets
# Dosyalar olmalı:
# - bitki_hastalik_modeli.tflite (12.37 MB)
# - disease_info.json (100+ KB)
```

### Hata: "Kamera izni reddedildi"
**Çözüm**: Uygulama ayarlarından kamera iznini manuel olarak verin
- Android: Ayarlar → Uygulamalar → plant_disease_detector → İzinler → Kamera

### Hata: "Paket bulunamadı"
**Çözüm**: Paketleri yeniden yükleyin
```bash
flutter clean
flutter pub get
```

### Hata: "TFLite hatası"
**Çözüm**: Model dosyasının bozulmadığından emin olun
- Model boyutu: 12.37 MB olmalı
- Gerekirse modelinizi yeniden dönüştürün:
```bash
cd ..
python convert_to_tflite.py
```

## 📊 Performans İzleme

### Debug Modunda
```bash
flutter run --profile
```

### Release Modunda (Daha hızlı)
```bash
flutter run --release
```

## 🏗️ APK Oluşturma (Android)

### Debug APK
```bash
flutter build apk --debug
```

### Release APK
```bash
flutter build apk --release
```

APK konumu: `build/app/outputs/flutter-apk/app-release.apk`

## 💻 Windows Uygulaması Oluşturma

```bash
flutter build windows --release
```

Çıktı: `build/windows/x64/runner/Release/`

## 🌐 Web Uygulaması Oluşturma

```bash
flutter build web --release
```

Çıktı: `build/web/`

## 📝 Log İzleme

```bash
flutter logs
```

## 🔥 Hot Reload Kullanımı

Uygulama çalışırken terminalde:
- **Hot Reload**: `r` tuşuna basın
- **Hot Restart**: `R` tuşuna basın
- **Uygulamayı Kapat**: `q` tuşuna basın

## ✅ Başarılı Çalışma Göstergeleri

1. ✓ Uygulama açılır açılmaz yeşil gradient ana sayfa görünür
2. ✓ "Teşhise Başla" butonu çalışır
3. ✓ Kamera ve Galeri butonları aktif
4. ✓ Fotoğraf seçildiğinde önizleme gösterilir
5. ✓ "Analiz Et" butonu çalışır ve sonuç sayfası açılır
6. ✓ Hastalık bilgileri doğru şekilde gösterilir

## 🎯 İlk Çalıştırma Kontrol Listesi

- [ ] Flutter doctor çalıştırıldı mı? (`flutter doctor`)
- [ ] Bağımlılıklar yüklendi mi? (`flutter pub get`)
- [ ] Bir cihaz bağlı mı? (`flutter devices`)
- [ ] Assets dosyaları yerinde mi? (tflite ve json)
- [ ] Android izinleri ayarlandı mı? (AndroidManifest.xml)

## 📞 Destek

Herhangi bir sorun yaşarsanız:
1. Hata mesajını kontrol edin
2. `flutter clean && flutter pub get` komutunu çalıştırın
3. Cihazı yeniden başlatın
4. Uygulamayı yeniden derleyin

---

**Keyifli kullanımlar!** 🌿✨
