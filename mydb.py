import mysql.connector # type: ignore

dataBase = mysql.connector.connect(
    host= 'localhost', 
    user = 'root',
    password = 'Mjbaba@22',
    port = 3306
    )

# Preapare a cursor object
cursorObject = dataBase.cursor()

# Create a database
cursorObject.execute("CREATE DATABASE eldercodb")

print("All Done!")
print("Connected successfully!")
