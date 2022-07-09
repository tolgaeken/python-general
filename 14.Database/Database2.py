# MySql Temel Sorgular
import mysql.connector as conn

def InsertProduct():
    connection = conn.connect(host = "localhost", user = "root", password = "MySql1234", database = "node-app")
    cursor = connection.cursor()

    sql = "INSERT INTO products (name,price,imageUrl,description) VALUES (%s,%s,%s,%s)"
    values = ("Samsung S5",1000,"1.jpg","iyi")

    cursor.execute(sql,values)
    try:
        connection.commit() # Uygulanan değişikliklerin veritabanına yansıması için yazılır
    except conn.Error as err:
        print(f"Hata : {err}")
    finally:
        connection.close() # Veritabanı bağlantısını kapatmak için kullanılır
        print("Veritabanı bağlantısı kapandı")
# InsertProduct()


def InsertProduct2(name,price,imageUrl,description): # Alternatif
    connection = conn.connect(host = "localhost", user = "root", password = "MySql1234", database = "node-app")
    cursor = connection.cursor()

    sql = "INSERT INTO products (name,price,imageUrl,description) VALUES (%s,%s,%s,%s)"
    values = (name,price,imageUrl,description)

    cursor.execute(sql,values)
    try:
        connection.commit()
        print(f"{cursor.rowcount} tane kayıt eklendi") # Yapılan değşikliklerle kaç kayıt eklendiğini belirtir
        print(f"Son eklenen kayıt id : {cursor.lastrowid}") # Son eklenen verinin id numarasını gösterir
    except conn.Error as err:
        print(f"Hata : {err}")
    finally:
        connection.close()
        print("Veritabanı bağlantısı kapandı")

def InsertProduct3(list): # Her veri için veritabanına bağlanmamak ve verileri topluca göndermek için hazırlanan fonksiyon 
    connection = conn.connect(host = "localhost", user = "root", password = "MySql1234", database = "node-app")
    cursor = connection.cursor()

    sql = "INSERT INTO products (name,price,imageUrl,description) VALUES (%s,%s,%s,%s)"
    values = list

    cursor.executemany(sql,values) # executemany ile toplu değişiklikleri uygular
    try:
        connection.commit()
        print(f"{cursor.rowcount} tane kayıt eklendi")
        print(f"Son eklenen kayıt id : {cursor.lastrowid}")
    except conn.Error as err:
        print(f"Hata : {err}")
    finally:
        connection.close()
        print("Veritabanı bağlantısı kapandı")

list = []
while True: # Bu döngü ile veriler hazırlanır ve toplu olarak veritabanına gönderme işlemi yapılır
    name = input("Ürün Adı : \n")
    price = float(input("Ürün Fiyatı : \n"))
    imageUrl = input("Ürün Resmi : \n")
    description = input("Ürün Durumu : \n")

    list.append((name,price,imageUrl,description))

    result = input("Devam etmek istiyor musunuz? \n")
    if result.lower()=="h":
        print("Kayıtlar veritabanına ekleniyor")
        print(list)
        InsertProduct3(list)
        break
    elif result.lower()=="e":
        continue
    else:
        print("Hatalı giriş")