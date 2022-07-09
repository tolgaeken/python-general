# MySql Bağlantısı

# # mysql-connector modülünün yüklenmesi gerekir
# # Aşağıdaki kod ile otomatik yüklenir
# import os
# os.system('cmd /c "pip install mysql-connector"')
# os.system('cmd /c "pip install --user mysql-connector-python"')
# İkinci yüklenen modül ile python uygulamasında native girişi yapma zorunluluğu kalkar

import mysql.connector as conn

myDatabase =conn.connect(
    host = "localhost", # Server adresi
    user = "root", # Kullanıcı adı
    password = "MySql1234" , # Parola
    # auth_plugin = "mysql_native_password" ,# ikinci modül yüklenmezse yazılması zorunludur
    database = "mydb" # Bağlanmak istenen veritabanı adı
)

myCursor = myDatabase.cursor()
# myCursor.execute("Create database myDb") # bağlanan veritabanına sorgu gönderilir

# myCursor.execute("show databases")  
# for i in myCursor:
#     print(i)

# myCursor.execute("create table customers (name VARCHAR(255), address VARCHAR(255))")

