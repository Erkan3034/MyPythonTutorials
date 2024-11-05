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

# 3 basamaklı

# Algoritma:
# 1. Kullanıcıdan üç basamaklı bir sayı alın.
# 2. Sayının yüzler basamağını, onlar basamağını ve birler basamağını ayrı ayrı bulun.
# 3. Her bir basamağa karşılık gelen kelimeyi belirleyin.
# 4. Sayının okunuşunu, yüzler, onlar ve birler basamağındaki kelimeleri birleştirerek oluşturun.
# 5. Elde edilen kelimeyi ekrana yazdırın.

# Yüzler, onlar ve birler basamağındaki sayılar için kelime karşılıklarını tanımla
birler = ["", "bir", "iki", "üç", "dört", "beş", "altı", "yedi", "sekiz", "dokuz"]
onlar = ["", "on", "yirmi", "otuz", "kırk", "elli", "altmış", "yetmiş", "seksen", "doksan"]
yuzler = ["", "yüz", "iki yüz", "üç yüz", "dört yüz", "beş yüz", "altı yüz", "yedi yüz", "sekiz yüz", "dokuz yüz"]

# Kullanıcıdan üç basamaklı bir sayı al
sayi = int(input("Üç basamaklı bir sayı girin: "))

# Sayının yüzler, onlar ve birler basamağını bul
yuzler_basamagi = sayi // 100          # Yüzler basamağı
onlar_basamagi = (sayi % 100) // 10     # Onlar basamağı
birler_basamagi = sayi % 10             # Birler basamağı

# Sayının okunuşunu oluştur
okunus = f"{yuzler[yuzler_basamagi]} {onlar[onlar_basamagi]} {birler[birler_basamagi]}"

# Okunuşu ekrana yazdır
print(okunus.strip())  # strip() boşlukları kaldırır

