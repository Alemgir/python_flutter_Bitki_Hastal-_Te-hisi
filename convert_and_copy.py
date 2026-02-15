import tensorflow as tf
import numpy as np
import os
import shutil

# Modeli yükle
model_path = r"d:\Users\alamg\Desktop\aaa\bitki_hastalik_modeli.keras"
print("Model yukleniyor...")
model = tf.keras.models.load_model(model_path, compile=False)

print(f"TensorFlow Version: {tf.__version__}")

# Model'i build et (dummy input ile)
print("\nModel build ediliyor...")
dummy_input = np.random.rand(1, 128, 128, 3).astype(np.float32)
_ = model(dummy_input, training=False)

print(f"Model Input Shape: {model.input_shape}")
print(f"Model Output Shape: {model.output_shape}")

# TFLite'a dönüştür
print("\nTFLite'a donusturuluyor...")

def representative_dataset():
    for _ in range(100):
        data = np.random.rand(1, 128, 128, 3).astype(np.float32)
        yield [data]

converter = tf.lite.TFLiteConverter.from_keras_model(model)

# En uyumlu ayarlar
converter.optimizations = [tf.lite.Optimize.DEFAULT]
converter.representative_dataset = representative_dataset
converter.target_spec.supported_ops = [
    tf.lite.OpsSet.TFLITE_BUILTINS,
    tf.lite.OpsSet.SELECT_TF_OPS  # TF ops fallback
]
converter.experimental_new_converter = True
converter._experimental_lower_tensor_list_ops = False

tflite_model = converter.convert()

# Geçici kaydet
temp_path = r"d:\Users\alamg\Desktop\aaa\bitki_hastalik_modeli_new.tflite"
with open(temp_path, "wb") as f:
    f.write(tflite_model)

file_size_mb = os.path.getsize(temp_path) / (1024 * 1024)
print(f"\nBAŞARILI! TFLite Model olusturuldu!")
print(f"Gecici Dosya: {temp_path}")
print(f"Boyut: {file_size_mb:.2f} MB")

# Assets klasörüne kopyala
assets_dir = r"d:\Users\alamg\Desktop\aaa\plant_disease_detector\assets"
os.makedirs(assets_dir, exist_ok=True)

dest_path = os.path.join(assets_dir, "bitki_hastalik_modeli.tflite")
shutil.copy2(temp_path, dest_path)
print(f"\nAssets klasorune kopyalandi: {dest_path}")

# Ana dizine de kopyala (eski dosyayı değiştir)
main_path = r"d:\Users\alamg\Desktop\aaa\bitki_hastalik_modeli.tflite"
shutil.copy2(temp_path, main_path)
print(f"Ana dizine kopyalandi: {main_path}")

print(f"\nToplam Boyut: {file_size_mb:.2f} MB")
print(f"Ozellikler: SELECT_TF_OPS (Android uyumlu) + Optimization")
