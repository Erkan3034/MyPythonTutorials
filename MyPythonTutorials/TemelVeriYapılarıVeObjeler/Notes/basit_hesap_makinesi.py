print(" ")
print("************************ WELCOME TO CALCULATOR PROGRAM**********************")

print("""Lütfen yap ak istediğiniz işlemi seçiniz
1. =Toplama 
2. =Çıkarma
3. =Bölme
4. =Çarpma
      """);

print("")
s1 = int(input("Sayı 1  : "))
s2 = int(input("Sayı 2 : "))
islem = int(input("İşlem : "))

if (islem == 1):
    print("------> {} ile {} sayısının toplamı : {} ".format(s1, s2, s1 + s2))
elif (islem == 2):
    print("------> {} ile {} sayısının çıkarma sonucu : {} ".format(s1, s2, abs(s1 - s2)))
elif (islem == 3):
    print("------> {} ile {} sayısının bölmesi : {} ".format(s1, s2, s1 / s2))
elif (islem == 4):
    print("------> {} ile {} sayısının çarpımı : {} ".format(s1, s2, s1 * s2))
else:
    print("Geçersiz işlem!!!")