# Numpy dizileri ile çalışma
import numpy as np

# result = np.array([1,3,5,7,9])
# result = np.arange(1,10) # 1 ile 10 arasında bir dizi oluşturur fakat dizinin ilk elemanı dahil olmakla birlikte son elemanı dahil olmaz
# result = np.arange(10,100,3) # Üçüncü parametre artış miktarını belirtir
# result = np.zeros(10) # Sıfırlardan oluşan 10 elemanlı array oluşturur (float değere sahiptir)
# result = np.ones(10) # Birlerden oluşan 10 elemanlı array oluşturur (float değere sahiptir)
# result = np.linspace(0,100,5) # 0 ile 100 arasındaki 5 eşit parçaya bölerek liste oluşturur (float değere sahiptir)
# result = np.linspace(0,5,5)
# result = np.random.randint(0,10) # Rastgele saı üretir fakat ikinci değeri almaz
# result = np.random.randint(20) # 0 ile 19 arasında sayı üretir
# result = np.random.randint(1,10,3) # Üçüncü parametre kaç tane sayı gösterileeğini belirtir
# result = np.random.rand(5) # 0 ile 1 arasında 5 adet sayı üretir
# result = np.random.randn(5) # -1 ile +1 arasında 5 adet sayı üretir
# print(result)

# npArray = np.arange(50)
# npMulti = npArray.reshape(5,10) # 0 dan 50 ye kadar olan sayılardan 5 satır 10 sütunluk bir matris oluşturur
# print(npMulti.sum(axis = 0)) # Satırların toplamını belirtir
# print(npMulti.sum(axis = 1)) # Sütunların toplamını belirtir

rndNumbers = np.random.randint(1,100,10)
result = rndNumbers.max() # Liste içindeki en büyük sayıyı getirir
result = rndNumbers.min() # Liste içindeki en küçük sayıyı getirir
result = rndNumbers.mean() # Liste içindeki sayıların ortalamasını getirir
result = rndNumbers.argmax() # Liste içindeki en büyük sayının index numarasını getirir
result = rndNumbers.argmin() # Liste içindeki en küçük sayının index numarasını getirir
print(result)