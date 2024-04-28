# transaction

import pymysql

con = pymysql.connect(port=3306, user="root", password='123456')
con.select_db('exercise')
cur = con.cursor()

try:
    con.begin()
    sqls = [
        'delete from my_big_table where  id > 10;',
        'show table;'
    ]

    line = cur.execute(sqls[0])
    print(f"影响行数：{line}")
    cur.execute(sqls[1])
    con.commit()
except  Exception:
    con.rollback()
    print("有错误语句，执行回滚！")

cur.close()
con.close()
