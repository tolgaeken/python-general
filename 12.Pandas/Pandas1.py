# Pandas veriler üzerinde veri analizi yapmak için kullanılır
# Pandas kütüphanesini kullanmak için yüklemek gerekir

# # Aşağıdaki kod ile otomatik yüklenir
# import os
# os.system('cmd /c "py -m pip install pandas"')

import pandas as pd
import numpy as np

# Data
numbers = [20,35,40,55]
letters = ["a","b","c","d",20,True] # Pandas serilerinde tek veri tipi kullanmak zorunlu değildir
scalar = 5
dict = {"a":10,"b":20,"c":30,"d":40}
randomNumbers = np.random.randint(10,100,6)

# pandasSeries = pd.Series()
# pandasSeries = pd.Series(numbers)
# pandasSeries = pd.Series(letters)
# pandasSeries = pd.Series(scalar, [0,1,2,3]) # Köşeli parantez ile index numarası verilebilir

# Index numaraları sayı olmak zorunda değildir fakat bir liste gönderilirse listenin eleman sayısı kadar key bilgisi gönderilmesi gerekir
pandasSeries = pd.Series(numbers,["a","b","c","d"])

# pandasSeries = pd.Series(dict) # Sözlük değerlerinde key bilgisi otomatik gelir
# pandasSeries = pd.Series(randomNumbers) # Veri olarak Numpy ile kullanılabilir

result = pandasSeries[0] # Elemanın index numarası sayı olmasa bile sıradaki index sırasına göre getirir
result = pandasSeries[-1] # En sondaki elemanı getirir
result = pandasSeries[:2] # İlk 2 elemanı getirir
result = pandasSeries[-2:] # Son 2 elemanı getirir
result = pandasSeries["a"] # Bu şekilde key değeri de gönderilebilir
result = pandasSeries[["a","c"]] # Birden fazla key değeri girilebilir
result = pandasSeries.ndim # Serinin kaç boyutlu olduğunu gösterir
result = pandasSeries.dtype # Serinin veri tipini gösterir
result = pandasSeries.shape # Serinin kaç elemanlı olduğunu gösterir
result = pandasSeries.sum() # Serinin toplamını alır
result = pandasSeries.max() # Serinin en büyük değerini gösterir
result = pandasSeries.min() # Serinin en küçük değerini gösterir
result = pandasSeries + pandasSeries # Seriler bu şekilde toplanabilir
result = pandasSeries + 50 # Serideki her elemana 50 ekler
result = np.sqrt(pandasSeries) # Numpy ile serideki her elemanın karekökünü alır
result = pandasSeries >= 50 # Numpy da olduğu gibi koşullu ifadeler girilebilir
result = pandasSeries % 2 == 0

print(pandasSeries)
print(pandasSeries[result])
print(result)

opel2018 = pd.Series([20,30,40,10],["Astra","Corsa","Mokka","Insignia"])
opel2019 = pd.Series([40,30,20,10],["Astra","Corsa","Grandland","Insignia"])

total = opel2018 + opel2019 # İki serinin toplamı sonucunda sadece birinde olan değerler için NaN (Not a Number) hatası verir
print(total["Astra"]) # Sadece istenen elemanın işlem görmüş değerini getirir