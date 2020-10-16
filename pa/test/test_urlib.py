# -*- CODING = utf-8 -*-
# @TIME :  17:00
# @Author ： hwy
# @File : test_urlib.py
# @Software : PyCharm 17:00

import urllib.request

# 获取一个get请求
# response = urllib.request.urlopen("http://www.baidu.com")
# print(response)
# print(response.read().decode("utf-8"))  #进行解码

# 获取一个post请求  模拟真实登陆
# import urllib.parse
# data = bytes(urllib.parse.urlencode({"用户名":"密码"}),encoding="utf-8")
# response = urllib.request.urlopen("http://httpbin.org/post",data=data
#                                   )
# print(response.read().decode("utf-8"))

# 超时处理
# try:
#     response = urllib.request.urlopen("http://httpbin.org/get",timeout=1)
#     print(response.read().decode("utf-8"))
# except urllib.error.URLError as e:
#     print("time out!")


# response = urllib.request.urlopen("http://httpbin.org/get")
# print(response.status)   #状态码
# print(response.getheaders())

# url = "http://httpbin.org/post"
# headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36"}
# data = bytes(urllib.parse.urlencode({"name":"eric"}),encoding="utf-8")
# req = urllib.request.Request(url=url, data=data, headers=headers)
# response = urllib.request.urlopen(req)
# print(response.read().decode("utf-8"))

url = "http://www.douban.com"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36"}
# headers 伪装成浏览器
req = urllib.request.Request(url=url, headers=headers)  # 生成一个请求对象，包含url headers data method 等等
response = urllib.request.urlopen(req)  # 将请求对象传入urlopen 向网站发出请求
print(response.read().decode("utf-8"))
