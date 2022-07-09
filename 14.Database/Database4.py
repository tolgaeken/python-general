# MySql - Aggregate
import mysql.connector as conn

connection = conn.connect(host = "localhost",user = "root",password = "MySql1234",database = "node-app")
cursor = connection.cursor()

def getProduct():
    sql = "Select count(*) from products" # Tüm kayıtların toplam sayısını getirir
    sql = "Select count(*) from products where price > 3000" # price kolonunda 3000 den fazla olan kayıtların sayısını
    sql = "Select avg(price) from products" # price kolonunun ortalamasını getirir
    sql = "Select sum(price) from products" # price kolonunn toplamını getirir
    sql = "Select max(price) from products" # price kolonundaki max değeri getirir
    sql = "Select min(price) from products" # price kolonundaki min değeri getirir
    sql = "Select Name from products where price = (Select max(price) from products)" # price kolonundaki max değerin name koloundaki değerini getirir

    try:
        cursor.execute(sql)
        result = cursor.fetchone()
        print(result)
    except conn.Error as err:
        print(f"Hata : {err}")
    finally:
        connection.close()
getProduct()