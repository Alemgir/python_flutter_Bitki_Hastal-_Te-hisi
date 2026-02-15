import os
import shutil
import random

print("Veri ayırma script'i başlatıldı...")

# Ana veri setinin yolu (Lütfen kontrol et)
source_dataset_path = r"C:\Users\alamg\Downloads\Veri Dataset\Dataset"

# Yeni, ayrılmış veri setinin oluşturulacağı ana klasör
# Bu klasör, 'aaa' masaüstü klasörünüzün içinde oluşturulacak
base_dir = r"C:\Users\alamg\Desktop\aaa\split_dataset"

# --- Klasörleri oluşturma ---
print(f"'{base_dir}' ana klasörü oluşturuluyor...")
os.makedirs(base_dir, exist_ok=True)

train_dir = os.path.join(base_dir, 'train')
os.makedirs(train_dir, exist_ok=True)

validation_dir = os.path.join(base_dir, 'val')
os.makedirs(validation_dir, exist_ok=True)

test_dir = os.path.join(base_dir, 'test')
os.makedirs(test_dir, exist_ok=True)

# Ayırma oranları
train_split_ratio = 0.8
val_split_ratio = 0.1
# Test oranı geri kalan olacak (0.1)

# --- Fotoğrafları ayırma ve kopyalama işlemi ---
try:
    classes = os.listdir(source_dataset_path)
    print(f"\nToplam {len(classes)} sınıf bulundu. Ayırma işlemi başlıyor...")
    print("--------------------------------------------------")

    for cls in classes:
        source_cls_path = os.path.join(source_dataset_path, cls)
        
        # Hedef klasörleri de oluştur
        train_cls_dir = os.path.join(train_dir, cls)
        os.makedirs(train_cls_dir, exist_ok=True)
        
        val_cls_dir = os.path.join(validation_dir, cls)
        os.makedirs(val_cls_dir, exist_ok=True)
        
        test_cls_dir = os.path.join(test_dir, cls)
        os.makedirs(test_cls_dir, exist_ok=True)
        
        # Sınıf içindeki tüm dosyaları listele ve karıştır
        all_files = os.listdir(source_cls_path)
        random.shuffle(all_files)
        
        total_files = len(all_files)
        train_count = int(total_files * train_split_ratio)
        val_count = int(total_files * val_split_ratio)
        
        # Dosyaları ayır
        train_files = all_files[:train_count]
        val_files = all_files[train_count : train_count + val_count]
        test_files = all_files[train_count + val_count :]
        
        # Dosyaları yeni yerlerine kopyala
        for fname in train_files:
            shutil.copy(os.path.join(source_cls_path, fname), os.path.join(train_cls_dir, fname))
        
        for fname in val_files:
            shutil.copy(os.path.join(source_cls_path, fname), os.path.join(val_cls_dir, fname))
            
        for fname in test_files:
            shutil.copy(os.path.join(source_cls_path, fname), os.path.join(test_cls_dir, fname))
            
        print(f"- '{cls}' sınıfı ayrıldı: Eğitim={len(train_files)}, Doğrulama={len(val_files)}, Test={len(test_files)}")

    print("\n--------------------------------------------------")
    print("Tüm dosyalar başarıyla ayrıldı ve kopyalandı!")
    print(f"Yeni veri setiniz şu yolda oluşturuldu: '{base_dir}'")

except FileNotFoundError:
    print(f"\HATA: Kaynak veri seti yolu bulunamadı: '{source_dataset_path}'")
    print("Lütfen koddaki 'source_dataset_path' değişkenini kontrol edin.")
except Exception as e:
    print(f"Beklenmedik bir hata oluştu: {e}")