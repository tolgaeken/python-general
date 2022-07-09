# Pandas Dataframe filtreleme
import pandas as pd
import numpy as np

data = np.random.randint(10,100,75).reshape(15,5)
dataFrame = pd.DataFrame(data,columns=["Column1","Column2","Column3","Column4","Column5"])

result = dataFrame.columns # Kolonları listeler
result = dataFrame.head() # İlk 5 satırı listeler (Parametre girilmezse varsayılan 5'tir)
result = dataFrame.head(10)
result = dataFrame.head(-3) # Son 3 satır haric tüm verileri listeler
result = dataFrame.tail() # Son 5 satırı listeler (Parametre girilmezse varsayılan 5'tir)
result = dataFrame.tail(4) # Son 4 satırı listeler
result = dataFrame["Column1"].head() # Sadece "Column1" kolonundan ilk 5 satırı listeler
result = dataFrame.Column1.head() # Alternatif
result = dataFrame[["Column1","Column3"]] # Sadece "Column1" ve "Column3" kolonlarındaki değerleri getirir
result = dataFrame[["Column1","Column3"]].head() # Sadece "Column1" ve "Column3" kolonlarından ilk 5 satırı getirir
result = dataFrame[5:12][["Column1","Column2"]] # 5 ile 12. Satır arasındaki ilk 2 kolondaki verileri listeler
result = dataFrame[5:12][["Column1","Column2"]].head() # 5. Satırdan itibaren ilk 5 kaydı getirir

result = dataFrame > 50 # Sadece 50 den büyük olan verileri True ya da False olarak döndürür
result = dataFrame[dataFrame > 50] # Verilen şarta göre filtreleme yapar
result = dataFrame[dataFrame % 2 == 0]
result = dataFrame["Column1"]  > 50 # Sadece girilen kolona göre şart kullanılır fakat bu şekilde değerleri getirmez
result = dataFrame[dataFrame["Column1"]  > 50] # Şarta uygun şekilde tüm kolonları listeler
result = dataFrame[dataFrame["Column1"]  > 50][["Column1","Column2"]] # Verilen şarta göre istenen kolonları listeler
result = dataFrame[(dataFrame["Column1"]  > 50) & (dataFrame["Column1"] < 70)][["Column1","Column2"]] # "Ve" operatörü kullanımı
result = dataFrame[(dataFrame["Column1"]  > 50) & (dataFrame["Column2"] < 50)]
result = dataFrame[(dataFrame["Column1"]  > 50) | (dataFrame["Column2"] < 50)] # "Veya" operatörü kullanımı
result = dataFrame.query("Column1 >= 50 & Column1 % 2 == 0")[["Column1","Column2"]] # Query ile koşul belirleme
result = dataFrame.query("Column1 >= 50 | Column1 % 2 == 0")

print(result)