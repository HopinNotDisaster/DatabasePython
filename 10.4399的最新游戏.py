import re

import requests

url = 'https://www.4399.com/special/19.htm'

# res是响应的意思！
res = requests.get(url, headers={}, data={}, cookies={}, proxies={})

res = res.content.decode('GBK')
zui = re.findall(r'<div class="bre">(.*?)<div class="bre">',
                 res, re.S)[0]
# print(zui)
zui1 = re.findall(r'<a href=".*?"><img alt="(.*?)" lzimg="1" lz_src="(.*?)">.*?</a>',
                  zui, re.S)
print(zui1, len(zui1))
zui2 = re.findall(
    r'<div class="h-hover" style="display:none"><a class="play" href=".*?"></a><a href=".*?">官网</a>\|<a href="(.*?)">礼包</a></div>',
    zui, re.S)
print(zui2, len(zui2))

latest_game = [

]
for i in range(len(zui2)):
    tem = {
        "game_name": zui1[i][0],
        "picture": zui1[i][1],
        'gift_bag': zui2[i]
    }
    latest_game.append(tem)
# kflist19 = re.findall(r'<ul class="s-list cf" id="kflist19">(.*?)</ul>',
#                       res, re.S)[0]
# # print(kflist19)
# # print(type(kflist19))
# # print(len(kflist19))
# kflist19 = re.findall(
#     r'<li><a href=".*?" alt=".*?"></a><em><a href=".*?">(.*?)</a><i>(.*?)</i></em><span><a href=".*?">(.*?)</a></span></li>',
#     kflist19, re.S)

# kf_datas = [
#
# ]
# # print(kflist19)
# for data in kflist19:
#     tem = {
#         'name': data[0],
#         'kf_time': data[1].replace("&nbsp;", ' '),
#         'server_name': data[2]
#     }
#     print(data[0], data[1].replace("&nbsp;", ' '), data[2])
#     kf_datas.append(tem)
#
import pymongo

client = pymongo.MongoClient()
db = client.get_database("4399")
collection_kf = db.get_collection('latest_game')
collection_kf.insert_many(latest_game)

client.close()
