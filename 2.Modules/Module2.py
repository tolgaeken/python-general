#Random Modülü
import random

# result = dir(random)
# result = help(random)

# result = random.random() # 0 ile arasında restgele sayı üretir
# result = random.random() * 100
# result = random.uniform(10,100) # Float olarak rastgele sayı üretir
# result = random.randint(1,100) # Int olarak rastgele sayı üretir
# result = random.randrange(1,100)

names = ["Ali","Yağmur","Cenk","Mehmet"]
# result = names[random.randint(0,len(names)-1)]
# result = random.choice(names) # Liste içinden rastgele eleman seçer
# metin = "Hello"
# result = random.choice(metin) # String için de kullanılabilir

# liste = list(range(10))
# random.shuffle(liste) # Listenin elemanlarını karıştırır

# liste = range(100)
# result = random.sample(liste,3) # Liste içinden 3 adet restgele değeri getirir
result = random.sample(names,2)
print(result)