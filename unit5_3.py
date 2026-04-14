import sqlite3
con=sqlite3.connect('student.db');cur=con.cursor()
r=int(input())
res=cur.execute('select * from student where roll=?',(r,)).fetchone()
print(res if res else 'Not found')