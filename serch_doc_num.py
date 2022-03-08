import sqlite3
connection = sqlite3.connect("hospital.db")
getPhone_no = input("Enter Doctor number to be Searched:")
result1 = connection.execute("SELECT * FROM DOCTOR  WHERE PHONE_NO="+getPhone_no+"")
for i in result1:
    print("DOCTOR_Name:", i[0])
    print("QUALIFICATION:", i[1])
    print("ADDRESS:", i[2])
    print("PHONE_NO:", i[3])
    print("EMAIL_ID:", i[4])
