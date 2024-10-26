print("  ")
print("**********************************OYUNCU KAYDETME SİSTEMİ****************")

ad=input("Oyuncu ismini giriniz: ")
soyad=input("Oyuncunun soyadını giriniz: ")
takim=input("Oyuncunun bulunacağı takımı yazınız: ")

bilgiler=[ad,soyad,takim] #bilgileri bir listeye kaydedelim

print("----------------Bilgiler kaydediliyor...")

print(" Oyuncu ismi: {}\n Oyuncu Soyadı: {}\n Oyuncunun takımı: {}".format(bilgiler[0],bilgiler[1],bilgiler[2]))

print("Bilgiler kaydedildi...")