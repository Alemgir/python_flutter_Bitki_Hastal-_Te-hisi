import tensorflow as tf
import os

# Modeli yükle
model_path = r"d:\Users\alamg\Desktop\aaa\bitki_hastalik_modeli.keras"
converter = tf.lite.TFLiteConverter.from_keras_model(
    tf.keras.models.load_model(model_path)
)

# Optimizasyon seçeneği KALDIRIYORUZ - eski Android cihazlar için
converter.optimizations = []  # Boş - optimizasyon yok
converter.target_spec.supported_ops = [
    tf.lite.OpsSet.TFLITE_BUILTINS
]

# Dönüştür
tflite_model = converter.convert()

# Kaydet
output_path = r"d:\Users\alamg\Desktop\aaa\bitki_hastalik_modeli.tflite"
with open(output_path, "wb") as f:
    f.write(tflite_model)

file_size_mb = os.path.getsize(output_path) / (1024 * 1024)
print(f"✅ TFLite Model başarıyla dönüştürüldü!")
print(f"📁 Dosya: {output_path}")
print(f"💾 Boyut: {file_size_mb:.2f} MB")
print(f"⚙️ Optimizasyon: KALDIRILDı (eski cihazlar için)")
