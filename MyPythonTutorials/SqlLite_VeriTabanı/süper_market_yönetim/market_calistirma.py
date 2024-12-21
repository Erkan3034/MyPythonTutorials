import time
from market import *

print(""" =================================================
| Market Programına Hoşgeldiniz...               |
|                                                |
| Yapmak istediğiniz işlemi Seçiniz:             |
|                                                |
| 1) Ürünleri Göster                             |
| 2) Ürün Ekle                                   |
| 3) Ürün Sorgula                                |
| 4) Ürün Sil                                    |
| 5) Ürün Miktarı Arttır                         |
| 6) Çıkış                                       |
|                                                |
=================================================
""")

market = Market()

while True:

    islem = input("Yapmak istediğiniz işlem: ")

    if islem == "6":
        print("İşleminiz Sonlandırılıyor....")
        time.sleep(1)
        print("İşleminiz sonlandırıldı, Görüşmek Üzere🖐️")
        break


    elif islem == "1":
       market.list_products()


    elif islem == "2":
        name = input("Ürün ismi: ")
        id = input("Ürün İd: ")
        price = input("Ürün Fiyatı: ")
        amount = input("Ürün Miktarı: ")


        new_product = Product(name,id,price,amount) #obje
        print("Product adding...")
        time.sleep(1)
        market.add_product(new_product)
        print("Product added Succesfully...")



    elif islem == "3":
       name = input("Hangi ürübü sorgulamak istiyorsunuz?  ")
       print("Ürün sorgulanıyor...")
       time.sleep(2)
       market.search_product(name)


    elif islem == "4":
        product_to_del = input("Silmek istediğiniz Ürün ismi: ")
        print("Kitap siliniyor....")
        time.sleep(2)
        market.delete_product(product_to_del)
        print("Ürün başarıyla Silindi....")

    elif islem == "5":
        try:
            new_amount = input("Ürün ismi Giriniz: ")
            market.increase_amount(new_amount)
            print("İşlem başarılı...")
        except sqlite3.OperationalError as e:
            print("Veritabanı bağlantı hatası:", e)

    else:
        print("Geçersiz İşlem!..")


