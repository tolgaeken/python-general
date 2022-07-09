# Fonksiyon Parametrelerine Fonksiyon Gönderme

def toplam(a,b):
    return a+b

def cikar(a,b):
    return a-b

def carp(a,b):
    return a*b

def bol(a,b):
    return a/b

def islem(f1,f2,f3,f4,islemAdi):
    if islemAdi == "toplama":
        print(f1(2,3))
    elif islemAdi == "cikarma":
        print(f2(7,3))
    elif islemAdi == "carpma":
        print(f3(4,7))
    elif islemAdi == "bolme":
        print(f4(18,2))
    else:
        print("Geçersiz işlem")

islem(toplam,cikar,carp,bol,"toplama")
islem(toplam,cikar,carp,bol,"cikarma")
islem(toplam,cikar,carp,bol,"carpma")
islem(toplam,cikar,carp,bol,"bolme")
islem(toplam,cikar,carp,bol,"test")
