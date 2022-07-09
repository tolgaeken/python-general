def islem(islemAdi):
    def toplam(*args):
        toplam = 0
        for i in args:
            toplam +=i
        
        return toplam
    
    def carpma(*args):
        carpim = 1
        for i in args:
            carpim *= i
        
        return carpim

    if islemAdi == "toplama":
        return toplam
    
    elif islemAdi == "carpma":
        return carpma
    
topla = islem("toplama")
print(topla(1,2,3,4,5))

carp = islem("carpma")
print(carp(1,2,3,4,5,6))