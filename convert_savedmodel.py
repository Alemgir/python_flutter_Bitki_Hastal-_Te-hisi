import tensorflow as tf
import os
import tempfile

# Modeli yükle
model_path = r"d:\Users\alamg\Desktop\aaa\bitki_hastalik_modeli.keras"
model = tf.keras.models.load_model(model_path)

print("📊 TensorFlow Version:", tf.__version__)
print("📊 Model yüklendi")

# SavedModel olarak geçici kaydet
temp_dir = tempfile.mkdtemp()
saved_model_path = os.path.join(temp_dir, "saved_model")
print(f"\n💾 SavedModel oluşturuluyor: {saved_model_path}")
tf.saved_model.save(model, saved_model_path)

# SavedModel'den TFLite'a dönüştür
print("\n🔄 TFLite'a dönüştürülüyor...")
converter = tf.lite.TFLiteConverter.from_saved_model(saved_model_path)
converter.optimizations = []
converter.target_spec.supported_ops = [tf.lite.OpsSet.TFLITE_BUILTINS]

tflite_model = converter.convert()

# Kaydet
output_path = r"d:\Users\alamg\Desktop\aaa\bitki_hastalik_modeli.tflite"
with open(output_path, "wb") as f:
    f.write(tflite_model)

# Cleanup
import shutil
shutil.rmtree(temp_dir, ignore_errors=True)

file_size_mb = os.path.getsize(output_path) / (1024 * 1024)
print(f"\n✅ TFLite Model başarıyla dönüştürüldü!")
print(f"📁 Dosya: {output_path}")
print(f"💾 Boyut: {file_size_mb:.2f} MB")
print(f"⚙️ Yöntem: SavedModel → TFLite")
