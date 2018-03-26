#-*- coding:utf-8 -*-
import requests

req = requests.get('http://xian.fang.com')
req.encoding = req.headers
print(req.text)