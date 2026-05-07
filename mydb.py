import mysql.connector  # type: ignore

import os
from dotenv import load_dotenv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")

dataBase = mysql.connector.connect(
    host= 'localhost', 
    user = 'root',
    password = os.getenv("DB_PASSWORD"),
    port = 3306
    )

# Preapare a cursor object
cursorObject = dataBase.cursor()

# Create a database
cursorObject.execute("CREATE DATABASE eldercodb")


print("Connected successfully!")
