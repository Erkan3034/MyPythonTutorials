def hesapla(satır):


    satır = satır[:-1] # listenin sonundaki \ işaretini sil.

    liste = satır.split(",") # ","e göre ayırma yap.

    isim = liste[0] # ismi al

    not1 = int(liste[1])

    not2 = int(liste[2])

    not3 = int(liste[3])

    son_not = not1 * (3/10) + not2 * (3/10) + not3 * (4/10)

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







with open("notlar.txt","r",encoding= "utf-8") as file:

    eklenecekler_listesi = []

    for i in file:

        eklenecekler_listesi.append(hesapla(i))

    with open("not_sonuclari.txt","w",encoding="utf-8") as file2: # not_sonuclari.txt dosyası oluşturuluyor.

        for i in eklenecekler_listesi:
            file2.write(i)
