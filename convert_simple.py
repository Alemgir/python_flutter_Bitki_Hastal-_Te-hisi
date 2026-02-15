import tensorflow as tf
import os

# Modeli yükle
model_path = r"d:\Users\alamg\Desktop\aaa\bitki_hastalik_modeli.keras"
model = tf.keras.models.load_model(model_path)

print("📊 TensorFlow Version:", tf.__version__)
print("📊 Model Yapısı:")
model.summary()

# Basit dönüştürücü - eski uyumlu
converter = tf.lite.TFLiteConverter.from_keras_model(model)

# Hiçbir optimizasyon YAPMA - tam uyumluluk için
converter.optimizations = []
converter.target_spec.supported_ops = [tf.lite.OpsSet.TFLITE_BUILTINS]
converter.experimental_new_converter = False  # ESKİ converter kullan

# Dönüştür
print("\n🔄 Dönüştürülüyor...")
tflite_model = converter.convert()

# Kaydet
output_path = r"d:\Users\alamg\Desktop\aaa\bitki_hastalik_modeli.tflite"
with open(output_path, "wb") as f:
    f.write(tflite_model)

file_size_mb = os.path.getsize(output_path) / (1024 * 1024)
print(f"\n✅ TFLite Model başarıyla dönüştürüldü!")
print(f"📁 Dosya: {output_path}")
print(f"💾 Boyut: {file_size_mb:.2f} MB")
print(f"⚙️ Mod: Eski Converter (Android 11 uyumlu)")
