#-*- CODING = utf-8 -*-
#@TIME :  20:05
#@Author ： hwy
#@File : re_tets.py
#@Software : PyCharm 20:05

# 正则表达式 ：字符串模式 判断字符串是否符合一定的标准
import re

# 创建模式对象
# pat = re.compile("AA")  # 此处的是正则表达式  是标准
# m = pat.search("CBA")    # 这里的字符串是被校验的内容
# m = pat.search("ABCAA")  # search方法进行比较查找
# print(m)
#
# # 没有模式对象
#
# m = re.search("asd","asdaa")  # 前面的是标准，后面的是待校验的
#
# print(m)

# m = re.findall("a","AAAVVaCDsda")
# print(m)
#
# m = re.findall("[A-Z]","AAAVVaCDsda")
# print(m)

# m = re.findall("[A-Z]+","AAAVVaCDsda")
# print(m)

# sub

m = re.sub("a", "", "acasddd")  # 找到a用A替换，在第三个字符串中查找
print(m)

# 建议在正则表达式中，被比较的字符串的前面加上r  不用担心转义字符的问题。



