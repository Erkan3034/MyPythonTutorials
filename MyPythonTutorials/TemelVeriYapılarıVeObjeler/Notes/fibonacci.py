"""
Fibonacci Serisi yeni bir sayıyı önceki iki sayının toplamı şeklinde oluşturur.

1,1,2,3,5,8,13,21,34...............
"""
ilk_sayı = 1

ikincisayi = 1

fibonacci = [ilk_sayı,ikincisayi]
for i in range(20):


    ilk_sayı,ikincisayi = ikincisayi,ilk_sayı + ikincisayi  # a,b=b,a mantığıyla ikinci_sayi = yeni eleman(ilksayi+ikinc,sayi) olur

    fibonacci.append(ikincisayi)

print(fibonacci)
