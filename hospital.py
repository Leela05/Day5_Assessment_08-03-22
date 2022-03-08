import sqlite3
connection = sqlite3.connect("hospital.db")
# Create a  Db
result = connection.execute("SELECT * FROM PATIENT")
result1 = connection.execute("SELECT * FROM DOCTOR")
