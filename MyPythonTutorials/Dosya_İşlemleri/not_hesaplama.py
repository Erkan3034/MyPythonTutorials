import time


def hesapla(satir):
    satir = satir.strip()  # Satır sonundaki boşlukları veya \n karakterini sil
    liste = satir.split(",")  # ","e göre ayırma yap

    isim = liste[0]  # Öğrencinin ismini al
    not1 = int(liste[1])
    not2 = int(liste[2])
    not3 = int(liste[3])

    # Ortalama not hesaplama
    son_not = not1 * (3 / 10) + not2 * (3 / 10) + not3 * (4 / 10)

    # Harf notu belirleme
    if son_not >= 90:
        harf = "AA"
    elif son_not >= 85:
        harf = "BA"
    elif son_not >= 80:
        harf = "BB"
    elif son_not >= 75:
        harf = "CB"
    elif son_not >= 70:
        harf = "CC"
    elif son_not >= 65:
        harf = "DC"
    elif son_not >= 60:
        harf = "DD"
    elif son_not >= 55:
        harf = "FD"
    else:
        harf = "FF"

    return isim, harf  # Hem isim hem de harf notunu döndür


# Dosya işlemleri
with open("notlar.txt", "r", encoding="utf-8") as file:
    eklenecekler_listesi = []  # Tüm sonuçları tutacak olan liste.
    aa_listesi = []  # AA olanların listesi
    ba_listesi = []  # BS olanların listesi
    bb_listesi = []  # BB olanların listesi
    cb_listesi = []  # CB olanların listesi
    cc_listesi = []  # CC olanların listesi
    dc_listesi = []  # DC olanların listesi
    dd_listesi = []  # DD olanların listesi
    ff_listesi = []  # DD olanların listesi

    genislik = 20
    for satir in file:
        isim, harf = hesapla(satir)  # hesapla fonksiyonundan hem isim hem harf al
        eklenecekler_listesi.append(f"{isim.ljust(genislik)} -----> {harf}\n")

        if harf == "AA":  # Eğer harf "AA" ise listeye ekle
            aa_listesi.append(f"{isim.ljust(genislik)} -----> {harf}\n")
        elif harf == "BA":
            ba_listesi.append(f"{isim.ljust(genislik)} -----> {harf}\n")
        elif harf == "BB":
            bb_listesi.append(f"{isim.ljust(genislik)} -----> {harf}\n")
        elif harf == "CB":
            cb_listesi.append(f"{isim.ljust(genislik)} -----> {harf}\n")
        elif harf == "CC":
            cc_listesi.append(f"{isim.ljust(genislik)} -----> {harf}\n")
        elif harf == "DC":
            dc_listesi.append(f"{isim.ljust(genislik)} -----> {harf}\n")
        elif harf == "DD":
            dd_listesi.append(f"{isim.ljust(genislik)} -----> {harf}\n")
        elif harf == "FF":
            ff_listesi.append(f"{isim.ljust(genislik)} -----> {harf}\n")

    # Sonuç dosyasını oluşturma
    with open("not_sonuclari.txt", "w", encoding="utf-8") as file2:
        file2.writelines(eklenecekler_listesi)

    # AA alanları ayrı dosyaya yazma
    with open("AA_notu_olanlar.txt", "w", encoding="utf-8") as file3:
        file3.writelines(aa_listesi)

    # BA alanları ayrı dosyaya yazma
    with open("BA_notu_olanlar.txt", "w", encoding="utf-8") as file4:
        file4.writelines(ba_listesi)

    # BB alanları ayrı dosyaya yazma
    with open("BB_notu_olanlar.txt", "w", encoding="utf-8") as file5:
        file5.writelines(bb_listesi)

    # CB alanları ayrı dosyaya yazma
    with open("CB_notu_olanlar.txt", "w", encoding="utf-8") as file6:
        file6.writelines(cb_listesi)

    # CC alanları ayrı dosyaya yazma
    with open("CC_notu_olanlar.txt", "w", encoding="utf-8") as file7:
        file7.writelines(cc_listesi)

    # DC alanları ayrı dosyaya yazma
    with open("DC_notu_olanlar.txt", "w", encoding="utf-8") as file8:
        file8.writelines(dc_listesi)

    # DD alanları ayrı dosyaya yazma
    with open("DD_notu_olanlar.txt", "w", encoding="utf-8") as file9:
        file9.writelines(dd_listesi)

    # FF alanları ayrı dosyaya yazma
    with open("FF_notu_olanlar.txt", "w", encoding="utf-8") as file9:
        file9.writelines(ff_listesi)

print("Notlar hesaplanıyor...")
time.sleep(1)
print("Notlar dosyalar halinde düzenlendi. Dosyaları kontrol edebilirsiniz...")
