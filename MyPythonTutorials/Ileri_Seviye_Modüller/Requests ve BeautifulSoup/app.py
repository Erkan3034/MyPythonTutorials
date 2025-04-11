"""
import requests
from bs4 import BeautifulSoup

# Hedef URL
url = "https://yellowpages.com.tr/ara?q=Ankara"

# Tarayıcı gibi gözükmek için User-Agent ekleyelim
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
}

# HTTP isteği gönder
response = requests.get(url, headers=headers)

# Sayfa içeriğini al
html_icerigi = response.content

# Sayfa kaynak kodunu ekrana yazdır (DEBUG için)
print("\n💡 Sayfa Kaynağı (İlk 500 Karakter):\n", html_icerigi[:500].decode('utf-8', 'ignore'))

# BeautifulSoup ile HTML içeriğini işle
soup = BeautifulSoup(html_icerigi, "html.parser")

# Class değeri "yp-poi-box-2" olan div'leri bul
divler = soup.find_all("div", class_="yp-poi-box-2")

# Eğer veri varsa yazdır
if divler:
    for i, div in enumerate(divler, start=1):
        print(f"\n📌 {i}. Bulunan Kayıt:")
        print(div.text.strip())  # Sadece içeriği göster
else:
    print("\n❌ Veri bulunamadı veya site botları engelliyor.")
"""
"""
import requests

from bs4 import  BeautifulSoup

url = "https://yellowpages.com.tr/ara?q=Ankara"
response = requests.get(url)

html_icerigi = response.content

soup = BeautifulSoup(html_icerigi,"html.parser")


print(soup.find_all("div",{"class":"yp-poi-box-2"}))

"""

import requests

from bs4 import BeautifulSoup

url = "http://www.imdb.com/chart/top"

response = requests.get(url)

html_icerigi = response.content

soup = BeautifulSoup(html_icerigi,"html.parser")

a = float(input("Rating'i giriniz:"))


basliklar = soup.find_all("td",{"class":"titleColumn"})
ratingler = soup.find_all("td",{"class","ratingColumn imdbRating"})




for baslik, rating in zip(basliklar,ratingler):
    baslik = baslik.text
    rating = rating.text

    baslik = baslik.strip()
    baslik = baslik.replace("\n","")

    rating = rating.strip()
    rating = rating.replace("\n","")

    if (float(rating) > a):
        print("Film ismi: {} Filmin Ratingi : {}".format(baslik,rating))








