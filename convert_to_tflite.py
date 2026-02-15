import tensorflow as tf
import os

print("Model TFLite formatına dönüştürülüyor...")

# Kaydedilmiş Keras modelini yükle
model_path = r"d:\Users\alamg\Desktop\aaa\bitki_hastalik_modeli.keras"
model = tf.keras.models.load_model(model_path)

print("Model başarıyla yüklendi.")

# TFLite Converter oluştur
converter = tf.lite.TFLiteConverter.from_keras_model(model)

# Optimizasyonlar ekle (model boyutunu küçültür)
converter.optimizations = [tf.lite.Optimize.DEFAULT]

# Modeli dönüştür
tflite_model = converter.convert()

# TFLite modelini kaydet
tflite_path = r"d:\Users\alamg\Desktop\aaa\bitki_hastalik_modeli.tflite"
with open(tflite_path, 'wb') as f:
    f.write(tflite_model)

print(f"\n✓ Model başarıyla TFLite formatına dönüştürüldü!")
print(f"✓ Kaydedilen dosya: {tflite_path}")

# Dosya boyutlarını karşılaştır
keras_size = os.path.getsize(model_path) / (1024 * 1024)  # MB
tflite_size = os.path.getsize(tflite_path) / (1024 * 1024)  # MB

print(f"\nDosya Boyutları:")
print(f"  - Keras Model (.keras): {keras_size:.2f} MB")
print(f"  - TFLite Model (.tflite): {tflite_size:.2f} MB")
print(f"  - Boyut Azalması: {((keras_size - tflite_size) / keras_size * 100):.2f}%")
