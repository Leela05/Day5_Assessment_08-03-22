import sqlite3
connection = sqlite3.connect("hospital.db")
getPhone_no = input("Enter Phone number to be deleted:")
result1 = connection.execute("DELETE FROM DOCTOR WHERE PHONE_NO="+getPhone_no)
connection.commit()
print("Delete Successfully!")

