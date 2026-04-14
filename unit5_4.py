import sqlite3
con=sqlite3.connect('student.db');cur=con.cursor()
data=(int(input()),input(),input(),int(input()),input(),input(),input())
cur.execute('insert into student values(?,?,?,?,?,?,?)',data);con.commit()