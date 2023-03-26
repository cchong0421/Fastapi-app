import sqlite3
import uuid



conn = sqlite3.connect("demo.db", timeout=10.0)

cursor = conn.cursor()
# myuuid = uuid.uuid4()
# cursor.execute(f"INSERT INTO Users VALUES('{myuuid}','{myuuid}','1234','1975-04-21',0)")


result = cursor.execute("SELECT * FROM Users")

for row in result:
    print(row)

conn.commit()
conn.close()