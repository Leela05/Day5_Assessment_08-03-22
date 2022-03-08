import sqlite3
connection = sqlite3.connect("hospital.db")  #create a db
# connection.execute('''CREATE TABLE PATIENT(ID INTEGER PRIMARY KEY AUTOINCREMENT,PATIENT_NAME TEXT,ADDRESS TEXT,
#  PHONE_NO INTEGER,EMAIL_ID VARCHAR,PIN_CODE INTEGER
#  ); ''')
print("Creation of Table")
print("Table Created Succesfully")
getName = input("Enter Name : ")
getAddress = input("Enter Address : ")
getPhone_no = input("Enter Phone Number : ")
getEmail_Id = input("Enter Email ID:")
getPincode = input("Enter Pincode : ")
connection.execute("INSERT INTO PATIENT(PATIENT_NAME,ADDRESS,PHONE_NO,EMAIL_ID,PIN_CODE) \
VALUES('"+getName+"','"+getAddress+"',"+getPhone_no+",'"+getEmail_Id+"',"+getPincode+")")
connection.commit()
connection.close()
print("Inserted Succesfully")

