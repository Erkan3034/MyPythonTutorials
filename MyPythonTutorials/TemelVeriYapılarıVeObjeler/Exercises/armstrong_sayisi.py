print("""
***************************************************************************************************************
Örnek olarak, Bir sayı eğer 4 basamaklı ise ve oluşturan rakamlardan herbirinin 
4. kuvvetinin toplamı( 3 basamaklı sayılar için 3.kuvveti ) o sayıya eşitse bu sayıya "Armstrong" sayısı denir.
***************************************************************************************************************

   Örnek olarak : 1634 = 1^4 + 6^4 + 3^4 + 4^4
""")

#region ALGORİTMA
# 1. Kullanıcıdan bir sayı al.
# 2. Sayının basamak sayısını bul.
# 3. Sayının her basamağını sırayla al ve basamak sayısı kadar üssünü hesapla.
# 4. Hesapladığın üssü bir toplam değişkenine ekle.
# 5. Tüm basamaklar için işlemi tekrarla.
# 6. Son olarak, toplam sayıya eşit mi kontrol et:
#     - Eşitse, bu bir Armstrong sayısıdır.
#     - Eşit değilse, Armstrong sayısı değildir.

#endregion

while True: #işlem iptal edilmediği sürece sistem çalışsın
    sayi = int(input("Kontrol etmek istediğiiniz sayıyı giriniz(Çıkmak için 0 girin ): "))

    if sayi == 0:
        print("Program sonlandırıldı !")
        break


    basamak_sayisi = len(str(sayi)) #sayının basamak sayısı


    gecici_sayı = sayi  # geçici sayı tanımlıyoruz, işlemlerimiz burda gerçekleşecek.

    # Toplamı tutacak değişkeni başlatıyoruz
    toplam = 0

    # Sayının her basamağını sırayla alacağız
    while (gecici_sayı > 0):

        basamak = gecici_sayı % 10  # Son basamak

        # Bulduğumuz basamağın basamak sayısı kadar üssünü alıp toplama ekliyoruz
        toplam += basamak ** basamak_sayisi

        # Son basamağı attığımız için geçici sayı 10'a bölünerek küçültülür
        gecici_sayı //= 10

    if toplam == sayi:
        print(f"{sayi} bir Armstrong sayısıdır.")
    else:
        print(f"{sayi} bir Armstrong sayısı değildir.")