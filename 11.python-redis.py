import redis

client = redis.StrictRedis(password='123456')

# r = client.hget("h1", 'k1')
# print(r)

# client.hmset("hm1", {"k1": 'v1', "k2": 'v2'})

# r = client.lpush("l2", 1, 3, 5)
# print(r)
# r = client.rpush("l2", 7)
#
# r = client.lpop("l2")
# r = client.rpop("l2")

# 哈希 键（redis键）
# 字段（hash中的键）  值（hash中的值）
#  设置一个键对应的是一个哈希类型的键值对
# r = client.hmset('hash01',
#                  {'k2': 'v2',
#                   'k3': 'v3'})
# print(r)
# r = client.hget('hash01', 'k1')
# print(r)
# r = client.hmget('hash01', ['k1', 'k2'])
# print(r)
# r = client.hdel('hash01', 'k1')
# print(r)
# r = client.hset('hash01', 'k001', 1)
# print(r)
# r = client.hincrby('hash01','k001')
# print(client.hexists('hash01', 'k001'))
# r = client.hvals('hash01')
# print(r)
# r = client.hlen('hash01')
# print(r)
# 通过权重来实现排序
# r = client.zadd('zset0017', {
#     'v5': 50,
#     'v6': 80
# })
# # r = client.zrem('zset0017', 'v5')
# r = client.zrange('zset0017', 1, 2, withscores=1)
# print(r)
# r = client.zcard('zset0017')
# print(r)
# r = client.zcount('zset0017')
# print(r)






client.close()
"""
LPUSH key value1 [value2 ...]：将一个或多个值插入到列表的头部。
RPUSH key value1 [value2 ...]：将一个或多个值插入到列表的尾部。
LPOP key：移除并返回列表的第一个元素。
RPOP key：移除并返回列表的最后一个元素。
LINDEX key index：返回列表中指定索引位置的元素。
LRANGE key start stop：返回列表中指定范围内的元素，start和stop为索引。
LLEN key：返回列表的长度。
LINSERT key BEFORE|AFTER pivot value：在列表中某个元素的前面或后面插入一个新元素。
LREM key count value：从列表中删除指定数量的与指定值相等的元素。
LSET key index value：将列表中指定索引位置的元素设置为新值。
LTRIM key start stop：保留列表中指定范围内的元素，其它元素全部删除。

lpush(key,v)
rpush(key,v)
lpop(k)
rpop(k)
lset()
linsert()
lrem()
ltrim()  # 把原始内容切片
lrange()    # 修改指定位置的指定元素
lindex()

"""
