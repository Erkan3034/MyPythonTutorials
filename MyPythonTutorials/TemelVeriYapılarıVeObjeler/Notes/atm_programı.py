print("********************\n ATM \n********************")

print("""
Yapılabilecek işlemler: 

1. Bakiye Sorgulama
2. Para Yatırma
3. Para Çekme

Programdan 'q' tuşu ile çıkabilirsiniz.

""")

bakiye = 5000

while True:
    islem = input("Yapmak istediğiniz işlemi giriniz:")

    if (islem == "q"):
        print("Yine bekleriz....")
        break  # programı sonlandır.
    elif islem == "1":
        print("Bakiyeniz {} tldir".format(bakiye)) #bakiye miktarını göster
    elif (islem == "2"):
        miktar = int(input("Yatırmak istediğiniz tutar:"))
        bakiye += miktar #yatırılan bakiyeyi mevcut bakiyeye ekle
    elif (islem == "3"):
        miktar = int(input("Çekmek istediğiniz tutar:"))
        if (bakiye - miktar < 0):   #Çekilmek istenen tutar bakiyeden fazla ise uyarı ver.
            print("Bu kadar para çekemezsiniz...")
            print("Bakiyeniz {} tldir".format(bakiye))
            continue
        bakiye -= miktar

    else:
        print("Lütfen geçerli bir işlem giriniz.")
