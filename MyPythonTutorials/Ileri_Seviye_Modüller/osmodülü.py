import os
from datetime import datetime

"""
for klasör_yolu,klasör_isimleri,dosya_isimler  in os.walk("C:/Users/user/Desktop"):
    for i in klasör_isimleri:
        if (i.startswith("kr")):
            print(i)

"""





#from datetime import datetime

# print(dir(os)) #os modülünün fonksiyonlarını bastırır.

# print(os.getcwd()) #Dizin yolunu yazdırma

# os.chdir("C:/Users/user/Desktop/") # Dizin değiştirme


# print(os.getcwd())


# print(os.listdir()) #dizindeki dosyaları listele/yazdır

#os.mkdir("Deneme1") #klasör oluştur

#os.makedirs("Deneme2/Deneme3") #klasörleri oluştur(iç içe)

#os.rmdir("Deneme2/Deneme3") # deneme2 klasöründe bulunan Deneme3 klasörünü siler.

# os.rename("Deneme1","Deneme2")
# os.removedirs("Deneme2/Deneme3") #klasörleri kaldır(hepsini)

# os.rename("test.txt","test2.txt")

# print(os.stat("test2.txt")) #dosya özelliklerini yazdırır

# degistirilme = os.stat("test2.txt").st_mtime

# print(datetime.fromtimestamp(degistirilme))


"""
for klasör_yolu,klasör_isimleri,dosya_isimleri in os.walk("C:/Users/ERKAN TURGUT"): #dosyayı dolaşıp her dizini, okur


         print("Current Path",klasör_yolu)
         print("Directories",klasör_isimleri)
         print("Dosyalar",dosya_isimleri)
         print("**********************************")

"""
for klasör,klasör_isimleri,dosya_isimleri in os.walk("C:/Users/ERKAN TURGUT"):

    for i in dosya_isimleri:
        if i.lower().endswith('.png'):
            print(i)




