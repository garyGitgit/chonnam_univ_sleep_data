import sqlite3

conn = sqlite3.connect('db/biopac_data.db')
print ("Opened database successfully")
conn.execute(''' drop table if exists BIOPAC_DATA;''')
conn.execute('''CREATE TABLE BIOPAC_DATA 
         (ID INTEGER PRIMARY KEY     AUTOINCREMENT,
         USERNAME           TEXT    NOT NULL,
         BARO REAL NOT NULL,
         RED REAL NOT NULL,
         GREEN REAL NOT NULL,
         BLUE REAL NOT NULL,
         IR REAL NOT NULL,
         AMB1 REAL NOT NULL,
         AMB2 REAL NOT NULL,
         BIOPAC REAL NOT NULL,
         CREATED_DATE        DATE);''')
print ("Table created successfully")

conn.close()
