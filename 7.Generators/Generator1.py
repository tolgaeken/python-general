# Bellekte yer işgal etmeyen iterator üretmek için kullanılır

def cube():

    for i in range(5):
        yield i ** 3 # yield ile değeri gönderir ve gönderdikten sonra silinir

liste = (i**3 for i in range(5)) # List comprehension ile alternetif generator oluşturma

for i in liste:
    print(i)