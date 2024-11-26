def hesapla(satır):


    satır = satır[:-1] # listenin sonundaki \ işaretini sil.

    liste = satır.split(",") # ","e göre ayırma yap.( liste ögelerini ,'e göre tekrar listeler)

    isim = liste[0] # ismi al (,'e göre ayırma yaptığımızda isim, listenin 1. indeksinde yer alır)

    not1 = int(liste[1])

    not2 = int(liste[2])

    not3 = int(liste[3])

    son_not = not1 * (3/10) + not2 * (3/10) + not3 * (4/10) #Not sonucu hesaplama.

    if (son_not >= 90):
        harf = "AA"
    elif (son_not >= 85):
        harf = "BA"
    elif (son_not >= 80):
        harf = "BB"
    elif (son_not >= 75):
        harf = "CB"
    elif (son_not >= 70):
        harf = "CC"
    elif (son_not >= 65):
        harf = "DC"
    elif (son_not >= 60):
        harf = "DD"
    elif (son_not >= 55):
        harf = "FD"
    else:
        harf = "FF"

    return isim + "------------------> " + harf + "\n"







with open("notlar.txt","r",encoding= "utf-8") as file: # Dosyayı aç, read et.

    eklenecekler_listesi = [] # Not sonuclarını tutacağımız liste.

    for i in file: # dosyadaki her satır.

        eklenecekler_listesi.append(hesapla(i)) # gelen satırı hesapla() fonksiyonuna gönder ve işle.

    with open("not_sonuclari.txt","w",encoding="utf-8") as file2: # not_sonuclari.txt dosyası oluşturuluyor.

        for i in eklenecekler_listesi: # eklenecekler listesi artık sonuçları tutan liste. Ordan verileri alıp yazalım.
            file2.write(i)
