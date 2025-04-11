from datetime import datetime
import locale
locale.setlocale(locale.LC_ALL,"")


tarih = datetime(2024,12,23)

su_an = datetime.now()


print(tarih - su_an)



print(datetime.strftime(su_an, "%Y")) # yıl bilgisi
print(datetime.strftime(su_an, "%B")) # Ay bilgisi
print(datetime.strftime(su_an, "%A")) # Gün ismi
print(datetime.strftime(su_an, "%X")) # Saat bilgisi
print(datetime.strftime(su_an, "%D")) # ay/gün/yıl


