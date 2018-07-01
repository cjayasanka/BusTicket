import dbConn.py
Id="150280D"
cursor.execute('SELECT * FROM User where UserId='+ Id)
row = cursor.fetchone()

conn.close()

print(row)
