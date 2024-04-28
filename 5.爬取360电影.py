import json
from urllib import request
import re
import pymysql

# 轻罗小扇 UID ： 147693939
headers = {
    'Referer': 'https://www.360kan.com/rank/dongman'
}
datas = [

]

urls = ['https://api.web.360kan.com/v1/rank?cat=5&callback=__jp7']
test_url = 'https://api.web.360kan.com/v1/rank?cat=5&callback=__jp7'
req = request.Request(test_url, headers=headers)

res = request.urlopen(req)
res = res.read().decode()
res = re.findall(r'__jp7\((.*?)\);', res)[0]
res = json.loads(res)
for data in res['data']:
    datas.append((0,data['title'], data['pv']))
# print(datas)
# print(res, type(res))


#
con = pymysql.connect(user='root', password='123456', database='rank_360video')
cur = con.cursor()
cur.executemany('insert into  cartoon values (%s,%s,%s) ', datas)
con.commit()

cur.close()
con.close()
