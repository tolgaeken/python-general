liste = ["1","2","5a","10b","abc","10","50"]

# 1 - Liste içindeki sayısal elemanları bulma

def ilkFonksiyon():
    for i in liste:
        try:
            result = int(i)
            print(result)
        except ValueError:
            continue

# 2 - Kullanıcı q değerini girmedikçe alınan her inputun sayı olduğundan emin olma, değilse hata mesajı yazdırma

def ikinciFonksiyon():
    while True:
        girdi = input("Bir değer girin\n")
        if girdi.lower() == "q":
            break
        try:
            girdi = float(girdi)
        except ValueError:
            print("Girilen değer bir sayı değildir")
            continue


# 3 - Girilen parola içinde türkçe karakter hatası

def ucuncuFonksiyon():
    turkceKarakterler ="şçğüöİı"
    parola = input("Parola Giriniz\n")
    for i in parola:
        if i in turkceKarakterler:
            raise TypeError("Parola Türkçe karakter içeremez")

    print(f"Parola {parola}")
        


# 4 - Faktöriyel fonksiyonu oluşturup fonksiyona gelen değer için hata mesajı verme

def dorduncuFonksiyon(sayi):
    sayi = int(sayi)
    if sayi<0:
        raise ValueError("Negatif Değer")
    
    result = 1
    for i in range(1,sayi+1):
        result *= i
    
    return result

def dorduncuFonksiyon2():
    for x in [5,10,"20",-3,"10a"]:
        try:
            y = dorduncuFonksiyon(x)
        except ValueError as val:
            print(val)
            continue

        print(y)



dorduncuFonksiyon2()