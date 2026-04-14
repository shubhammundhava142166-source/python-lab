import sqlite3
con=sqlite3.connect('student.db');cur=con.cursor()
cur.execute('update student set name=? where roll=?',(input(),int(input())));con.commit()