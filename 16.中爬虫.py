import requests

from functools import partial
import subprocess
subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')

import execjs

url = 'https://vipapi.qimingpian.cn/search/recommendedItemList'
data = {
    'page': 1,
    'num': 20,
    'sys': 'vip'
}

res = requests.post(url, data=data)
# print(res.json())
res = res.json()['encrypt_data']
# print(res)

with open("中爬虫的.js", 'r') as f:
    content = f.read()
    js_code = execjs.compile(content)
    info = js_code.call("s", res)
    for data in info['list']:
        print(data)
