import sqlite3

# "kütüphane.db" adlı  veritabanına bağlanıyoruz. Eğer bu dosya yoksa SQLite otomatik olarak oluşturur.
con = sqlite3.connect("kütüphane.db")

# Veritabanı üzerinde işlem yapmak için bir cursor (imleç) oluşturuyoruz.
cursor = con.cursor()


# Bir fonksiyon tanımlıyoruz. Bu fonksiyon, belirtilen yazara göre kayıtları siliyor.
def verilerisil(yazar):
    # Yazar adı verilen değere eşit olan kayıtları siliyoruz.
    cursor.execute("DELETE FROM kitaplık WHERE YazarAdı = ?", (yazar,))
    # Yapılan değişiklikleri veritabanına kaydediyoruz.
    con.commit()


# "Atıcı" isimli yazara ait kayıtları silmek için fonksiyonu çağırıyoruz.
verilerisil("Atıcı")


# Tablodaki tüm kayıtları çekmek için SELECT sorgusu çalıştırıyoruz.
cursor.execute("SELECT * FROM kitaplık")

# Çekilen verileri bir liste olarak alıyoruz.
data = cursor.fetchall()

# Tablo içeriğini ekrana yazdırıyoruz.
print("Kitaplık Tablosunun bilgileri:")
for i in data:
    print(i)

# Veritabanı bağlantısını kapatıyoruz.
con.close()
