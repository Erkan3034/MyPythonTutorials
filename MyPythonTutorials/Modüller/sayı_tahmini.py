import random  # random modülü tanıtımı

import time  # time modülü tanıtımı
#import math
print("""
******************************
        SAYI TAHMİN OYUNU 

   10 tane deneme hakkınız bulunmaktadır. 

******************************
""")

random_sayi = random.randint(1, 1000)  # random modülünden sayı üretimi
tahmin_hakki = 10

while True:
    tahmin = int(input("Tahmininizi giriniz  : "))

    if tahmin < random_sayi:
        print("Sorgu yapılıyor...")
        time.sleep(1)  # 1sn bekleme

        print("--> Daha büyük bir sayı deneyiniz !")
        tahmin_hakki -= 1
    elif tahmin > random_sayi:
        print("Sorgu yapılıyor...")
        time.sleep(1)

        print("--> Daha küçük bir sayı deneyiniz !")
        tahmin_hakki -= 1
    else:
        print("Sorgu yapılıyor ...")
        time.sleep(1)
        print("Tebrikler Doğru tahmin !")
        break
    if tahmin_hakki == 0:
        print("Maalesef tahmin hakkınız bitti, 30 dk. sonra  tekrar deneyiniz.")
        break
#print(math.ceil(1.5))
