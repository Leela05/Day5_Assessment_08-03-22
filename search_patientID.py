import sqlite3
connection = sqlite3.connect("hospital.db")
getID = input("Enter Patient Id to be Searched:")
result = connection.execute("SELECT * FROM PATIENT WHERE ID="+getID)
for i in result:
    print("ID", i[0])
    print("PATIENT_Name", i[1])
    print("ADDRESS", i[2])
    print("PHONE_NO", i[3])
    print("EMAIL_ID", i[4])
    print("PIN_CODE", i[5])