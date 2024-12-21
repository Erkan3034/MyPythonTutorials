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
=================================================
""")

market = Market()

while True:
    islem = input("Yapmak istediğiniz işlem: ")

    if islem == "6":
        print("İşleminiz Sonlandırılıyor...")
        time.sleep(1)
        market.disconnect()
        print("İşleminiz sonlandırıldı, Görüşmek Üzere 🖐️")
        break
    elif islem == "1":
        products = market.list_products()
        if not products:
            print("Hiç ürün bulunamadı.")
        else:
            for product in products:
                print(f"Ad: {product[0]}, ID: {product[1]}, Fiyat: {product[2]}, Miktar: {product[3]}")

    elif islem == "2":
        name = input("Ürün ismi: ")
        id = input("Ürün ID: ")
        price = input("Ürün Fiyatı: ")
        amount = input("Ürün Miktarı: ")
        new_product = Product(name, id, float(price), int(amount))
        market.add_product(new_product)
        print("Ürün başarıyla eklendi!")

    elif islem == "3":
        name = input("Hangi ürünü sorgulamak istiyorsunuz? ")
        products = market.search_product(name)
        if products:
            for product in products:
                print(f"Ad: {product[0]}, ID: {product[1]}, Fiyat: {product[2]}, Miktar: {product[3]}")
        else:
            print("Ürün bulunamadı.")
    elif islem == "4":
        name = input("Silmek istediğiniz ürünün adı: ")
        market.delete_product(name)
        print("Ürün başarıyla silindi!")
    elif islem == "5":
        name = input("Miktarını arttırmak istediğiniz ürünün adı: ")
        if market.increase_amount(name):
            print("Ürün miktarı başarıyla arttırıldı!")
        else:
            print("Ürün bulunamadı!")
    else:
        print("Geçersiz işlem!")
