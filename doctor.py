import sqlite3
connection = sqlite3.connect("hospital.db")  #create a db
# connection.execute('''CREATE TABLE DOCTOR(DOCTOR_NAME TEXT,QUALIFICATION TEXT,
#    ADDRESS TEXT,PHONE_NO INTEGER,EMAIL_ID VARCHAR
#     ); ''')
print("Creation of Table")
print("Table Created Succesfully")
getName = input("Enter Name : ")
getQualification = input("Enter Qualification:")
getAddress = input("Enter Address : ")
getPhone_no = input("Enter Phone Number : ")
getEmail_Id = input("Enter Email ID:")
connection.execute("INSERT INTO DOCTOR(DOCTOR_NAME,QUALIFICATION,ADDRESS,PHONE_NO,EMAIL_ID) \
VALUES('"+getName+"','"+getQualification+"','"+getAddress+"',"+getPhone_no+",'"+getEmail_Id+"')")
connection.commit()
connection.close()
print("Inserted Succesfully")

