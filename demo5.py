#-*- CODING = utf-8 -*-
#@TIME :  18:49
#@Author ： hwy
#@File : demo5.py
#@Software : PyCharm 18:49
namelist = []  #定义空列表
namelist1 = ["xiaozhang","xiaoli",1,namelist]  #可以是不同类型
'''
#for i in namelist1:
 #   print(i)
#增加
nameapp = input("请输入增加的内容：")
namelist1.append(nameapp)
print(namelist1)


a = [1,2]
b = [4,4]
a.append(b)  #整体追加
print(a)
a.extend(b)  #逐一追加
print(a)
a.insert(1,3) #第一个表示下标 第二个表示元素，在下标前面追加元素
print(a)


#删除
movename = ["得到的","dd","ww","ee","ee"]
del movename[1]  #删除指定下标处的元素
print(movename)

#movename.pop()   #弹出末尾的一个元素
#print(movename)

movename.remove("ee")  #删除指定内容,但只删除找到的第一个
print(movename)


# 改
movename = ["得到的","dd","ww","ee","ee"]
movename[1] = "11" #指定下标修改内容
print(movename)

# 查，in  not in
movename = ["得到的","dd","ww","ee","ee"]
findname = input("请输入要查找的电影名称:")
if findname in movename:
    print("find it!")
else:
    print("not found!")

print(movename.index("ee",1,5))  #查找指定范围（左闭右开）是否存在该元素，找不到会报错
print(movename.count("ee"))  #  有几个指定元素


#排序
a = [1,2,3,4]
a.reverse()   #反转
print(a)
a.sort()  #升序排序
print(a)
a.sort(reverse=True)  #降序排序
print(a)

# 嵌套  类似数组
sc = [["beida","qinghua"],[1,2,3],["a",5,6,7]]
print(sc[0][0])

import  random
offices = [[],[],[]]
t_name = ["a","b","c","d","f","g","h","i"]
for name in t_name:
    index = random.randint(0,2)
    offices[index].append(name)
i = 1
for office in offices:
    print("办公室%d的人数为%d"%(i,len(office)))
    for name in office:
        print("%s"%name,end="\t")
    i+=1
    print("\n")
    print("-"*20)
'''

products = [["ipone",6888],["macpro",16888],["coffee",31],["book",60],["nike",699]]
print("-"*5 + "商品列表" + "-"*5)
i = 0
for product in products:
    print(i,end="  ")
    i+=1
    for item in product:
        print(item,end="  ")

    print("\n")
cart = []

while True:
    num = input("请输入要购买的商品编号（输入q结算）：")
    if num == "q":
        break
    else:
        cart.append(products[int(num)])
print("-"*5 + "您购买的商品" + "-"*5)
i = 0
for bought in cart:
    print(i,end="  ")
    i+=1
    for item in bought:
        print(item,end="  ")
    print("\n")


