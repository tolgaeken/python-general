liste = [1,2,3,4,5] # Listeler bir Iterable obje olduğu için for döngüsünde dolaşılabilir

# print(dir(liste)) # İçinde __iter__ fonksiyonu mevcuttur

iterator = iter(liste)

# print(iterator)

# print(next(iterator)) # Listenin bir elemanını verir
# print(next(iterator)) # Eleman fazlası kadar iterator gonderilirse hata verir
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))


# for i in liste: # For döngüsü bir iterator oluşturur
#     print(i)

while True: # For döngüsünü iterator ile çalıştırma
    try:
        element = next(iterator)
        print(element)
    except StopIteration as ex:
        break




class MyNumbers:
    def __init__(self,start,stop):
        self.start = start
        self.stop  = stop

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.start<=self.stop:
            x = self.start
            self.start +=1
            return x
        
        else:
            raise StopIteration

list = MyNumbers(10,20)

myIter = iter(list)

while True:
    try:
        element = next(myIter)
        print(element)

    except:
        break

