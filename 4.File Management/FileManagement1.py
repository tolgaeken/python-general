# Dosya açmak için open() fonksiyonu kullanılır
# Kullanımı open(dosya_adi,dosya_erisme_modu) şeklindedir
# Dosya erişme modu hangi amaçla açılacağını belirtir

#----------
# "w" (Write) yazma modu. Dosyayı konumda oluşturur ve her kullanımında varolan veriyi silip bellekteki verileri yükler

# file = open("newfile.txt","w") # Relative Path
# file = open ("C:/test/test.txt","w") # Full Path
# file.close()

# Aşağıdaki daha yeni bir yöntemdir ve close ile kapatmaya gerek yoktur.
# Encoding yazmak zorunlu değildir fakat türkçe karakterleri tanımaz
# with open ("newfile.txt","w",encoding="utf-8") as f:
#     f.write("Test")

#----------
# "a" (Append) ekleme modu. Dosya konumda yoksa oluşturur ve her kullanımında silmeden üstüne ekleme yapar

# with open ("newfile.txt","a",encoding="utf-8") as f:
#     f.write("\nTest")

#----------
# "x" (Create) oluşturma modu. Dosya zaten mevcut ise hata verir

# with open ("newfile2.txt","x",encoding="utf-8") as f:
#     f.write("Test")

#----------
# "r" (Read) okuma modu. Varsayılandır. Dosya mevcut değil ise hata verir
with open("newfile.txt","r",encoding="utf-8") as f:
    # for i in f:
    #     print(i,end="")
    
    # print(f.readline(),end="") # Her bir satırı tek tek okur. Fazladan yazılırsa yok sayılır.
    # print(f.readline(),end="")
    # print(f.readline(),end="")
    # print(f.readline(),end="")

    liste = f.readlines() # Her satırı bir liste olarak yazdırır
    print(liste)