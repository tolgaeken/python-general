# NoSql - MongoDb

# # pymongo eklentisinin yüklenmesi gerekir
# # aşağıdaki kod ile otomatik yüklenir
# import os
# os.system('cmd /c "pip install pymongo"')
# os.system('cmd /c "pip install pymongo[srv]"') # MongoDb uzak servera bağlantı kurulması için gereklidir

import pymongo as mng

# myclient = mng.MongoClient("mongodb://localhost:27017") # local bağlantı
# myDb= myclient["node-app"] # Database adı girilir. Eğer böyle bir database yoksa oluşturur. local bağlantı için geçerlidir

myclient = mng.MongoClient("mongodb+srv://admin:1234@cluster0.2adan.mongodb.net/node-app?retryWrites=true&w=majority")
myDb = myclient["node-app"]
myCollection = myDb["products"]

# print(myclient.list_database_names()) # Veritabanlarını listeler
