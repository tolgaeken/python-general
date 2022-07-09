# DataFrameler ile çalışma
import pandas as pd
from numpy.random import randn

dataFrame = pd.DataFrame(randn(3,3),index=["A","B","C"],columns=["Column1","Column2","Column3"])

result = dataFrame["Column1"] # Sadece "Column1" kolonunu liteler
result = type(dataFrame)
result = dataFrame[["Column1","Column2"]] # birden fazla kolon listelemek için iç içe listeleme kullanılır
result = dataFrame.loc["A"] # Satır seçmek için key değeri girilir
result = type(result)
result = dataFrame.loc[["A","B"]] # Birden fazla key değerini listelemek için iç içe listeleme kullanılır
result = dataFrame.loc["A","Column2"] # Tek değer getirmek için satır ve sütun değerleri girilir
result = dataFrame.loc[:,"Column3"] # Kolona göre seçim yapılır
result = dataFrame.loc[:,["Column2","Column3"]] # İstenen kolonlar tek tek girilir
result = dataFrame.loc[:,"Column1":"Column3"] # Belirli bir aralıktaki kolonları getirir ve bu durumda köşeli parantez kullanılmaz
result = dataFrame.loc[:,:"Column2"] # "Column2" ve ondan önceki kolonlar getirilir
result = dataFrame.loc["A":"B",:"Column2"]
# result = dataFrame.loc[0:1,:"Column2"] # Index numaraları verilmediği durumda bu şekilde kullanılır
result = dataFrame.loc["B":,:"Column2"] # "B" satırı ve sonrasını, ayrıca "Column2" sütunu ve öncesindeki verileri getirir

result = dataFrame.iloc[2] # Index numaraları verildiği durumda numaraya göre arama yapar
result = dataFrame.iloc[1,1]

dataFrame["Column4"] = pd.Series(randn(3),["A","B","C"]) # Kolon ekler
result = dataFrame

dataFrame["Column5"] = dataFrame["Column1"] + dataFrame["Column3"] # Kolonlar arası işlem yapma
result = dataFrame

dataFrame.drop("Column5",axis = 1,inplace= True) # Kolon siler fakat "axis" ile eksen seçilmesi gerekir(1 = Dikey, 0 = Yatay)
# inplace=true ile dataframe kolon silindikten sonra güncelleme yapar, false olduğu taktirde kopyasını çıkartır
result = dataFrame

result = dataFrame.loc[:,:"Column2"]

print(result)