# MySql - Join
import mysql.connector as conn

# ALTER TABLE products
# ADD CONSTRAINT fk_categories_products
# FOREIGN KEY (CategoryId) REFERENCES categories(Id)

connection = conn.connect(host = "localhost",user = "root",password = "MySql1234",database = "node-app")
cursor = connection.cursor()

def getProducts():
    sql = "select * from products inner join categories on categories.id=products.categoryid"

    sql = """select p.name,p.price,c.name from products as p
    inner join categories as c on c.id=p.categoryid where p.name like '%samsung%'"""
    
    cursor.execute(sql)

    try:
        result = cursor.fetchall()
        for product in result:
            print(product)
    except conn.Error as err:
        print(f"Hata : {err}")
    finally:
        connection.close()

getProducts()