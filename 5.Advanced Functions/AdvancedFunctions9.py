import math
import time

def calculateTime(func):
    def inner(*args,**kwargs):
        start = time.time()
        time.sleep(1) # Fonksiyonu 1 saniye uyutur
        func(*args,**kwargs)
        finish = time.time()
        print(f"{func.__name__} fonksiyonu {str(finish-start)} saniye sürdü")
    return inner

@calculateTime
def usAlma(a,b):
    print(math.pow(a,b))

@calculateTime
def factorial(num):
    print(math.factorial(num))

usAlma(2,3)
factorial(4)