import math


def toplama(x, y):
    return x + y


def cikarma(x, y):
    return x - y


def carpma(x, y):
    return x * y


def bolme(x, y):
    return x / y


def karekok(x):
    return math.sqrt(x)


def logaritma(x, base=math.e):
    return math.log(x, base)


def sin(x):
    return math.sin(math.radians(x))


def cos(x):
    return math.cos(math.radians(x))


def tan(x):
    return math.tan(math.radians(x))


def hesap_makinesi():
    while True:
        print("\n"
              "******************Hesap Makinesi****************")
        print("1. Toplama")
        print("2. Çıkarma")
        print("3. Çarpma")
        print("4. Bölme")
        print("5. Karekök")
        print("6. Logaritma")
        print("7. Sinüs")
        print("8. Kosinüs")
        print("9. Tanjant")
        print("0. Çıkış")

        secim = input("Bir işlem seçin (0-9): ")

        if secim == '0':
            print("Programdan çıkılıyor...")
            break

        if secim in ['1', '2', '3', '4']:
            x = float(input("Birinci sayıyı girin: "))
            y = float(input("İkinci sayıyı girin: "))

            if secim == '1':
                print(f"{x} + {y} = {toplama(x, y)}")
            elif secim == '2':
                print(f"{x} - {y} = {cikarma(x, y)}")
            elif secim == '3':
                print(f"{x} * {y} = {carpma(x, y)}")
            elif secim == '4':
                print(f"{x} / {y} = {bolme(x, y)}")

        elif secim == '5':
            x = float(input("Karekökünü almak istediğiniz sayıyı girin: "))
            print(f"Karekök({x}) = {karekok(x)}")

        elif secim == '6':
            x = float(input("Logaritmasını almak istediğiniz sayıyı girin: "))
            base = float(input("Logaritmanın tabanını girin (varsayılan e için '0' girin): "))
            if base == 0:
                base = math.e
            print(f"Logaritma({x}) = {logaritma(x, base)}")

        elif secim == '7':
            x = float(input("Sinüsünü almak istediğiniz açıyı girin (derece): "))
            print(f"Sinüs({x}) = {sin(x)}")

        elif secim == '8':
            x = float(input("Kosinüsünü almak istediğiniz açıyı girin (derece): "))
            print(f"Kosinüs({x}) = {cos(x)}")

        elif secim == '9':
            x = float(input("Tanjantını almak istediğiniz açıyı girin (derece): "))
            print(f"Tanjant({x}) = {tan(x)}")

        else:
            print("Geçersiz seçim, lütfen tekrar deneyin.")


if __name__ == "__main__":
    hesap_makinesi()
