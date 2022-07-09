# Os modülü
import os
# print(dir(os))
# import datetime


# print(os.name) # İşletim sisteminin adını gösterir
# print(os.getcwd()) # Bu .py dosyasının bulunduğu konumu gösterir
# os.mkdir("new directory") # Bu .py dosyasının bulunduğu konuma klasör ekler
# os.chdir("C:\\") # Girilen konuma gider
# os.mkdir("Test") # chdir ile seçilen konuma klasör ekler
# os.chdir("..") # Bu .py dosyasının buluduğu klasörün bir üst klasörüne geçer
# os.chdir("../..") # Bu .py dosyasının buluduğu klasörün 2 üst klasörüne geçer
# os.makedirs("newdirectory/yklasor") # İç içe klasör oluşturulmaısnı sağlar
# os.rename("newdirectory","yklasor") # klasör ismini ikinci parametre ile değiştirir
# os.rmdir("newdirectory") # Etkin klasör içindeki klasörü siler
# print(os.listdir()) # Etkin klasör içindeki klasörleri ve dosyaları liste olarak gösterir
# print(os.listdir("C:\\")) # Seçilen klasör içindeki klasörleri ve dosyaları liste olarak gösterir

# for dosya in os.listdir():
#     if dosya.endswith(".py"):
#         print(dosya)

# result = os.stat("8. Advanced Python Modules/Advanced1.py") # Dosya hakkında bilgi verir

# print(result.st_size/1024) 
# # Dosyanın byte cinsinden büyüklüğünü verir. "/1024" ile kb cinsinden değerine ulaşılabilir

# print(datetime.datetime.fromtimestamp(result.st_atime)) 
# # Dosyanın son erişilme tarihini verir fakat "fromtimestamp" ile cast edilmesi gerekir

# print(datetime.datetime.fromtimestamp(result.st_mtime)) 
# # Dosyanın son değiştirilme tarihini gösterir

# print(datetime.datetime.fromtimestamp(result.st_ctime)) 
# # Dosyanın eklenme tarihini gösterir

# os.system("notepad.exe") # uygulama çalıştırmak için kullanılır

# print(os.path.abspath("8. Advanced Python Modules/Advanced1.py")) 
# # belirtilen dosyanın tam konumunu verir

# print(os.path.dirname("8. Advanced Python Modules/Advanced1.py")) 
# # belirtilen dosyanın buluduğu klasörü gösterir "FullPath" de verilebilir

# print(os.path.exists("8. Advanced Python Modules/Advanced1.py")) 
# # belirtilen dosyanın var olup olmadığını kontrol eder

# print(os.path.isdir("8. Advanced Python Modules")) 
# # belirtilen konumun klasör olup olmadığını kontrol eder

# print(os.path.isfile("8. Advanced Python Modules/Advanced1.py")) 
# # belirtilen konumun dosya olup olmadığını kontrol eder

