import os
import random
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# SENİN BİLGİSAYARIN İÇİN GÜNCELLENMİŞ YOL
dataset_path = r"C:\Users\alamg\Downloads\Veri Dataset"

print("Veri Seti Yolu:", dataset_path)

# Klasördeki sınıfları (hastalık isimlerini) al
try:
    # `Dataset` klasörünün içindeki asıl veri klasörünü bulmamız gerekebilir.
    # Eğer alt klasörler doğrudan bu yolda değilse, yolu düzenlememiz gerekebilir.
    # Önce bu yolu deneyelim.
    potential_data_folder = os.path.join(dataset_path, "Dataset")
    if os.path.exists(potential_data_folder):
        data_folder = potential_data_folder
    else:
        # Eğer "Dataset" adında bir alt klasör yoksa, ana yolu kullan
        data_folder = dataset_path

    print("Kullanılan Veri Klasörü:", data_folder)
    
    classes = os.listdir(data_folder)
    print(f"\nToplam {len(classes)} adet sınıf bulundu.")
    print("-----------------------------------------")

    class_counts = {}
    for cls in classes:
        class_path = os.path.join(data_folder, cls)
        if os.path.isdir(class_path):
            num_files = len(os.listdir(class_path))
            class_counts[cls] = num_files
            print(f"- {cls}: {num_files} adet fotoğraf")

    # Rastgele birkaç sınıf seçip görsellerini gösterelim
    print("\n\nRastgele Sınıflardan Örnek Görseller:")
    
    num_samples_to_show = 4 
    plt.figure(figsize=(15, 10))

    # Eğer hiç sınıf bulunamazsa hata vermemesi için kontrol
    if not classes:
         print("\HATA: Belirtilen yolda hiç sınıf klasörü bulunamadı.")
    else:
        random_classes = random.sample(list(class_counts.keys()), min(num_samples_to_show, len(classes)))

        for i, cls in enumerate(random_classes):
            class_path = os.path.join(data_folder, cls)
            random_image_name = random.choice(os.listdir(class_path))
            image_path = os.path.join(class_path, random_image_name)
            
            img = mpimg.imread(image_path)
            
            plt.subplot(2, 2, i + 1)
            plt.imshow(img)
            plt.title(cls, fontsize=10) # Yazı boyutunu biraz küçülttüm
            plt.axis('off')

        plt.tight_layout()
        plt.show()

except FileNotFoundError:
    print(r"\HATA: Belirtilen yol bulunamadı: '{dataset_path}'")
    print("Lütfen yolu kontrol edin. Kopyalarken bir hata yapmış olabilirsiniz.")
except Exception as e:
    print(f"Beklenmedik bir hata oluştu: {e}")