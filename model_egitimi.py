# 1. GEREKLİ KÜTÜPHANELERİ İÇERİ AKTARMA
# -------------------------------------------
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
import matplotlib.pyplot as plt
import os

print("TensorFlow sürümü:", tf.__version__)

# 2. VERİ YOLLARINI VE PARAMETRELERİ TANIMLAMA
# -----------------------------------------------
# Bir önceki adımda oluşturduğumuz, ayrılmış veri setinin yolu
base_dir = r"C:\Users\alamg\Desktop\aaa\split_dataset"

train_dir = os.path.join(base_dir, 'train')
validation_dir = os.path.join(base_dir, 'val')

# Modelimizin daha hızlı öğrenmesi için fotoğrafları yeniden boyutlandıracağımız ölçü
IMG_WIDTH = 128
IMG_HEIGHT = 128
# Modele fotoğrafları kaçarlı gruplar halinde göndereceğimizi belirten parametre
BATCH_SIZE = 32

# 3. VERİ YÜKLEYİCİLERİ VE VERİ ARTIRMA (IMAGE DATA GENERATOR)
# -------------------------------------------------------------
print("\nVeri artırma ve yükleyiciler hazırlanıyor...")

# Eğitim verisi için veri artırma ayarları
train_datagen = ImageDataGenerator(
    rescale=1./255,             # Fotoğraf piksellerini 0-1 arasına normalize et
    rotation_range=40,          # Rastgele 40 dereceye kadar döndür
    width_shift_range=0.2,      # Genişliği %20 oranında rastgele kaydır
    height_shift_range=0.2,     # Yüksekliği %20 oranında rastgele kaydır
    shear_range=0.2,            # %20 oranında rastgele makaslama uygula
    zoom_range=0.2,             # %20 oranında rastgele yakınlaştır
    horizontal_flip=True,       # Yatay olarak rastgele çevir
    fill_mode='nearest'         # Oluşan boşlukları en yakın pikselle doldur
)

# Doğrulama (validation) verisi için sadece normalize etme işlemi yapacağız.
# Çünkü modelin başarısını orijinal, değiştirilmemiş fotoğraflarla ölçmeliyiz.
validation_datagen = ImageDataGenerator(rescale=1./255)

# Veri yükleyicileri oluşturma
# train_dir klasöründeki fotoğrafları okur, veri artırma uygular ve modele gönderir
train_generator = train_datagen.flow_from_directory(
    train_dir,
    target_size=(IMG_HEIGHT, IMG_WIDTH),
    batch_size=BATCH_SIZE,
    class_mode='categorical' # Sınıflandırma problemi olduğu için 'categorical' seçilir
)

# validation_dir klasöründeki fotoğrafları okur ve modele gönderir
validation_generator = validation_datagen.flow_from_directory(
    validation_dir,
    target_size=(IMG_HEIGHT, IMG_WIDTH),
    batch_size=BATCH_SIZE,
    class_mode='categorical'
)

# 4. CNN MODEL MİMARİSİNİ OLUŞTURMA
# ------------------------------------
print("\nCNN modeli oluşturuluyor...")

model = Sequential([
    # 1. Evrişim ve Havuzlama Katmanı
    Conv2D(32, (3,3), activation='relu', input_shape=(IMG_HEIGHT, IMG_WIDTH, 3)),
    MaxPooling2D(2, 2),

    # 2. Evrişim ve Havuzlama Katmanı
    Conv2D(64, (3,3), activation='relu'),
    MaxPooling2D(2, 2),

    # 3. Evrişim ve Havuzlama Katmanı
    Conv2D(128, (3,3), activation='relu'),
    MaxPooling2D(2, 2),

    # Düzleştirme Katmanı
    Flatten(),

    # Yoğun (Dense) Katman ve Dropout
    Dense(512, activation='relu'),
    Dropout(0.5), # Aşırı öğrenmeyi (ezberlemeyi) engellemek için %50'sini rastgele kapat

    # Çıkış Katmanı
    # 23 sınıfımız olduğu için 23 nöron ve 'softmax' aktivasyonu kullanıyoruz
    Dense(23, activation='softmax')
])

# Modelin özetini yazdır
model.summary()

# 5. MODELİ DERLEME
# -------------------
print("\nModel derleniyor...")
model.compile(optimizer='adam',
              loss='categorical_crossentropy', # Çok sınıflı sınıflandırma için standart loss fonksiyonu
              metrics=['accuracy'])

# 6. MODELİ EĞİTME
# -----------------
print("\nModel eğitimi başlıyor...")
# Eğitim süreci için epoch sayısı (modelin tüm veri setini kaç kez göreceği)
EPOCHS = 20

# Modeli eğit!
history = model.fit(
    train_generator,
    epochs=EPOCHS,
    validation_data=validation_generator,
    verbose=1
)

# 7. EĞİTİM SONUÇLARINI GÖRSELLEŞTİRME
# ------------------------------------
# Eğitim ve doğrulama başarısını (accuracy) çizdir
plt.figure(figsize=(12, 4))
plt.subplot(1, 2, 1)
plt.plot(history.history['accuracy'], label='Eğitim Başarısı')
plt.plot(history.history['val_accuracy'], label='Doğrulama Başarısı')
plt.title('Eğitim ve Doğrulama Başarısı')
plt.legend()

# Eğitim ve doğrulama kaybını (loss) çizdir
plt.subplot(1, 2, 2)
plt.plot(history.history['loss'], label='Eğitim Kaybı')
plt.plot(history.history['val_loss'], label='Doğrulama Kaybı')
plt.title('Eğitim ve Doğrulama Kaybı')
plt.legend()

plt.show()

print("\nEğitim tamamlandı!")

# 8. EĞİTİLEN MODELİ KAYDETME
# ---------------------------
model.save("bitki_hastalik_modeli.keras")
print("\nModel 'bitki_hastalik_modeli.keras' adıyla kaydedildi.")