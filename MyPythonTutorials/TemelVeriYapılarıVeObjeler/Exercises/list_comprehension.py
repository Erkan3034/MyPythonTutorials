# Example - 1 ===========================================================

print("List comprehesnion ile olşturulan listeden sadece çift sayıları alan program ")
print()
liste = [x for x in range(1, 101) if x % 2 == 0]

flat_list = liste[:]  # alternatif kullanım.
print(flat_list)

print(liste)

# Example - 2 ===========================================================

list4 = "erkan"
new = list4.replace("erkan", "serkan")
print(new)
print("---------------")

# Example - 3 =======================================================

liste = [[1, 2, 3], [4, 5, 6, 7, 8], [9, 10, 11, 12, 13, 14, 15]]
liste2 = [x for i in liste for x in i]  # Doğru kullanım
print(liste2)
print()


# Example - 4 =======================================================
# İki boyutlu diziyi düzleştirme.

two_dimensions_list = [[1, 2, 3], [10, 20, 30], [5, 15, 25]]

flattened_list = [eleman for liste in two_dimensions_list for eleman in liste] # liste = iki boyutlu liste içindeki her liste, eleman = liste içindeki eleman.
print("Flattened List : " , flattened_list)

   #düzleştirilmilş_liste = [ a  for b in two_dimensions_list for a in b]
   #print("düz liste : ",düzleştirilmilş_liste)
# Example - 5 =======================================================

numbers = range(10)
even_odd = ["çift" if x % 2 == 0 else "tek" for x in numbers]
print(*range(10) ,"= ",  even_odd)  # Çıktı: ['çift', 'tek', 'çift', 'tek', ...]

# Example - 6 =======================================================


numbers = [1, 2, 2,4, 3,3 , 4, 5, 6, 6, 7, 8, 8, 9]
unique_numbers = set([x for x in numbers])
print(unique_numbers)
# Çıktı: [1, 2, 3, 4, 5, 6, 7, 8, 9]
