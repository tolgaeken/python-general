# Dosya üzerinde güncelleme yapma

# with open("newfile.txt","r+",encoding="utf-8") as f: # r+ ile hem okuma hem güncelleme yapılır
#     f.seek(4)
#     f.write("Test2") # 4. Karakterden itibaren üstüne yazılır

# with open("newfile.txt","r+",encoding="utf-8") as f:
#     print(f.read())


# Sayfa başında güncelleme
with open("newfile.txt","r+",encoding="utf-8") as f:
    content = f.read()
    content = "Baslangic\n" + content
    f.seek(0)
    f.write(content)


# Sayfa sonunda güncelleme
with open("newfile.txt","a",encoding="utf-8") as f:
    metin = "\nBitis"
    f.write(metin)


# Sayfa ortasında güncelleme
with open("newfile.txt","r+",encoding="utf-8") as f:
    liste = f.readlines()
    liste.insert(1,"Orta2\n")
    f.seek(0)

    # for i in liste: # 1. Yöntem
    #     f.write(i)
    
    f.writelines(liste) # 2. Yöntem

with open("newfile.txt","r+",encoding="utf-8") as f:
    print(f.read())