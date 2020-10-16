# -*- CODING = utf-8 -*-
# @TIME :  23:23
# @Author ： hwy
# @File : demo6.py
# @Software : PyCharm 23:23

""" 元组  元素不可修改，但可以包含可变对象 如列表list
定义只有一个元素的元组tuple必须加逗号

# tup = (50)  #这不是元组，而是一个int
tup = (50,)
print(type(tup))
tup1 = ("abc","def",2020)
#增加
tup2 = (12,34,56)
#tup2[0] = 100  # 报错，不允许修改
tup3 = ("abc","xyz")
tup4 = tup2+tup3
print(tup4)
# 删除

print(tup2)
del tup2  #直接删除整个元组变量，而不是清空内部元素
print(tup2)

#查找

#字典  dict 使用键值对 key-value 存储，极快的查找速度，键必须是唯一的，key 是不变类型
info = {"name":"wuyanzu","age":"18","pro":"student"}  #字典的定义
#访问  通过键找值  访问不存在的键会报错
print(info["name"])
#print(info.get("gender"))  #使用get方法没有找到键返回none
print(info.get("gender","man"))  #没找到可以有默认值

# 增加
info = {"name": "wuyanzu", "age": "18", "pro": "student"}
newid = input("请输入id：")
info["id"] = newid
print(info["id"])
# 删除
del info["id"]  # 删除指定键值对， 不指定会删除整个字典
print(info.get("id"))

info.clear()  #清空字典
print(info["age"])
"""
#修改
info = {"name": "wuyanzu", "age": "18", "pro": "student"}
info["age"] = 20
print(info["age"])

#查找
# print(info.keys())  # 打印所有的键
# print(info.values())  # 打印所有的值
# print(info.items())  # 得到所有的项（列表） 每个键值对是一个元组
# ctrl + /  快捷注释
# 遍历所有的键或者值
for key in info.keys():
    print(key)
for key,value in info.items():   # 遍历所有键值对
    print("key = %s,vlaue = %s"%(key,value))
mylist = ["a","b","c","d"]
for i,x in enumerate(mylist):  # enumerate 枚举函数 把列表拆分成下标和内容
    print(i,x)
