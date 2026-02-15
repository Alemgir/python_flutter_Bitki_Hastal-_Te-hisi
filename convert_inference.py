import tensorflow as tf
import os

# Modeli yükle
model_path = r"d:\Users\alamg\Desktop\aaa\bitki_hastalik_modeli.keras"
print("📊 Model yükleniyor...")
model = tf.keras.models.load_model(model_path, compile=False)

print(f"📊 TensorFlow Version: {tf.__version__}")
print(f"📊 Model Input Shape: {model.input_shape}")
print(f"📊 Model Output Shape: {model.output_shape}")

# Yeni bir model oluştur (sadece inference için)
print("\n🔧 Inference modeli oluşturuluyor...")
inference_model = tf.keras.Model(
    inputs=model.input,
    outputs=model.output
)

# TFLite'a dönüştür
print("\n🔄 TFLite'a dönüştürülüyor...")
converter = tf.lite.TFLiteConverter.from_keras_model(inference_model)

# Basit ayarlar
converter.optimizations = []
converter.target_spec.supported_ops = [tf.lite.OpsSet.TFLITE_BUILTINS]

try:
    tflite_model = converter.convert()
    
    # Kaydet
    output_path = r"d:\Users\alamg\Desktop\aaa\bitki_hastalik_modeli.tflite"
    with open(output_path, "wb") as f:
        f.write(tflite_model)
    
    file_size_mb = os.path.getsize(output_path) / (1024 * 1024)
    print(f"\n✅ TFLite Model başarıyla dönüştürüldü!")
    print(f"📁 Dosya: {output_path}")
    print(f"💾 Boyut: {file_size_mb:.2f} MB")
    print(f"⚙️ Yöntem: Inference Model (optimizer yok)")
    
except Exception as e:
    print(f"\n❌ Hata: {e}")
    print("\n⚠️ Alternatif: tflite_flutter paketini güncelleyelim...")
