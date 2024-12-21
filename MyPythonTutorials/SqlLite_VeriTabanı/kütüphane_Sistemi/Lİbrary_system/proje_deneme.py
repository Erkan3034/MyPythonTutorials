import time
from library import *
# kendi yazdığımız modül.

print(""" =================================================
| Kütüphane Programına Hoşgeldiniz...            |
|                                                |
| Yapmak istediğiniz işlemi Seçiniz:             |
|                                                |
| 1) Kitapları Göster                            |
| 2) Kitap Ekle                                  |
| 3) Kitap Sorgula                               |
| 4) Kitap Sil                                   |
| 5) Baskı Yükselt                               |
| 6) Çıkış                                       |
|                                                |
=================================================
""")

kutuphane = Kutuphane()

while True:

    islem = input("Yapmak istediğiniz işlem: ")

    if islem == "6":
        print("İşleminiz Sonlandırılıyor....")
        time.sleep(1)
        print("İşleminiz sonlandırıldı, Görüşmek Üzere🖐️")
        break


    elif islem == "1":
       kutuphane.kitaplari_goster2()


    elif islem == "2":
        isim = input("Kitap ismi: ")
        yazaradi = input("Kitap yazarı: ")
        tur = input("Kitap türü: ")
        yayinevi = input("Yayınevi: ")
        baski = int(input("Baskı: "))

        yeni_kitap = Kitap(isim,yazaradi,yayinevi,tur,baski) #obje
        print("Kitap ekleniyor...")
        time.sleep(1)
        kutuphane.kitap_ekle(yeni_kitap)
        print("Kİtap başarıyla eklendi...")



    elif islem == "3":
       isim = input("Hangi kitabı sorgulamak istiyorsunuz?  ")
       print("Kitap sorgulanıyor...")
       time.sleep(2)
       kutuphane.kitap_sorgula(isim)


    elif islem == "4":
        silinecek_kitap = input("Silmek istediğiniz Kitap ismi: ")
        print("Kitap siliniyor....")
        time.sleep(2)
        kutuphane.kitap_sil(silinecek_kitap)
        print("Kitap başarıyla Silindi....")

    elif islem == "5":
        try:
            yeni_baski = input("Kitap ismi Giriniz: ")
            kutuphane.baski_yukseltme(yeni_baski)
            print("İşlem başarılı...")
        except sqlite3.OperationalError as e:
            print("Veritabanı bağlantı hatası:", e)

    else:
        print("Geçersiz İşlem!..")


