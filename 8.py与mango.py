import pymongo

#   mango端口号  27017


# 创建连接
client = pymongo.MongoClient()

# 获取数据库名字

db = client.get_database("qiku")

collection = db.get_collection("teacher")

curson = collection.find()
# 游标对象是一个迭代器


for data in curson:
    print(data)
