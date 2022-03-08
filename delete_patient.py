import sqlite3
connection = sqlite3.connect("hospital.db")
getID = input("Enter ID to be deleted:")
connection.execute("DELETE FROM PATIENT WHERE ID="+getID)
connection.commit()
print("Delete Successfully!")

