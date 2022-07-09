# Dosya Okuma Fonksiyonları
with open("newfile.txt","r",encoding="utf-8") as f:
    content = f.read()
    print(content)
    print(f.tell()) # İşaretçi konumunu verir
    f.seek(3) #İşaretçinin gitmesi gereken konumu gösterir
    content2 = f.read()
    print(content2) # İşaretçinin gittiği konumdan itibaren yazdırır