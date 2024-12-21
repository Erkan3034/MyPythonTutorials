#pythonda kendi szölüğünü yapmak.
sozluk ={
    "apple":"elma",
    "banana":"muz",
    "cherry":"kiraz"
}

kelime=input("Çevirmek istediğiz kelime(eng): ")
print("Türkçe karşılığı: ",sozluk.get(kelime,"Bu kelime sözlükte yok!"))



#=======================================================================================================================
class Employee:
    def __init__(self,isim,soyisim,bolum): #constructor
        self.isim = isim
        self.soyisim = soyisim
        self.bolum = bolum

    def bilgileriGetir(self):
        print("""
    İsim: {}
    Soyisim: {}
    Bölüm: {}
        """.format(self.isim,self.soyisim,self.bolum))


employee =  Employee("Erkan","Turgut","Yazılım")
employee.bilgileriGetir()
#=======================================================================================================================