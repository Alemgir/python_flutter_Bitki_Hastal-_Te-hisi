import tensorflow as tf
import os

print("Model test script'i başlatıldı...")

# --- DEĞİŞKENLERİ KONTROL ET ---
# Kaydedilmiş modelimizin yolu
model_path = r"d:\Users\alamg\Desktop\aaa\bitki_hastalik_modeli.keras"

# Test veri setimizin yolu
test_dir = r"d:\Users\alamg\Desktop\aaa\split_dataset\test"

# Eğitim sırasında kullandığımız parametrelerle aynı olmalı
IMG_WIDTH = 128
IMG_HEIGHT = 128
BATCH_SIZE = 32
# ---

# 1. Kaydedilmiş Modeli Yükle
print(f"Model yükleniyor: {model_path}")
try:
    model = tf.keras.models.load_model(model_path)
    print("Model başarıyla yüklendi.")
except Exception as e:
    print(f"HATA: Model yüklenirken bir sorun oluştu: {e}")
    exit()

# 2. Test Veri Yükleyicisini Hazırla
# Test verisinde veri artırma (augmentation) yapılmaz, sadece pikseller normalize edilir.
test_datagen = tf.keras.preprocessing.image.ImageDataGenerator(rescale=1./255)

test_generator = test_datagen.flow_from_directory(
    test_dir,
    target_size=(IMG_HEIGHT, IMG_WIDTH),
    batch_size=BATCH_SIZE,
    class_mode='categorical',
    shuffle=False  # Test verisinde karıştırma yapmamak önemlidir
)

# 3. Modeli Test Veri Seti Üzerinde Değerlendir
print("\nModel test verisi üzerinde değerlendiriliyor...")
results = model.evaluate(test_generator)

# 4. Sonuçları Ekrana Yazdır
print("\n------------------ TEST SONUÇLARI ------------------")
print(f"Test Kaybı (Loss): {results[0]:.4f}")
print(f"Test Başarısı (Accuracy): {results[1]*100:.2f}%")
print("----------------------------------------------------")