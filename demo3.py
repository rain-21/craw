# -*- CODING = utf-8 -*-
# @TIME :  23:33
# @Author ： hwy
# @File : demo3.py
# @Software : PyCharm 23:33
'''for i in range(5):
    print(i)

for i in range(2,10,3):
    print(i)

name = "chengdu"
for i in name:
    print(i)


a = ["aa","bb","cc","dd"]
for i in range(len(a)):
    print(a[i])


i=0
sum=0
while i<=100 :
    sum += i
    i=i+1
print(sum)

count = 0
while count<5:
    print(count,"小于5")
    count+=1
else:
    print(count,"大于等于5")


n=1
while n<=100:
    if n>10:
        break   #break 可以跳出for 和while 的循环体
    print(n)
    n+=1

n=0
while n<10:
    n+=1
    if n%2 == 0:
        continue
    print(n)

for letter in "room":
    if letter =='o':
        pass
        print('pass')
    print(letter)
'''

# 九九乘法表
# 第一种 for循环嵌套实现
for i in range(1, 10):
    for num in range(1, i + 1):
        a = i * num
        print("%d*%d=%d" % (i, num, a), end=" ")
    print("")
# 第二种 while判断条件
for x in range(1, 10):
    y = 1
    while y <= x:
        print("%s*%s=%s" % (x, y, x * y), end=" ")
        y += 1
    print("")
