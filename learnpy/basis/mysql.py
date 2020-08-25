import MySQLdb

conn = MySQLdb.connect(
	host = 'localhost',
	port = 3306,
	user = 'root',
	passwd ='123456',
	db = 'gust_test')

cur = conn.cursor()

#create table
#cur.execute("create table student(id int, name varchar(20), class varchar(30), age varchar(10))")

# insert one row
cur.execute("insert into student values('2','Tom', '3 year 2 class','9')")

#update data
cur.execute("update student set class = '3 year 1 class' where name = 'Tom'")

#delete
cur.execute("delete from student where age ='9'")

sqli = "insert into student values(%s,%s,%s,%s)"
cur.execute(sqli, ('4','Huhu', '2 year 1 class','7'))

cur.executemany(sqli,[
    ('3','Tom','1 year 1 class','6'),
    ('3','Jack','2 year 1 class','7'),
    ('3','Yaheng','2 year 2 class','7'),
    ])

cur.executemany(sqli,[
	('3','Lyli','3 year 2 class', '9'),
	('3','May','3 year 2 class', '9'),
	])

aa = cur.execute("select * from student")
cur.fetchone()
cur.scroll(0,'absolute')

info = cur.fetchmany(aa)

for ii in info:
	print(ii)

cur.close()
conn.commit()
conn.close()