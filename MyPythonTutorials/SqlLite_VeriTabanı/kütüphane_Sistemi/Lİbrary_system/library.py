import sqlite3
import time


class Kitap():
    # Kitap sınıfı kitap bilgilerini tutar. Kitapların özelliklerini tanımlamak için kullanılır.
    def __init__(self, isim, yazar, yayinevi, tur, baski):
        self.isim = isim
        self.yazar = yazar
        self.yayinevi = yayinevi
        self.tur = tur
        self.baski = baski

    def __str__(self):
        # Kitap bilgilerini düzgün bir formatta döndürmek için __str__ metodu kullanılır.
        return ("Kitap ismi: {}\n"
                "Yazar: {}\n"
                "YayınEvi: {}\n"
                "Tür: {}\n"
                "Baskı: {}"
                .format(self.isim, self.yazar, self.yayinevi, self.tur, self.baski)
                )


class Kutuphane():
    # Kütüphane sınıfı veritabanı işlemleri için oluşturuldu.

    def __init__(self):
        # Sınıfın örneği oluşturulurken veritabanı bağlantısını hemen kurar.
        self.baglanti_olustur()

    # ========================Bağlantı Oluşturma======================

    def baglanti_olustur(self):
        # Veritabanına bağlanır ve tabloyu oluşturur (eğer yoksa).
        self.baglanti = sqlite3.connect("library.db")  # Veritabanı bağlantısı oluşturulur.
        self.cursor = self.baglanti.cursor()  # SQL sorgularını yürütmek için cursor nesnesi alınır.

        sorgu = "CREATE TABLE IF NOT EXISTS kitaplar(isim TEXT , yazar TEXT , yayınevi TEXT , tur TEXT , baski INT)"
        # Eğer 'kitaplar' tablosu yoksa oluşturulur.

        self.cursor.execute(sorgu)  # SQL sorgusunu çalıştırır.
        self.baglanti.commit()  # Değişiklikler kaydedilir.


    # ========================Bağlantı Kesme======================
    def baglantiyi_kes(self):
        # Veritabanı bağlantısını kapatır.
        self.baglanti.close()


    # ========================Kİtapları Gösterme======================
    def kitaplari_goster2(self):
        # Tüm kitapları veritabanından çeker ve ekrana yazdırır.
        sorgu = "Select * from kitaplar"  # Tablodaki tüm kayıtları seçmek için SQL sorgusu.
        self.cursor.execute(sorgu)  # Sorguyu çalıştırır.

        kitaplar = self.cursor.fetchall()  # Tüm sonuçları bir liste olarak alır.

        if len(kitaplar) == 0:
            # Eğer kayıt yoksa bilgilendirme mesajı göster
            print("Kayıtlı kitap bulunmamaktadır!")
        else:
            for i in kitaplar:
                # Her bir kayıt için bir Kitap nesnesi oluşturulur ve yazdırılır.
                kitap = Kitap(i[0], i[1], i[2], i[3], i[4])
                print(kitap)
                print(" ")


    # ========================Kitap  Sorgulama======================
    def kitap_sorgula(self, isim):
        # Verilen isimdeki kitabı sorgular
        sorgu = "Select * from kitaplar where isim = ?"  # Sadece belirtilen ismi arar
        self.cursor.execute(sorgu, (isim,))  # Parametreli sorgu. 'isim' değeri sorguya yerleştirilir

        kitaplar = self.cursor.fetchall()

        if len(kitaplar) == 0:
            print("Böyle bir kitap bulunmamaktadır!..")
        else:
            # Bulunan kitabın bilgileri bir Kitap nesnesine dönüştürülüp yazdırılır.
            kitap = Kitap(kitaplar[0][0], kitaplar[0][1], kitaplar[0][2], kitaplar[0][3], kitaplar[0][4])
            print(kitap)

    # ========================Kitap  EKLEME======================

    def kitap_ekle(self, kitap):
        # Verilen Kitap nesnesini veritabanına ekler.
        sorgu = "INSERT INTO kitaplar VALUES(?,?,?,?,?)"
        self.cursor.execute(sorgu, (kitap.isim, kitap.yazar, kitap.yayinevi, kitap.tur, kitap.baski))
        self.baglanti.commit()

    # ========================Kitap  SİLME======================

    def kitap_sil(self, isim):
        # Verilen isimdeki kitabı veritabanından siler.
        sorgu = "DELETE FROM kitaplar WHERE isim = ?"
        self.cursor.execute(sorgu, (isim,))
        self.baglanti.commit()

    # ========================Baskı Yükseltme======================

    def baski_yukseltme(self, isim):
        # Verilen isimdeki kitabın baskı sayısını bir artırır.
        sorgu = "SELECT * FROM kitaplar WHERE isim = ?"
        self.cursor.execute(sorgu, (isim,))  # Belirtilen isme göre kitabı bulur.

        kitaplar = self.cursor.fetchall()

        if len(kitaplar) == 0:
            # Eğer kitap bulunamazsa bilgilendirme mesajı
            print("Böyle bir kitap bulunmamaktadır!..")
        else:
            baski = kitaplar[0][4]  # Mevcut baskı sayısı alınır.
            baski += 1  # Baskı sayısı artırılır.

            sorgu2 = "UPDATE kitaplar SET baski = ? WHERE isim = ?"
            self.cursor.execute(sorgu2, (baski, isim))  # Yeni baskı sayısı güncellenir.
            self.baglanti.commit()

