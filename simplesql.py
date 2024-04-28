import pymysql


class SimpleSql:
    """
    传入数据库的名字，直接以root连接数据库！
    """

    def __init__(self, database):
        self.con = pymysql.connect(user='root', password='123456')
        self.con.select_db(database)
        self.cur = self.con.cursor()
        print(f"成功连接数据库{database}")

    def show_tables(self):
        self.cur.execute('show tables;')
        self.print_result()

    def show_data_in_table(self, table):
        self.cur.execute(f'select * from {table}')
        self.print_result()

    def print_result(self):
        datas = self.cur.fetchall()
        for data in datas:
            print(_ for _ in data)

    def only_execute(self, sql):
        """
        创建表格，无返回值，无输出查看的内容。
        删除任何内容，无返回值，无输出查看的内容。
        :param sql:
        :return:
        """
        self.cur.execute(sql)

    def __del__(self):
        self.cur.close()
        self.con.close()
