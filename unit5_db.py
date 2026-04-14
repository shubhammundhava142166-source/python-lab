import sqlite3
con=sqlite3.connect('student.db');cur=con.cursor()
cur.execute('create table if not exists student(roll int,name text,gender text,age int,email text,mobile text,city text)');con.commit()