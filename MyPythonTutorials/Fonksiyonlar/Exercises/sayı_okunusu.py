def sayiOkunus(sayi):
    onlar = ["", "On", "Yirmi", "Otuz", "Kırk", "Elli", "Altmış", "Yetmiş", "Seksen", "Doksan"]
    birler = ["", "Bir", "İki", "Üç", "Dört", "Beş", "Altı", "Yedi", "Sekiz", "Dokuz"]

    onlar_basamagi = sayi // 10
    birler_basamagi = sayi % 10

    return (f"{onlar[onlar_basamagi]} {birler[birler_basamagi]}").strip()


# Kullanıcıdan sayı alımı ve fonksiyonun çağrılması
while True:
    sayi = input("İki basamaklı bir sayı giriniz (Çıkmak için 'q' tuşlayın): ")

    if sayi == "q":
        print("Program sonlandırıldı!")
        break

    try:
        sayi = int(sayi)
        if 10 <= sayi <= 99:
            print(f"{sayi} -----> {sayiOkunus(sayi)}")
        else:
            print("Lütfen iki basamaklı bir sayı giriniz.")
    except ValueError:
        print("Hatalı giriş! Lütfen bir sayı giriniz.")
