#-*- CODING = utf-8 -*-
#@TIME :  18:39
#@Author ： hwy
#@File : DEMO2.py
#@Software : PyCharm 18:39
'''if True:
    print("true")  # 缩进表达
else:
    print("flase")
'''
import random
a = int(input("请输入：剪刀（0），石头（1），布（2）"))
b = random.randint(0, 2)

if a!=0 and a!=1 and a!=2:  #注意此处的逻辑，三个都不是的时候为真，不能用or ，应该用and
    print("您的输入有误！")
else:
    print("你的输入为：%s" % a)
    print("随机生成的数字为：%s" % b)
    if a == b:
        print("draw!(平局)")
    elif a==0 and b==2 or a==1 and b==0 or a==2 and b==1:
        print("Oh,victory!")
    elif a==0 and b==2 or a==1 and b==2 or a==2 and b==0:
        print("Opps,defeat!")




