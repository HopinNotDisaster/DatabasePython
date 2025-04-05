import pymongo

# 连接数据库管理系统
con = pymongo.MongoClient()

# 查看当前系统中有什么数据库！
print(con.list_database_names())

# # 连接数据库！ 一！
# db = con.student
# handler = db.info
# first_line = handler.find_one()
# print(first_line)
# 连接数据库！
db = con['teacher']  # 数据库不需要创建直接use
handler = db['pay']  # 表也不需要创建，直接使用
rows = handler.insert_one({"name": 'aaa', "_id": 0})  # 想要哪个列，就这样标成1
# , {"name": 0, "age": 1}   不能既有0又有1

# for row in rows:
# #     print(row)
#
# handler = db['pay']  # 表也不需要创建，直接使用
# rows = handler.insert_one({"name": 'aaa', "_id": 0})  # 想要哪个列，就这样标成1
# # , {"name": 0, "age": 1}   不能既有0又有1
#  db = con.student
# handler = db.info
# first_line = handler.find_one()
# print(first_line)