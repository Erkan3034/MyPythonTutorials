import requests

from bs4 import  BeautifulSoup

url = "https://yellowpages.com.tr/ara?q=Ankara"
response = requests.get(url) #isteği getir.

html_icerigi = response.content #cevaptaki içeriği al.

soup = BeautifulSoup(html_icerigi,"html.parser") #beautifulsoup ile içeriği parse et.

for i in soup.find_all("a"): #soup içerisindeki tüm a etiketlerini bul.
    print(i.get("href")) #a etiketlerinin href değerlerini al.
    print(i.text) #a

print("==========================================================================")
print(soup.prettify()) # tüm içeriği düzgün şekilde alır.






