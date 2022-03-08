import sqlite3
connection = sqlite3.connect("hospital.db")
getName = input("Enter Name : ")
getQualification = input("Enter Qualification:")
getAddress = input("Enter Address : ")
getPhone_no = input("Enter Phone Number : ")
getEmail_Id = input("Enter Email ID:")
result1 = connection.execute("SELECT * FROM DOCTOR  WHERE PHONE_NO="+getPhone_no+"")

connection.commit()
print("Updated Sucessfully")

for i in result1:
    print("DOCTOR_Name:", i[0])
    print("QUALIFICATION:", i[1])
    print("ADDRESS:", i[2])
    print("PHONE_NO:", i[3])
    print("EMAIL_ID:", i[4])
