import sqlite3

con = sqlite3.connect("kütüphane.db")

cursor = con.cursor()
"""
1.yürüt
2. fetchall
3. for ile bastır.
"""

# ============================================== VERİLERİ ÇEKME ========================================================

# tablodan verileri alma. (1. sorgu)
def verileri_al():
    cursor.execute("Select * From kitaplık")  # Bütün bilgileri alıyorruz önce
    data = cursor.fetchall()  # Veritabanından bilgileri çekmek için "fetchall()" kullanıyoruz
    print("Kitaplık Tablosunun verileri çekildi...")
    for i in data:  #fetcahall(), bize verileri liste halinde döndürdüğü için bu liste elemanları üzerinde döngü ile dönüyoruz.
        print(i)
    # con.commit() işlemine gerek yok. Çünkü tabloda herhangi bir güncelleme yapmıyoruz.


verileri_al()
# con.close()
print("___________________________________________________________________________")


# 2. sorgu
def verileri_al2():
    cursor.execute("Select İsim,YazarAdı From kitaplık")  # Sadece İsim ve Yazar özelliklerini alıyoruz.
    data2 = cursor.fetchall()
    print("Kitaplık Tablosunun bilgileri.....")
    for i in data2:
        print(i)


verileri_al2()
print("___________________________________________________________________________")


# Yayınevine göre çekelim.
def verileri_al3(yayinevi):
    cursor.execute("Select * From kitaplık where Yayınevi  = ?",(yayinevi,))  # Sadece yayınevi ,Everest olan kitaplara dair tüm bilgileri alıyoruz.

    data3 = cursor.fetchall()
    print("Kitaplık Tablosunun bilgileri.....")
    for i in data3:
        print(i)


verileri_al3("Everest")
print("____________________________________")


#YAZAR ADINA GÖRE ÇEKELİM
def veriler_al4(yazar_adi):
    cursor.execute("Select * from  kitaplık where YazarAdı = ?", (yazar_adi,))
    data4 = cursor.fetchall()

    print("Yazar Adına göre kitaplar...........")

    for i in data4:
        print(i)


veriler_al4("Turgut")

print("____________________________________")

# Sadece yazarAdı ve Yayınevi bilgilerini çekelim.

def verileri_al5():
    cursor.execute("Select YazarAdı,Yayınevi from kitaplık")
    data5 = cursor.fetchall()
    print("Yazar adı ve Yayinevi.........")

    for i in data5:
        print(i)
verileri_al5()


print("____________________________________")



#==============================================VERİLERİ GÜNCELLEME======================================================


"""
1. update
2. set
3. where
4. commit
"""
def verileri_guncelle(degisecek_yayinevi):
    cursor.execute("Update kitaplık set Yayınevi = ?  where Yayınevi = ?",("Nobel",degisecek_yayinevi))
    con.commit()



verileri_guncelle("Everest")
print("Veriler Güncellendi...")


cursor.execute("Select * From kitaplık")  # Bütün bilgileri alıyoruz.
data = cursor.fetchall()  # Veritabanından bilgileri çekmek için "fetchall()" kullanıyoruz.
print("Kitaplık Tablosunun bilgileri.....")
for i in data:
    print(i)


cursor.close()