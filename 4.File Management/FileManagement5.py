def notHesapla(satir):
    satir = satir[:-1]
    liste = satir.split(":")
    ogrenciAdi = liste[0]
    notlar = liste[1].split(",")

    not1 = int(notlar[0])
    not2 = int(notlar[1])
    not3 = int(notlar[2])

    ortalama = (not1+not2+not3) / 3

    if 100>=ortalama>90:
        harf = "AA"
    elif 90>=ortalama>80:
        harf = "BB"
    elif 80>=ortalama>70:
        harf = "CC"
    elif 70>=ortalama>60:
        harf = "DD"
    elif 60>=ortalama>=0:
        harf = "FF"
    
    return f"{ogrenciAdi} : {harf}\n"

def ortalamaOku():
    with open("notlar.txt","r",encoding="utf-8") as f:
        for satir in f:
            print(notHesapla(satir))

def notGir():
    isim = input("Öğrenci Adı\n")
    soyisim = input("Öğrenci Soyadı\n")
    not1 = input("1. Not\n")
    not2 = input("2. Not\n")
    not3 = input("3. Not\n")

    with open("notlar.txt","a",encoding="utf-8") as f:
        f.write(f"{isim} {soyisim}:{not1},{not2},{not3}\n")

def notKaydet():
    with open ("notlar.txt","r",encoding="utf-8") as f:
        liste = []

        for i in f:
            liste.append(notHesapla(i))

    with open ("sonuclar.txt","w",encoding="utf-8") as f2:
        for i in liste:
            f2.write(i)

while True:
    islem = int(input("1 - Notları Oku\n2 - Not Gir\n3 - Notları Kaydet\n4 - Çıkış\n"))

    match (islem):
        case 1:
            ortalamaOku()
        case 2:
            notGir()
        case 3:
            notKaydet()
        case 4:
            break