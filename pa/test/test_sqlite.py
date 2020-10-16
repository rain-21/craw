# -*- CODING = utf-8 -*-
# @TIME :  21:39
# @Author ： hwy
# @File : test_sqlite.py
# @Software : PyCharm 21:39

import sqlite3

# conn = sqlite3.connect("test.db")  # 打开或创建数据库文件
#
# print("Opened database successfully")
# c = conn.cursor()   # 获取游标
# sql = '''
#     create table company
#         (id int primary key not null,
#         name text not null,
#         age int not null,
#         address char(50),
#         salary real);
#
# '''
# c.execute(sql)    # 执行sql语句
# conn.commit()     # 提交数据库操作
# conn.close()      # 关闭数据库连接
#
# print("成功建表")

# 插入数据
conn = sqlite3.connect("test.db")  # 打开或创建数据库文件

print("Opened database successfully")
c = conn.cursor()   # 获取游标
# sql1 = '''
#     insert into company (id,name,age,address,salary)
#     values (1,"张三",32,"成都",9000);
# '''
# sql2 = '''
#     insert into company (id,name,age,address,salary)
#     values (2,"李四",32,"四川",8000);
# c.execute(sql1)
# c.execute(sql2)  # 执行sql语句
# conn.commit()     # 提交数据库操作
# print("插入完毕")
# '''
sql = "select id,name,address,salary from company"
cursor = c.execute(sql)
for row in cursor:
    print("id = ", row[0])
    print("name = ", row[1])
    print("address = ", row[2],"\n")
print("查询完毕")
conn.close()      # 关闭数据库连接










