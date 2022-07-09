# Pandas dataframe fonksiyonları
import pandas as pd
import numpy as np

def kareAl(x):
    return x*x

kareAl2 = lambda x: x*x

data = {
    "Column1":[1,2,3,4,5],
    "Column2":[10,20,13,20,25],
    "Column3":["abc","bcaa","ade","cb","dea"]
}

dataFrame = pd.DataFrame(data)

result = dataFrame["Column2"].unique() # "Column2" kolonunda tekrarlanmayan değerleri getirir
result = dataFrame["Column2"].nunique() # "Column2" kolonunda tekrarlanmayan değerlerin saysını getirir
result = dataFrame["Column2"].value_counts() # "Column2" kolonunda her elemanın kaç kere tekrar ettiğini gösterir
result = dataFrame["Column1"] * 2 # "Column1" kolonundaki değerleri 2'ye çarpılır
result = dataFrame["Column1"].apply(kareAl) # "Column1" kolonundaki değerlerin karesini alır
result = dataFrame["Column1"].apply(kareAl2) # Alternatif
result = dataFrame["Column1"].apply(lambda x: x*x) # Alternatif
dataFrame["Column4"] = dataFrame["Column3"].apply(len) # "Column3" kolonunda her kaydın uzunluğunu yeni bir kolona atar
result = dataFrame.columns # Kolon bilgilerini gösterir
result = len(dataFrame.columns) # Kolon sayısını getirir
result = dataFrame.index # Index bilgilerini getirir
result = len(dataFrame.index) # Index sayısını getirir
result = dataFrame.info # Tablo bilgilerinin verir
result = dataFrame.sort_values("Column2") # "Column2" kolonuna göre sıralı gelir
result = dataFrame.sort_values("Column3") # "Column3" kolonuna göre sıralı gelir
result = dataFrame.sort_values("Column3", ascending = False) # "Column3" kolonuna göre azalan şekilde gelir (varsayılan değeri True, yani artandır)

data2 = {
    "Ay": ["Mayıs","Haziran","Nisan","Mayıs","Haziran","Nisan","Mayıs","Haziran","Nisan"],
    "Kategori": ["Elektronik","Elektronik","Elektronik","Kitap","Kitap","Kitap","Giyim","Giyim","Giyim"],
    "Gelir": [20,30,15,14,32,42,12,36,52]
}

dataFrame2 = pd.DataFrame(data2)
dataFrame2 = dataFrame2.pivot_table(index="Ay",columns="Kategori",values="Gelir") # İsteğe göre satır ve sütunları özel bir tablo olarak listeler
print(dataFrame2)