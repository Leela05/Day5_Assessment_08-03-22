import sqlite3
connection = sqlite3.connect("hospital.db")
getName = input("Enter Patient name:")
getAddress = input("Enter Address:")
getPhone_no = input("Enter Phone number:")
getEmail_Id = input("Enter mail id:")
getPincode = input("Enter Pincode:")
result = connection.execute("SELECT * FROM DOCTOR  WHERE PHONE_NO="+getPhone_no+"")
connection.commit()
print("Updated Sucessfully")

for i in result:
    print("ID", i[0])
    print("PATIENT_Name", i[1])
    print("ADDRESS", i[2])
    print("PHONENO", i[3])
    print("EMAIL_ID", i[4])
    print("PINCODE", i[5])