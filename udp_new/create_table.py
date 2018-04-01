import sqlite3

conn = sqlite3.connect('db/sleep_data.db')
print ("Open database successfully")
conn.execute(''' drop table if exists SLEEP_DATA;''')
conn.execute('''CREATE TABLE SLEEP_DATA 
         (Num INTEGER PRIMARY KEY AUTOINCREMENT,
         Name TEXT    NOT NULL,
         Device TEXT NOT NULL,
         ch1 TEXT NOT NULL,
         ch2 TEXT NOT NULL,
         created_date DATE);''')
print ("Table created successfully")

conn.close()
