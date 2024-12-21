class Dosya:
    def __init__(self):
        with open("metin.txt" , "r" ,encoding="utf-8") as file:
            dosya_icerigi = file.read() # dosya içeriğini oku.

            # print(dosya_icerigi) # dosya içerini oku.
            kelimeler = dosya_icerigi.split() # tüm kelimeleri boşluğa göre ayır.(listeye atar)
            #print(kelimeler)
            self.sade_kelimler = list()

            for i in kelimeler:
                i = i.strip("\n") # \n'e göre sadeleştir.

                i = i.strip(" ") # boşluk krakterine göre sadeleştir.

                i= i.strip(".") # .'ya  göre sadeleştir.
                i= i.strip(",") # ,'e göre sadeleştir.

                self.sade_kelimler.append(i) #kelimeler tamamen sadeleştirildi.


    def tum_kelimeler(self):
        kelimeler_kumesi = set()

        for i in self.sade_kelimler:
            kelimeler_kumesi.add(i)
        print("Tüm kelimeler...")

        for i in kelimeler_kumesi:
            print(i)

            print("______________________________________")

    def kelime_frekansi(self): # bir kelimenin kaç defa geçtiğini bulalım.
        kelime_sozluk = dict()

        for i in self.sade_kelimler:
            if(i in kelime_sozluk):
                kelime_sozluk[i] += 1
            else:
                kelime_sozluk[i] = 1

        for kelime,sayi in kelime_sozluk.items():
            print(" {} kelimesi {} defa geçiyor...".format(kelime,sayi))
            print("____________________________")



    def kelimeyi_bul(self):
        kelime = input("Kelime: ")

        # Kelimeyi liste içinde arama
        for i, kelime_metni in enumerate(self.sade_kelimler):
            if kelime == kelime_metni:
                print("{} kelimesi metinde var. İndex numarası: {}".format(kelime, i))
                return  # İlk bulduğunda fonksiyonu sonlandır

        print("{} kelimesi metinde bulunamadı.".format(kelime))  # Kelime bulunmazsa mesaj







dosya = Dosya()

dosya.kelimeyi_bul()