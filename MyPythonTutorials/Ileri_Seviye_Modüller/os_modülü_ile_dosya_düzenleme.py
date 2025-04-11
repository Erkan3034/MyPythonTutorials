import os
import shutil  # Dosya/dizin taşıma işlemleri için gerekli modül

# Çalışma dizinini belirleme

source_dir = r"C:\Users\ERKAN TURGUT\OneDrive\Masaüstü\WEBWORKS\Html şablon"  # İşlem yapılacak dizin
target_dir = r"C:\Users\ERKAN TURGUT\OneDrive\Masaüstü\WEBWORKS\Html şablon\HTML_SABLON"  # Dosyaların taşınacağı dizin

# Hedef dizin yoksa oluştur
if not os.path.exists(target_dir):  # Eğer hedef dizin mevcut değilse
    os.mkdir(target_dir)  # Hedef dizini oluştur

# Kaynak dizindeki dosyaları listele
try:
    for file_name in os.listdir(source_dir):  # Kaynak dizindeki tüm dosya ve klasörleri listele
        # Dosya yolunu oluştur
        file_path = os.path.join(source_dir, file_name)  # Kaynak dizindeki tam dosya yolunu oluştur

        # Sadece .html dosyalarını işle
        if os.path.isfile(file_path) and file_name.endswith(".html"):  # Sadece dosyaları ve .html uzantılı olanları seç
            # Yeni hedef yolu oluştur
            new_path = os.path.join(target_dir, file_name)  # Hedef dizindeki yeni dosya yolunu oluştur
            shutil.move(file_path, new_path)  # Dosyayı kaynak dizinden hedef dizine taşı
            print(f"{file_name} taşındı -> {new_path}")  # Taşınan dosya ve yeni konumunu yazdır
except FileNotFoundError as e:  # Eğer kaynak dizin bulunamazsa
    print(f"Hata: {e}")  # Hata mesajını yazdır
except Exception as e:  # Diğer beklenmeyen hatalar için genel bir hata yakalama
    print(f"Bilinmeyen bir hata oluştu: {e}")  # Hata mesajını yazdır

print("İşlem tamamlandı.")  # İşlemin tamamlandığını bildiren mesaj

