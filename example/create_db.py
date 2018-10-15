import sqlite3

conn = sqlite3.connect('student.db')

conn.execute('''CREATE TABLE STUDENT
         (ID INT PRIMARY KEY NOT NULL,
         Q1 INT NOT NULL,
         Q2 INT NOT NULL,
         Q3 INT NOT NULL,
         Q4 INT NOT NULL,
         TOTAL INT NOT NULL);''')
print("Table created successfully")

conn.close()