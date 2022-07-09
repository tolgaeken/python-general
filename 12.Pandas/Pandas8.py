# Pandas kayıp ve bozuk veriler
import pandas as pd
import numpy as np

data = np.random.randint(10,100,15).reshape(5,3)

dataFrame = pd.DataFrame(data,index=["a","c","e","f","h"],columns=["Column1","Column2","Column3"])

dataFrame = dataFrame.reindex(["a","b","c","d","e","f","g","h"]) # Yeniden Index sıralaması yapar fakat ilk defa key bilgisi verilen değerler NaN (Not a Number,boş) olarak gelir

result = dataFrame.drop("Column1",axis = 1) # Kolonu siler fakat kod satır bazlı çalıştığı için axis değerini 1 olarak vermek gerekir (Varsayılan 0'dır)
result = dataFrame.drop(["Column1","Column2"],axis = 1)
result = dataFrame.drop("a",axis = 0) # Veriyi (satırı) siler
result = dataFrame.drop(["a","b","h"],axis = 0)
result = dataFrame.isnull() # Boş olanları true, dolu olanları false olarak getirir
result = dataFrame.notnull() # Dolu olanları true, boş olanları false olarak getirir
result = dataFrame.isnull().sum() # Boş olanların toplamını kolona göre sayarak listeler
result = dataFrame["Column1"].isnull().sum() # Sadece Column1 kolonundaki boş değerleri sayar

newColumn = [np.nan,30,np.nan,51,np.nan,30,np.nan,10] # "np.nan" ile boş değer atanır
dataFrame["Column4"] = newColumn

result = dataFrame[dataFrame["Column1"].isnull()] # Column1 kolonunda boş olanları getirir
result = dataFrame[dataFrame["Column1"].isnull()]["Column1"] # Column1 kolonunda boş olanları getirir ve sadece Column1 kolonunu getirir
result = dataFrame[dataFrame["Column1"].notnull()]["Column1"]
result = dataFrame.dropna() # Satır içinde en az 1 tane boş değer varsa o satırı tamamen siler
result = dataFrame.dropna(axis = 1) # Sütun içinde en az 1 tane boş değer varsa o sütunu tamamen siler
result = dataFrame.dropna(how = "any") # Satır içinde en az 1 tane boş değer varsa o satırı tamamen siler
result = dataFrame.dropna(how = "all") # Satır tamamen boş ise o satırı siler
result = dataFrame.dropna(subset = ["Column1","Column2"],how = "all") # Subset ile hangi kolon ya da kolonlarda boş değer olduğu aranır ve "all" ise verilen kolonların hepsi boş ise o satır tamamen silinir
result = dataFrame.dropna(subset = ["Column1","Column2"],how = "any") # "any" ile de verilen kolonlardan herhangi biri boş ise o satır tamamen silinir
result = dataFrame.dropna(thresh = 3) # "thresh" ile verilen değerde, yani en az 3 tane dolu kayıt varsa o satırı silmez
result = dataFrame.fillna(value = "No Input") # Boş olan değerleri value ile verilen değer ile doldurur
result = dataFrame.fillna(value = 1)

def ortalama(dfr):
    # toplam = dfr.sum() # Tablodaki tüm değerlerin kolon bazlı toplamını getirir
    toplam = dfr.sum().sum() # Kolonlarda toplanan sayıları da ayrıca toplar
    adet = dfr.size - dfr.isnull().sum().sum() # size ile tablodaki toplam eleman sayısını getirir, toplam boş değerlerin sayılıp tüm tablodan çıkarılır
    return toplam/adet

result = dataFrame.fillna(value = ortalama(dataFrame)) # "ortalama" metodu ile alınan ortalamaları boş değerlere yerleştirir

print(result)