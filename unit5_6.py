import sqlite3
con=sqlite3.connect('student.db');cur=con.cursor()
cur.execute('delete from student where roll=?',(int(input()),));con.commit()