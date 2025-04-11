import querystring
import requests

url = "https://data.fixer.io/api/latest?access_key=72831fc02fb34437c7c07d86cd93f6bd"

#querystring = {"from":"USD","to":"INR","amount":100,"date":"1999-08-14"}

first_currency = input("Birinci Para Birimi:") # Örnek : USD
second_currency = input("İkinci Para Birimi:") # Örnek : TRY
amount = int(input("Miktar:")) # Örnek: 15
response = requests.get(url, params=querystring)

infos= response.json()
firstValue = infos["rates"][first_currency]
secondValue = infos["rates"][second_currency]

print((secondValue / firstValue) * amount)
