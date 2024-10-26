# 2.dereceden bir bilinmeyenli denklemin köklerini bulan program
"""
     denklem : ax^2 +bx + c
     delta : b^2 -4(a.c)

     birinci kök : (-b-delta^0.5)/2*a
     ikinci kök : (-b+delta^0.5)/2*a


"""

print("Lütfen köklerini bulmak istediğiniz denkleme ait istenilen değerleri giriniz:")
print(" ")

a=int(input("a değerini giriniz: "))
b=int(input("b değerini giriniz: "))
c=int(input("c değerini giriniz: "))

print("Girilen değerler kaydediliyor...")
print(" ")
print("Kökler hesaplanıyor...")

delta=(b**2)-4*(a*c)
birinci_kok=(-b-(delta**0.5)/(2*a))
ikinci_kok=(-b+(delta**0.5)/(2*a))


print("Girilen denkleme ait 1. kök : {}\n 2.kök: {}".format(birinci_kok,ikinci_kok))
