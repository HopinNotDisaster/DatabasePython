import re

import requests

url = 'https://www.4399.com/special/19.htm'

# res是响应的意思！
res = requests.get(url, headers={}, data={}, cookies={}, proxies={})

res = res.content.decode('GBK')
# print(res)
kflist19 = re.findall(r'<ul class="s-list cf" id="kflist19">(.*?)</ul>',
                      res, re.S)[0]
# print(kflist19)
# print(type(kflist19))
# print(len(kflist19))
kflist19 = re.findall(
    r'<li><a href=".*?" alt=".*?"></a><em><a href=".*?">(.*?)</a><i>(.*?)</i></em><span><a href=".*?">(.*?)</a></span></li>',
    kflist19, re.S)

kf_datas = [

]
# print(kflist19)
for data in kflist19:
    tem = {
        'name': data[0],
        'kf_time': data[1].replace("&nbsp;", ' '),
        'server_name': data[2]
    }
    print(data[0], data[1].replace("&nbsp;", ' '), data[2])
    kf_datas.append(tem)

import pymongo

client = pymongo.MongoClient()
db = client.get_database("4399")
collection_kf = db.get_collection('kflist19')
collection_kf.insert_many(kf_datas)

client.close()
