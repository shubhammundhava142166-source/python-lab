import sqlite3
con=sqlite3.connect('student.db');cur=con.cursor()
while True:
 c=int(input())
 if c==1:
  cur.execute('insert into student values(?,?,?,?,?,?,?)',(int(input()),input(),input(),int(input()),input(),input(),input()));con.commit()
 elif c==2:
  cur.execute('update student set name=? where roll=?',(input(),int(input())));con.commit()
 elif c==3:
  print(cur.execute('select * from student where roll=?',(int(input()),)).fetchone())
 elif c==4:
  cur.execute('delete from student where roll=?',(int(input()),));con.commit()
 elif c==5:
  print(list(cur.execute('select * from student')))
 else:break