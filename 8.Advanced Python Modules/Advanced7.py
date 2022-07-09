# Güncel Dövüz Kuru Çevirme

import requests
import json

apiUrl = "https://api.exchangerate.host/latest"

bozulanDoviz = input("Bozulacak döviz türünü seçiniz\n")
alinanDoviz = input("Alınacak döviz türünü seçiniz\n")
miktar = input(f"{bozulanDoviz} türünden bozdurmak istediğiniz miktarı giriniz\n")
miktar = float(miktar)

result = requests.get(apiUrl+"?base="+bozulanDoviz)
result = json.loads(result.text)

print(f"1 {bozulanDoviz} = {result['rates'][alinanDoviz]} {alinanDoviz}")
print(f"{miktar} {bozulanDoviz} = {miktar * result['rates'][alinanDoviz]} {alinanDoviz}")