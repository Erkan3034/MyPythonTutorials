"""

Asal sayı : 1 ve kendisinden başka böleni bulunmayan sayılara denir.

Dolayısıyla bir sayının 2'den fazla böleni varsa bu sayı asal değildir.

2 sayısı en küçük asal sayıdır.
"""
from random import sample


def asal_mi(sayi):
    if sayi == 1:
        return False
    elif sayi == 2:
        return True
    else:
        for i in range(2, sayi):
            if sayi % i == 0:
                return False
        return True


while True:
    sayi = input("SAYI: ")

    if sayi == "q":
        print("Program sonlandırıldı!!")
        break
    else:
        sayi = int(sayi)

    if asal_mi(sayi):
        print(sayi, "sayısı asaldır")

    else:
        print(sayi, "sayısı asal değildir !")
