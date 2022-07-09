# Numpy dizi operasyonları
import numpy as np

numbers1 = np.random.randint(10,100,6)
numbers2 = np.random.randint(10,100,6)

print(numbers1)
# print(numbers2)

# result = numbers1 + numbers2 # Eğer dizi eleman sayısı aynı ise aynı indekste olan elemanlar ile matematiksel operatör işlemleri yapılabilir
# result = numbers1 + 10 # Dizinin her elemanına 10 ekler
# result = numbers1 - numbers2
# result = numbers1 - 10
# result = numbers1 * numbers2
# result = numbers1 * 10
# result = numbers1 / numbers2
# result = numbers1 / 10

# result = np.sin(numbers1) # Dizideki her elemanın sinüsünü alır
# result = np.cos(numbers1) # Dizideki her elemanın kosinüsünü alır
# result = np.sqrt(numbers1) # Dizideki her elemanın karekökünü alır
# result = np.log(numbers1) # Dizideki her elemanın logaritmasını alır

# multiNumbers1 = numbers1.reshape(2,3) # Matrisi 2 satır 3 sütun olacak şekilde boyutlandırır
# multiNumbers2 = numbers2.reshape(2,3)
# print(multiNumbers1)
# print(multiNumbers2)

# result = np.vstack((multiNumbers1,multiNumbers2)) # İki matrisi alt alta olacak şekilde birleştirir
# result = np.hstack((multiNumbers1,multiNumbers2)) # İki matrisiyan yana olacak şekilde birleştirir

# result = numbers1 >= 50 # Listedeki her eleman için şartı kontrol eder. Her eleman için true ya da false değer döner
# result = numbers1 % 2 == 0
# result2 = numbers1[result] # Sadece verilen şarta uyan sayıları getirir
# print(result)

