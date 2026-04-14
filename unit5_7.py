import sqlite3,re
con=sqlite3.connect('student.db');cur=con.cursor()
for r in cur.execute('select * from student'):
 if re.match(r'^[\w\.-]+@[\w\.-]+$',r[4]):print(r)