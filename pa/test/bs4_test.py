# -*- CODING = utf-8 -*-
# @TIME :  23:34
# @Author ： hwy
# @File : bs4_test.py
# @Software : PyCharm 23:34

"""
bs4 解析 将复杂的html文档装换成复杂的树形结构，每个节点都是一个python 对象，所有对象可以归纳为4种
注意不要将文件命名为bs4.py 程序会首先在当前目录下找名为bs4的模块。
Tag
NavigableString
BeautifulSoup
Comment
"""

# tag  标签及其内容，只能拿到找到的第一个内容

# from bs4 import BeautifulSoup
#
# file = open("./百度一下.html", "rb")
# html = file.read().decode("utf-8")
# bs = BeautifulSoup(html, "html.parser")
#
# print(bs.title)
# print(bs.a)
# #print(bs.head)
# print(type(bs.head))
# print(bs.title.string)  # NavigableString
# print(bs.a.attrs)
# print(type(bs))  # 表示整个文档  BeautifulSoup
# print(bs.name)
# print(bs.attrs)
# print(bs)

# comment 是一个特殊的NavigableString ，内容不包含注释符号
# print(type(bs.a.string))

# ---------------
# 文档的遍历
# print(bs.head.contents)
# #content  获取Tag的所有子节点，返回一个list
# print(bs.head.contents[44])
# # print(len(bs.head.contents))


# 文档的搜索 更重要 知道内容在哪儿

from bs4 import BeautifulSoup
file = open("./百度一下.html", "rb")
html = file.read().decode("utf-8")
bs = BeautifulSoup(html, "html.parser")

# find_all()
# 字符串过滤，会查找与字符串完全匹配的内容
#t_list = bs.find_all("a")

#正则表达式 ：使用search()搜索
import re
#t_list = bs.find_all(re.compile("a"))

# 方法 ：传入一个函数，根据函数的要求来搜索
# 作为了解
# def name_is_exists(tag):
#     return tag.has_attr("name")
# t_list = bs.find_all(name_is_exists)
# print(t_list)
# for item in t_list:
#     print(item)

#  kwargs 参数
# t_list = bs.find_all(id="head")
# for item in t_list:
#     print(item)
# t_list = bs.find_all(class_=True)
# for item in t_list:
#     print(item)

# text参数
#t_list = bs.find_all(text="hao123")
#t_list = bs.find_all(text=["hao123","地图","贴吧"])
#t_list = bs.find_all(text=re.compile("\d"))
# 正则表达式查找特定文本的内容（标签里的字符）

# limit 参数
# t_list = bs.find_all("a",limit=3)  #限制个数
# for item in t_list:
#     print(item)

# css选择器
t_list = bs.select("title")  #标签查找
t_list = bs.select(".mnav")  #类名查找
t_list = bs.select("#u1")    #id查找
t_list = bs.select("a[class='s-set-skin']")  # 通过属性来查找
t_list = bs.select("head>title")     # 通过子标签查找

for item in t_list:
    print(item)












