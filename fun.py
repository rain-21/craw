# -*- CODING = utf-8 -*-
# @TIME :  22:34
# @Author ： hwy
# @File : fun.py
# @Software : PyCharm 22:34
# 函数的定义
# def printinfo():
#     print("-----")
#     print("人生苦短！")
# #函数的调用
# printinfo()

# 带参数的函数
# def add2num(a,b):
#     c = a+b
#     print(c)
# add2num(11,22)

# 带返回值的
# def add2num(a,b):
#     return a+b
# x = add2num(11,22)
# print(x)
# #返回多个值的函数
# def div(a,b):
#     shang = a//b
#     yushu = a&b
#     return shang,yushu
# sh,yu = div(5,2)  #多个值接受，逗号分隔
# print(sh,yu)
# def printline():
#     print("-"*10)
#
# def printlinecontrol(a):
#     while a>0:
#         printline()
#         a-=1
# printlinecontrol(3)
#
# def add3num(a,b,c):
#     return a+b+c
# def average(x,y,z):
#     return add3num(x,y,z)/3
#
# print(average(1,2,3))

# 全局变量与局部变量
# a = 600 #全局变量
# def test():
#     #a = 300  # 局部变量
#     print(a) #调用全局变量
#    # a = 100
#     print(a)
# def test1():
#    global a  #申明全局变量，可以修改全局变量
#
#    a = 500
#    print(a)
#
# print(a)
#
# test()
# test1()

# 文件操作
# 文件打开与关闭
# f = open("test.txt")  # 打开文件，写模式，不存在则新建
# #f.write("hello world!")  # 文件写入字符串
# #print(f.read(10)) #读文件字符 首次执行从头开始，之后从当前位置开始
# print(f.readline()) #按行读
# print(f.readlines()) #读取整个文件 ，以列表形式
# f.close()  #关闭文件

# 错误处理
"""try:  # 捕获异常
    print("----")
    f = open("123.txt","r")

    print("====")
except IOError:  # 文件没找到属于输入输出异常  IO异常
    pass
try:
    print(num)
except NameError:  # 异常类型要一致才能捕获
    print("error!")

try:
    print("----")
    f = open("123.txt", "r")
    print("====")
    print(num)
except (NameError, IOError) as result:
    #程序虽然没报错，
   # 但是只执行到第一次报错的地方，因此只会打印文件找不到的错误

    print("error!")
    print(result)
#  Exception 可以承接任何异常
"""
"""
#嵌套
import time
try:
    f = open("123.txt","r")

    try:
        while True:
            content = f.readline()
            if len(content) == 0:
                break
            time.sleep(2)
            print(content)
    finally:
        f.close()
        print("关闭文件！")

except Exception as result:
    print("出现异常！")
"""


def xieru():
    try:
        f = open("gushi.txt", "w")
        a = input("请输入古诗（输入q结束）：")
        while a != "q":
            f.writelines(a+"\n")
            a = input("请输入古诗（输入q结束）：")

    except Exception as result:
        print("出现异常！")
    finally:
        f.close()
def duqu():
    filename = input("请输入要读取的文件名：")
    filename1 = input("请输入目标文件名：")
    try:
        f = open(filename + ".txt","r")
        f1 = open(filename1+".txt","w")
        try:
            while True:
                content = f.readline()
                if len(content) == 0:
                    break
                f1.writelines(content)
            print("复制完毕！")
        finally:
            f.close()
            f1.close()
    except Exception as result:
        print("出现异常！")

xieru()
duqu()
