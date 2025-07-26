import time
import random


"""
crud mantıgında olusturulmus kumanda sistemi
"""
class Kumanda:
    def __init__(self, marka, kanal_listesi):
        self.marka = marka
        self.kanal_listesi = kanal_listesi
        self.aktif_kanal = 0
        self.ses_seviyesi = 50
        self.kanal_sayisi = len(kanal_listesi)

    def kanal_ekle(self, kanal):
        self.kanal_listesi.append(kanal)
        self.kanal_sayisi += 1
        print("Ekleniyor...")
        time.sleep(random.uniform(0.5, 2.0))  # Rastgele bir süre bekler
        print(f"{kanal} eklendi.")


    def kanal_sil(self, kanal):
        if kanal in self.kanal_listesi:
            self.kanal_listesi.remove(kanal)
            self.kanal_sayisi -= 1
            print("Siliniyor...")
            time.sleep(random.uniform(0.5, 2.0))  # Rastgele bir süre bekler
            print(f"{kanal} silindi.")

        else:
            print(f"{kanal} kanal listesinde bulunamadı.")

    def kanal_degistir(self, kanal):
        if kanal in self.kanal_listesi:
            self.aktif_kanal = self.kanal_listesi.index(kanal)
            print(f"Kanal değiştirildi: {kanal}")
            time.sleep(random.uniform(0.5, 2.0))  # Rastgele bir süre bekler
        else:
            print(f"{kanal} kanal listesinde bulunamadı.")

    def ses_artir(self):
        if self.ses_seviyesi < 100:
            self.ses_seviyesi += 1
            print(f"Ses seviyesi artırıldı: {self.ses_seviyesi}")
            time.sleep(random.uniform(0.5, 2.0))  # Rastgele bir süre bekler
        else:
            print("Ses seviyesi zaten maksimumda.")

    def ses_azalt(self):
        if self.ses_seviyesi > 0:
            self.ses_seviyesi -= 1
            print(f"Ses seviyesi azaltıldı: {self.ses_seviyesi}")
            time.sleep(random.uniform(0.5, 2.0))  # Rastgele bir süre bekler
        else:
            print("Ses seviyesi zaten minimumda.")

    def __str__(self):
        return f"Kumanda Markası: {self.marka}\nAktif Kanal: {self.kanal_listesi[self.aktif_kanal]}\nSes Seviyesi: {self.ses_seviyesi}\nKanal Sayısı: {self.kanal_sayisi}"

    def __len__(self):
        return self.kanal_sayisi

    def __getitem__(self, index):
        return self.kanal_listesi[index]

# Kumanda sınıfını kullanma
kanallar = ["TRT", "Kanal D", "Star TV", "Show TV", "FOX"]
kumanda = Kumanda("Philips", kanallar)

def menu():
    print("""
    1. Kanal Ekle
    2. Kanal Sil
    3. Kanal Değiştir
    4. Ses Artır
    5. Ses Azalt
    6. Kumanda Bilgilerini Göster
    7. Çıkış
    """)

while True:
    menu()
    secim = input("Lütfen bir işlem seçin: ")
    if secim == "1":
        yeni_kanal = input("Eklenecek kanalın ismi: ")
        kumanda.kanal_ekle(yeni_kanal)
    elif secim == "2":
        silinecek_kanal = input("Silinecek kanalın ismi: ")
        kumanda.kanal_sil(silinecek_kanal)
    elif secim == "3":
        degistirilecek_kanal = input("Geçilecek kanalın ismi: ")
        kumanda.kanal_degistir(degistirilecek_kanal)
    elif secim == "4":
        kumanda.ses_artir()
    elif secim == "5":
        kumanda.ses_azalt()
    elif secim == "6":
        print(kumanda)
    elif secim == "7":
        print("Çıkış yapılıyor...")
        time.sleep(0.6)
        print("Çıkış yapıldı !")
        break
    else:
        print("Geçersiz seçim. Lütfen tekrar deneyin.")
