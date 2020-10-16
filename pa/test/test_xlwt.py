#-*- CODING = utf-8 -*-
#@TIME :  23:52
#@Author ： hwy
#@File : test_xlwt.py
#@Software : PyCharm 23:52

import xlwt

workbook = xlwt.Workbook(encoding="utf-8")   # 创建workbook 对象
worksheet = workbook.add_sheet("sheet1")     # 创建工作表
for i in range(1, 256):                       # 写入数据，行，列，内容
    for num in range(1, i + 1):
        a = i * num
        worksheet.write(i-1, num-1, "%d*%d=%d" % (i, num, a))

workbook.save("stu.xls")   # 保存数据表

