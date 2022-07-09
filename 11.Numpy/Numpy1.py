# Numpy veri analizinde kullanılır
# Numpy standart python listelerine göre daha az yer kaplar ve daha hızlı çalışır
# Bundan dolayı büyük verilerde numpy ile çalışılır

# Numpy kütüphanesinin yüklenmesi gerekir
# Aşağıdaki kod ile otomatik yüklenir
# import os
# os.system('cmd /c "py -m pip install numpy"')

import numpy as np

# Python listesi
pyList = [1,2,3,4,5,6,7,8,9]

# Numpy array
npArray = np.array([1,2,3,4,5,6,7,8,9]) # Elemanlar tek tek eklenecek ise parantes içine köşeli parantez açılarak eklenir

print(type(pyList))
print(type(npArray))

pyMulti = [[1,2,3],[4,5,6],[7,8,9]] # Elle oluşturulan 3*3 matris
npMulti = npArray.reshape(3,3) # Kod ile oluşturulan 3*3matris

print(pyMulti)
print(npMulti)

print(npArray.ndim) # Matrisin kaç boyutlu olduğunu gösterir
print(npMulti.ndim)

print(npArray.shape) # Matrisin satır ve sütun sayısını gösterir
print(npMulti.shape)