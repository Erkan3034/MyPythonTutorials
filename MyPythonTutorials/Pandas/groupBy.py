
import pandas as pd
# Örnek veri seti
data = {
    'Sehir': ['İstanbul', 'Ankara', 'İstanbul', 'Ankara', 'İzmir'],
    'Nüfus': [15, 5, 16, 6, 4],
    'Bölge': ['Marmara', 'İç Anadolu', 'Marmara', 'İç Anadolu', 'Ege']
}

dataframe = pd.DataFrame(data)

# Şehirlere göre gruplama
grouped = dataframe.groupby('Sehir')
print(grouped)


print(dataframe.columns)
print(dataframe.columns.tolist())

# Nüfusu şehir bazında toplama
if 'Sehir' in dataframe.columns:
    toplam_nufus = dataframe.groupby('Sehir')['Nüfus'].sum()
    print(toplam_nufus)
else:
    print("Sehir sütunu bulunamadı!")


# Şehir bazında toplam nüfusu 10'dan büyük olanlar
filtreli = dataframe.groupby('Sehir')['Nüfus'].sum().loc[lambda x: x > 10]
print(filtreli)


# Hem toplam hem de ortalama alalım
sonuc = dataframe.groupby('Sehir')['Nüfus'].agg(['sum', 'mean'])
print(sonuc)
