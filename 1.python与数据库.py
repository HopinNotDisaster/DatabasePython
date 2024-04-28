# import pymysql
#
# connection = pymysql.connect(port=3306, user='root', password='123456')
# cursor = connection.cursor()
# sqls = [
#     'create database st charset=utf8;',
#     'use stu',
#     'create table stud (sid int not null primary key,name varchar(225) not null,age int )'
# ]
# cursor.execute(sqls[0])
# cursor.execute(sqls[1])
# cursor.execute('show databases like "sm"')
# print(cursor.fetchall())
# sql = 'create database stumanage charset=utf8;'
# sql = 'select * from my_big_table'
# cursor.execute(sql)
#
# datas = cursor.fetchall()
# print(cursor)
# for data in datas:
#     print(data[0])
# connection.commit()
# cursor.close()
# connection.close()
# print(20000/70)

li = [56, 12, 54]
print(li.pop(0))
