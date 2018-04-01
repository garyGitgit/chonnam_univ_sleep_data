import sqlite3

conn = sqlite3.connect('db/sleep_data.db')
print ("Opened database successfully")
conn.execute(''' drop table if exists SLEEP_DATA;''')
conn.execute('''CREATE TABLE SLEEP_DATA 
         (ID INTEGER PRIMARY KEY     AUTOINCREMENT,
         USERNAME           TEXT    NOT NULL,
         DATA_A            BIGINT     NOT NULL,
         DATA_B            BIGINT     NOT NULL,
         DATA_C            BIGINT     NOT NULL,
         DATA_D            BIGINT     NOT NULL,
         DATA_E            BIGINT     NOT NULL,
         DATA_F            BIGINT     NOT NULL,
         CREATED_DATE        DATE);''')
print ("Table created successfully")

conn.close()
