print("""*************************************************************************************
Bir sayının kendisi hariç bölenlerinin toplamı kendine eşitse 
bu sayıya "mükemmel sayı" denir. Örnek olarak, 6 mükemmel bir sayıdır. (1 + 2 + 3 = 6)
**************************************************************************************
""")

while True:   # işlem iptal edilmdiği sürece program çalışsın.
    sayi = int(input("Lütfen kontrol etmek istediğiniz sayıyı giriniz (Çıkmak için 0 girin): "))

    if sayi == 0:
        print("İşlem iptal edildi...")
        break  # Kullanıcı 0 girerse döngü sonlanır

    bölen = 1  # bölenleri kontrol etmek için başlangıç değeri
    toplam = 0  # bölenlerin toplamı

    while bölen < sayi:
        if sayi % bölen == 0:
            toplam += bölen
        bölen += 1

    if toplam == sayi:
        print(f"{sayi} sayısı mükemmel bir sayıdır.")
    else:
        print(f"{sayi} sayısı mükemmel bir sayı değildir.")
