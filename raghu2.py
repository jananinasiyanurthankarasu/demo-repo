import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Janani_95",
    database="stuinfo"
)
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM branch")
results = mycursor.fetchall()
print(results)