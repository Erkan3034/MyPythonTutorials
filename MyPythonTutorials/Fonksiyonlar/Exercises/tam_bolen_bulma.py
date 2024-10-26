# bir sayının tam bölenlerini bulup bu bölenlerş bir listeye atama işlemi.

def tamBoleniBul(sayi):

    tamBolenler = []  # bölenleri tutacak olan liste
    for i in range(2,sayi):
        if sayi%i==0:
            tamBolenler.append(i)
    return tamBolenler

while True:
    sayi = input("Sayı giriniz: ")

    if sayi == "q":
        print("Program sonlandırıldı !!")
        break
    try:
        sayi = int(sayi)
        print("Tam bölenler:", tamBoleniBul(sayi))
    except ValueError:
            print("Hatalı giriş! Lütfen bir sayı giriniz.")