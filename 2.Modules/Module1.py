# pypi.org
# pip install package-name

# import math
# import math as islem

# value = dir(math)
# print(value)

# value = help(math)
# print(value)

# value = islem.sqrt(49)
# value = islem.factorial(5)
# value = islem.floor(5.9) # Aşağı Yuvarlama
# value = islem.ceil(5.9) # Yukarı Yuvarlama
# print(value)

from math import *
# from math import pow,pi,sqrt

def sqrt(x):
    print(f"x : {str(x)}")

value = sqrt(9) # Hangisi en son tanımlandıysa o fonksiyona göre işlem yapılır
print(value)
