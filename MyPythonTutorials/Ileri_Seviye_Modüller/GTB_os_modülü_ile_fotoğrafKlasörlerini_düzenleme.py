import os
import shutil
from datetime import datetime

from PIL import Image
from PIL.ExifTags import TAGS

print("DİZİN: " , os.getcwd()) # dizini söyle


# Fotoğraf dosyalarının bulunduğu kaynak dizin
source_dir = r"C:\Users\ERKAN TURGUT\Downloads"
# Fotoğrafların taşınacağı hedef dizin
target_dir = r"C:\Users\ERKAN TURGUT\Downloads\Düzenlenmis_Fotograflar"

# Hedef dizin yoksa oluştur
if not os.path.exists(target_dir):
    os.mkdir(target_dir)

# Fotoğraf dosyalarını kaynak dizinde tarama
for file_name in os.listdir(source_dir):
    file_path = os.path.join(source_dir, file_name)

    # Dosyanın bir resim dosyası olup olmadığını kontrol et
    if os.path.isfile(file_path) and file_name.lower().endswith(('.jpg', '.jpeg', '.png')):
        try:
            # Fotoğrafın EXIF verilerini oku
            image = Image.open(file_path)
            exif_data = image._getexif()

            if exif_data is not None:
                # EXIF verisindeki 'DateTime' etiketini kullanarak fotoğrafın çekildiği tarihi al
                for tag, value in exif_data.items():
                    if TAGS.get(tag) == 'DateTime':
                        photo_date = value  # 'DateTime' formatı: YYYY:MM:DD HH:MM:SS
                        break
                else:
                    # EXIF verisi yoksa, dosya adı üzerinden tarihi tahmin etmeye çalış
                    photo_date = datetime.fromtimestamp(os.path.getmtime(file_path)).strftime('%Y:%m:%d')
            else:
                # EXIF verisi yoksa, dosyanın son değiştirilme tarihini kullan
                photo_date = datetime.fromtimestamp(os.path.getmtime(file_path)).strftime('%Y:%m:%d')

            # Fotoğrafın tarihini yıl ve aya göre düzenle (örneğin 2024/12)
            year, month, _ = photo_date.split(':')
            year_month_dir = os.path.join(target_dir, year, month)

            # Hedef dizinde yıl/ay klasörünü oluştur
            if not os.path.exists(year_month_dir):
                os.makedirs(year_month_dir)

            # Fotoğrafı ilgili klasöre taşı
            new_path = os.path.join(year_month_dir, file_name)
            shutil.move(file_path, new_path)
            print(f"{file_name} taşındı -> {new_path}")

        except Exception as e:
            print(f"{file_name} işlenirken hata oluştu: {e}")

print("Fotoğraflar düzenlendi ve taşındı.")


"""
     Uygulamanın Açıklaması:

Dizinler ve Dosyalar:

source_dir: Fotoğrafların bulunduğu kaynak dizin.
target_dir: Fotoğrafların taşınacağı düzenlenmiş dizin.
Hedef Dizin Kontrolü ve Oluşturulması:

os.path.exists() ile hedef dizin kontrol edilir ve mevcut değilse os.makedirs() ile gerekli tüm klasörler (yıl/ay) oluşturulur.
EXIF Verilerini Okuma:

Fotoğrafların çekildiği tarih EXIF verilerinden alınır.
Eğer fotoğrafın EXIF verisi yoksa, dosyanın son değiştirilme tarihi alınır.
Yıl ve Ay Klasörleri:

Fotoğraflar, çekildikleri yıla ve ayına göre alt dizinlere taşınır (örneğin 2024/12 gibi).
Dosya Taşıma:

shutil.move() ile fotoğraf dosyası ilgili yıl/ay klasörüne taşınır.
Hata Yönetimi:

Fotoğraflar üzerinde işlem yapılırken olabilecek hatalar try-except bloğu ile yakalanır ve hata mesajı yazdırılır.

"""