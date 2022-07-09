# Numpy dizilerinin indekslenmesi
import numpy as np

# numbers = np.array([0,5,10,15,20,25,50,75])

# result = numbers[5]
# result = numbers[-1]
# result = numbers[0:3]
# result = numbers[:3]
# result = numbers[3:]
# result = numbers[::]
# result = numbers[::-1]
# result = numbers[::-2]
# print(result)

# numbers2 = np.array([[0,5,10],[15,20,25],[50,75,85]])
# result = numbers2[2] # İlk boyuttan tüm diziyi getirir
# result = numbers2[0,2] # İki boyutlu diziden eleman getirir
# result = numbers2[:,2] # ":" konulan yerdeki tüm satır ve sütunları getirir. Bu örnekte tüm satırların 2. indeksindeki elemanları getirir
# result = numbers2[:,0:2] # Tüm satırların ilk iki elemanından yeni matris oluşturur
# result = numbers2[-1,:] # son satırı alır
# result = numbers2[:2,:2] # İlk iki satırın ilk iki sütununu alır

# print(result)

arr1 = np.arange(0,10)
# arr2 = arr1 # Referans tiplidir. Bellek üzerinde aynı adreste tutulur. Birinde yapılan değişiklik diğerini de etkiler
arr2 = arr1.copy() # Bu durumda referans bağlantısı kalmaz ve bellek üzerinde farklı adreslerde tutulur

arr2[0] = 20


print(arr1)
print(arr2)