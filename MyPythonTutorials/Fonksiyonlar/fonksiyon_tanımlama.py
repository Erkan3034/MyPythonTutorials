def merhaba():
    print("Merhaba, dünya!")
merhaba() # fonk çağırma

print("--------------------------------------------")


def selamla(isim):
    print(f"Merhaba, {isim}!")

#çağırma

selamla("ERKAN")

print("--------------------------------------------")


def topla(a, b):
    return a + b

sonuc = topla(318, 515) #çağırma
print("Sonuç : ",sonuc)

print("--------------------------------------------")


Topla = lambda x, y: x + y # x ve y'nin toplamını tut.

print(Topla(2, 3))  # Çıktı: 5



Carp = lambda a,b,c : (a+b)*c

print(Carp(2,3,4))


print("-------------------------------------")


cıkar = lambda k,l : abs(k-l)

print(cıkar(5,10))


print("--------------------------------------------")

 #-------------------------->Bir Fonksiyon Kütüphanesi
   #Aşağıda, birkaç fonksiyonu bir araya getiren basit bir kütüphane örneğği


def faktoriyel(n):
    if n == 0:
        return 1
    else:
        return n * faktoriyel(n - 1)

def kare_al(x):
    return x ** 2

# Fonksiyonları kullanma
print(faktoriyel(5))  # Çıktı 120
print(kare_al(4))     # Çıktı 16


print("--------------------------------------------")

def toplama(*parametreler): # Artık parametreler değişkenini bir demet gibi kullanabiliriz. (Metot overloading) istenilen mikatrda parametre işlem yapılır.
    toplam =  0
    print("Parametreler:",parametreler)
    for i in parametreler:
        toplam += i
    return toplam

print(toplama(1,2,3,4,5,6,7,8,9)) # 1. parametre sayısı

print(toplama(10,20,30))    #2. paramaetre sayısı

print(toplama(2,8,9,7,5,78,95))



print("--------------------------------------------")


#burda genel bir değişken tanımladığımız için değişken programın her yerinden erişileblir olacaktır.

b= 15

def function():
    print(f"Usage global variable 'b' in function : {b**2}")
function()

def function2():
    print(f"Usage global varianle 'b' in function2 :  + {(b*b) + (b**2)}")
function2()