# SqLite
import sqlite3

connection = sqlite3.connect("14. Database/data/chinook.db")
cursor = connection.cursor()
cursor.execute("select * from customers")
result = cursor.fetchall()
for i in result:
    print(i)
connection.close()