import tensorflow as tf
import numpy as np
import os

# Modeli yükle
model_path = r"d:\Users\alamg\Desktop\aaa\bitki_hastalik_modeli.keras"
model = tf.keras.models.load_model(model_path)

print("📊 Model Yapısı:")
model.summary()

# Dönüştürücü oluştur
converter = tf.lite.TFLiteConverter.from_keras_model(model)

# Dinamik quantization ekle
converter.optimizations = [tf.lite.Optimize.DEFAULT]
converter.target_spec.supported_ops = [
    tf.lite.OpsSet.TFLITE_BUILTINS_INT8,
    tf.lite.OpsSet.TFLITE_BUILTINS
]

# Quantization-aware training için representative data (dummy)
def representative_dataset():
    for i in range(10):
        random_img = np.random.normal(0, 1, (1, 128, 128, 3)).astype(np.float32)
        yield [random_img]

# Quantization config
converter.representative_data_gen = representative_dataset
converter.inference_input_type = tf.uint8
converter.inference_output_type = tf.uint8

# Dönüştür
tflite_model = converter.convert()

# Kaydet
output_path = r"d:\Users\alamg\Desktop\aaa\bitki_hastalik_modeli.tflite"
with open(output_path, "wb") as f:
    f.write(tflite_model)

file_size_mb = os.path.getsize(output_path) / (1024 * 1024)
print(f"\n✅ TFLite Model başarıyla dönüştürüldü!")
print(f"📁 Dosya: {output_path}")
print(f"💾 Boyut: {file_size_mb:.2f} MB")
print(f"⚙️ Optimizasyon: INT8 Quantization")
