# 三、东方财富网爬虫存储mysql或者mongodb
# https://quote.eastmoney.com/center/gridlist.html#hs_a_board
# import json
# import re
# from urllib import request
#
# datas = [
# ]
#
# # 'https://27.push2.eastmoney.com/api/qt/clist/get?cb=jQuery112406571497915027975_1710851080110&pn=4&pz=20&po=1&np=1&ut=bd1d9ddb04089700cf9c27f6f7426281&fltt=2&invt=2&wbp2u=|0|0|0|web&fid=f3&fs=m:0+t:6,m:0+t:80,m:1+t:2,m:1+t:23,m:0+t:81+s:2048&fields=f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18,f20,f21,f23,f24,f25,f22,f11,f62,f128,f136,f115,f152&_=1710851080399'
# # 'https://27.push2.eastmoney.com/api/qt/clist/get?cb=jQuery112406571497915027975_1710851080110&pn=3&pz=20&po=1&np=1&ut=bd1d9ddb04089700cf9c27f6f7426281&fltt=2&invt=2&wbp2u=|0|0|0|web&fid=f3&fs=m:0+t:6,m:0+t:80,m:1+t:2,m:1+t:23,m:0+t:81+s:2048&fields=f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18,f20,f21,f23,f24,f25,f22,f11,f62,f128,f136,f115,f152&_=1710851080377'
# # 'https://27.push2.eastmoney.com/api/qt/clist/get?cb=jQuery112406571497915027975_1710851080110&pn=2&pz=20&po=1&np=1&ut=bd1d9ddb04089700cf9c27f6f7426281&fltt=2&invt=2&wbp2u=|0|0|0|web&fid=f3&fs=m:0+t:6,m:0+t:80,m:1+t:2,m:1+t:23,m:0+t:81+s:2048&fields=f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18,f20,f21,f23,f24,f25,f22,f11,f62,f128,f136,f115,f152&_=1710851080360'
# first_url = 'https://27.push2.eastmoney.com/api/qt/clist/get?cb=jQuery112406571497915027975_1710851080108&pn=1&pz=20&po=1&np=1&ut=bd1d9ddb04089700cf9c27f6f7426281&fltt=2&invt=2&wbp2u=|0|0|0|web&fid=f3&fs=m:0+t:6,m:0+t:80,m:1+t:2,m:1+t:23,m:0+t:81+s:2048&fields=f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18,f20,f21,f23,f24,f25,f22,f11,f62,f128,f136,f115,f152'
#
# res = request.urlopen(first_url)
# res = res.read().decode()
# # res = res[41:-1]
# print(res)
#
# # res = re.findall(r'jQuery112406571497915027975_1710851080108\(\{"rc":0,"rt":6,"svr":182482393,"lt":1,"full":1,"dlmkts":"","data":\{"total":5600,"diff":(.*?)\}\}\);',res)
# # s = 'jQuery112406571497915027975_1710851080108'
#
# res1 = re.findall(r'jQuery112(.*?)_1710851080108',res)[0]
# print(res1)
# s = 'jQuery112406571497915027975_1710851080108'
# print(len(s))
# s = '({"rc":0,"rt":6,"svr":2887259487,"lt":1,"full":1,"dlmkts":"","data":{"total":5600,"diff":'
# print(len(s))
# res = res[88:-3]
# # print(res)
# res = json.loads(res)
# for data in res:
#     data_dic = {'页码': 1, '公司名称': data['f14'], '最高': data['f15'], '最低': data['f16']}
#     datas.append(data_dic)
#     # print(data['f14'], data['f15'], data['f16'])
#     # print(type(data))
# # print(type(res))
# print(datas)
import json
# for i in range(2,21):
#     url =f'https://27.push2.eastmoney.com/api/qt/clist/get?cb=jQuery112406571497915027975_1710851080110&pn={i}&pz=20&po=1&np=1&ut=bd1d9ddb04089700cf9c27f6f7426281&fltt=2&invt=2&wbp2u=|0|0|0|web&fid=f3&fs=m:0+t:6,m:0+t:80,m:1+t:2,m:1+t:23,m:0+t:81+s:2048&fields=f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18,f20,f21,f23,f24,f25,f22,f11,f62,f128,f136,f115,f152'
#     res = request.urlopen(url)
#     res = res.read().decode()
#     res = res[41:-1]
#     res = res[88:-3]
#     res = json.loads(res)
#     for data in res:
#         data_dic = {'页码': i, '公司名称': data['f14'], '最高': data['f15'], '最低': data['f16']}
#         datas.append(data_dic)
#     print(datas)

# import pymongo
#
# client = pymongo.MongoClient()
# db = client.get_database("百度新闻")
# collection_bdxw = db.get_collection('bdxw')
# collection_bdxw.insert_many(datas)
#
# client.close()


import time

import requests
import re

# page=1
# time_stamp=time.time()*1000

url = 'https://35.push2.eastmoney.com/api/qt/clist/get?cb=jQuery1124011438784477947306_1710926078440&pn=1&pz=20&po=1&np=1&ut=bd1d9ddb04089700cf9c27f6f7426281&fltt=2&invt=2&wbp2u=|0|0|0|web&fid=f3&fs=m:0+t:6,m:0+t:80,m:1+t:2,m:1+t:23,m:0+t:81+s:2048&fields=f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18,f20,f21,f23,f24,f25,f22,f11,f62,f128,f136,f115,f152&_=1710926078441'
res = requests.get(url)
# print(dir(res))
# print(res.json)
# print(res.next)
res = res.text
# print(type(res))
print(res)

# 该正则的使用本质是截取，只要写出你想要部分的前后内容（其前后内容唯一）即可！
res = re.findall(
    r'"diff":(.*?)}}',
    res)[0]
# res = re.findall(
#     r'jQuery1124011438784477947306_1710926078440\(\{"rc":0,"rt":6,"svr":180606395,"lt":1,"full":1,"dlmkts":"","data":\{"total":5600,"diff":(.*?)}}\);',
#     res)[0]
print(res)
res = json.loads(res)
print(type(res))
