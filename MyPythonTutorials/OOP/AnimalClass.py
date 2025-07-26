# Hayvan Sınıfı
class Hayvan:
    def __init__(self, isim, yaş, tür):
        # Hayvan nesnesi oluşturulurken, isim, yaş ve tür özellikleri atanır
        self.isim = isim
        self.yaş = yaş
        self.tür = tür

    def tanıt(self):
        # Hayvan nesnesinin bilgilerini döner
        return f"İsim: {self.isim}, Yaş: {self.yaş}, Tür: {self.tür}"

# Köpek Sınıfı
class Kopek(Hayvan):
    def __init__(self, isim, yaş, tür, cins):
        # Üst sınıfın __init__ metodunu çağırarak isim, yaş ve tür özelliklerini atar
        super().__init__(isim, yaş, tür)
        # Köpek sınıfına özgü ek özellik: cins
        self.cins = cins

    def havla(self):
        # Köpek nesnesinin havlamasını sağlar
        return "Hav! Hav!"

    def tanıt(self):
        # Üst sınıfın tanıt metodunu çağırarak temel bilgileri alır ve cinsi ekler
        temel_tanıtım = super().tanıt()
        return f"{temel_tanıtım}, Cins: {self.cins}"

# Kuş Sınıfı
class Kus(Hayvan):
    def __init__(self, isim, yaş, tür, kanat_uzunluğu):
        # Üst sınıfın __init__ metodunu çağırarak isim, yaş ve tür özelliklerini atar
        super().__init__(isim, yaş, tür)
        # Kuş sınıfına özgü ek özellik: kanat uzunluğu
        self.kanat_uzunluğu = kanat_uzunluğu

    def ucur(self):
        # Kuş nesnesinin uçmasını sağlar
        return "Uçuyor!"

    def tanıt(self):
        # Üst sınıfın tanıt metodunu çağırarak temel bilgileri alır ve kanat uzunluğunu ekler
        temel_tanıtım = super().tanıt()
        return f"{temel_tanıtım}, Kanat Uzunluğu: {self.kanat_uzunluğu} cm"

# At Sınıfı
class At(Hayvan):
    def __init__(self, isim, yaş, tür, yarış_atı_mı):
        # Üst sınıfın __init__ metodunu çağırarak isim, yaş ve tür özelliklerini atar
        super().__init__(isim, yaş, tür)
        # At sınıfına özgü ek özellik: yarış atı mı
        self.yarış_atı_mı = yarış_atı_mı

    def kos(self):
        # At nesnesinin koşmasını sağlar
        return "Koşuyor!"

    def tanıt(self):
        # Üst sınıfın tanıt metodunu çağırarak temel bilgileri alır ve yarış atı olup olmadığını ekler
        temel_tanıtım = super().tanıt()
        yarış_atı = "Evet" if self.yarış_atı_mı else "Hayır"
        return f"{temel_tanıtım}, Yarış Atı mı: {yarış_atı}"

# Sınıfları kullanma
# Köpek sınıfından bir nesne oluşturma
kopek = Kopek("Karabaş", 5, "Köpek", "Labrador") #ozellkler burdan atanır
# Kuş sınıfından bir nesne oluşturma
kus = Kus("Maviş", 2, "Kuş", 25)
# At sınıfından bir nesne oluşturma
at = At("Rüzgar", 3, "At", True)

# Köpek nesnesinin tanıtımını ve havlamasını yazdırma
print(kopek.tanıt())  # İsim: Karabaş, Yaş: 5, Tür: Köpek, Cins: Labrador
print(kopek.havla())  # Hav! Hav!

# Kuş nesnesinin tanıtımını ve uçmasını yazdırma
print(kus.tanıt())    # İsim: Maviş, Yaş: 2, Tür: Kuş, Kanat Uzunluğu: 25 cm
print(kus.ucur())     # Uçuyor!

# At nesnesinin tanıtımını ve koşmasını yazdırma
print(at.tanıt())     # İsim: Rüzgar, Yaş: 3, Tür: At, Yarış Atı mı: Evet
print(at.kos())       # Koşuyor!
