import sqlite3
connection = sqlite3.connect("hospital.db")
result = connection.execute("SELECT * FROM PATIENT")
for i in result:
    print("ID:", i[0])
    print("PATIENT_Name:", i[1])
    print("ADDRESS:", i[2])
    print("PHONENO:", i[3])
    print("EMAIL_ID:", i[4])
    print("PINCODE:", i[5])