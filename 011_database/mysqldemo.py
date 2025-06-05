import mysql.connector

con  = mysql.connector.connect(
    host="localhost",
    user ="root",
    password="root",
    port=3306,
    database="08apr_py"
)

cursor  = con.cursor()

# cursor.execute("create database 08apr_py")