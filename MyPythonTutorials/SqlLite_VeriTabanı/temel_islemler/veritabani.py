import sqlite3 # Sqlite'yı dahil ediyoruz


baglanti = sqlite3.connect("kütüphane.db") # Tabloya bağlanıyoruz.Eğer böyle tablo yoksa oluşturacak.

cursor = baglanti.cursor() # cursor isimli değişken veritabanı üzerinde işlem yapmak için kullanacağımız imleç olacak.İşlemlerimizi cursor'dan sonraya ayarlayacağız.


def tablo_olustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS kitaplık (İsim TEXT, YazarAdı TEXT, Yayınevi TEXT, Sayfa_Sayısı INT)") # Sorguyu çalıştırıyoruz.
    baglanti.commit() # Sorgunun veritabanı üzerinde geçerli olması için commit işlemi gerekli.(kayıt)

"""
#Tabloya veri ekleyelim.
def veri_ekle():
    cursor.execute("INSERT INTO kitaplık VALUES('BEYAZ GEMİ','CENGİZ AYTMATOV','NOBEL','254')")
    con.commit()
"""

def deger_ekle(gelen_isim,gelen_yazar,gelen_yayinevi,gelen_sayfa_sayisi):
    cursor.execute("INSERT INTO kitaplık VALUES(?,?,?,?)",(gelen_isim,gelen_yazar,gelen_yayinevi,gelen_sayfa_sayisi))
    baglanti.commit()

isim = input("İsim:")
yazar = input("Yazar:")
yayinevi = input("Yayınevi:")
sayfa_sayisi =  int(input("Sayfa Sayısı:"))


deger_ekle(isim,yazar,yayinevi,sayfa_sayisi)

tablo_olustur()
baglanti.close() # Bağlantıyı koparıyoruz.