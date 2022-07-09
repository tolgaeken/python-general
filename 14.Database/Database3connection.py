import mysql.connector as conn

connection =conn.connect(
    host = "localhost",
    user = "root",
    password = "MySql1234",
    database = "schooldb"
)

cursor = connection.cursor()