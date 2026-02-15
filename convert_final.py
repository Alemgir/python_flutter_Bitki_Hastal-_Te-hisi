import tensorflow as tf
import numpy as np
import os

# Modeli yükle
model_path = r"d:\Users\alamg\Desktop\aaa\bitki_hastalik_modeli.keras"
print("📊 Model yükleniyor...")
model = tf.keras.models.load_model(model_path, compile=False)

print(f"📊 TensorFlow Version: {tf.__version__}")

# Model'i build et (dummy input ile)
print("\n🔧 Model build ediliyor...")
dummy_input = np.random.rand(1, 128, 128, 3).astype(np.float32)
_ = model(dummy_input, training=False)

print(f"✓ Model Input Shape: {model.input_shape}")
print(f"✓ Model Output Shape: {model.output_shape}")

# TFLite'a dönüştür
print("\n🔄 TFLite'a dönüştürülüyor...")

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

try:
    tflite_model = converter.convert()
    
    # Kaydet
    output_path = r"d:\Users\alamg\Desktop\aaa\assets\bitki_hastalik_modeli.tflite"
    with open(output_path, "wb") as f:
        f.write(tflite_model)
    
    file_size_mb = os.path.getsize(output_path) / (1024 * 1024)
    print(f"\n✅ TFLite Model başarıyla dönüştürüldü!")
    print(f"📁 Dosya: {output_path}")
    print(f"💾 Boyut: {file_size_mb:.2f} MB")
    print(f"⚙️ Ayarlar: SELECT_TF_OPS (fallback) + Optimization")
    
except Exception as e:
    print(f"\n❌ Hata: {e}")
    import traceback
    traceback.print_exc()
