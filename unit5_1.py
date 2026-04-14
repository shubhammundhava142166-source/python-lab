import sqlite3
con=sqlite3.connect('student.db');cur=con.cursor()
for r in cur.execute('select * from student'):print(r)