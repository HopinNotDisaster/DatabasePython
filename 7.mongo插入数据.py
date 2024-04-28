import pymongo

con = pymongo.MongoClient()

db = con['student']
table = db['info']

datas = [
    {
        "name": 'jkl',
        "age": 500,
        "address": 'zz'
    }
]
for i in range(100, 201):
    data = {
        "id": i,
        "age": 500 + i,
        "address": f"东三街{i}号院"
    }
    datas.append(data)

table.insert_many(datas)
rows = table.find()
for row in rows:
    print(row)
