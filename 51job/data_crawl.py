# -*- CODING = utf-8 -*-
# @TIME :  17:52
# @Author ： hwy
# @File : data_crawl.py
# @Software : PyCharm 17:52
"""制作流程
1 爬取数据  爬取列表 爬取详情  【可以先爬取一个页面测试代码，分析爬取到的html文件，再想办法解析，而不是一直爬取页面。这是调试技巧】
2 数据保存  保存列表 保存详情
3 搭建框架 app.py 路由 templates  页面  static 素材 图片 css js
前端页面 列表显示 表达制作
4 制作图表 Echarts  echarts.js柱形图 饼形图  WordCloud
"""
from bs4 import BeautifulSoup
import re
import urllib.request
import xlwt
import sqlite3


def main():
    # jobURLs = getURLs(pagenum)
    # for url in jobURLs:
    #     getData(url)
    # datalist = getData(baseurl)
    # dbpath = "./51job.db"
    # saveData2DB(datalist, dbpath)
    url = "https://search.51job.com/list/200200,000000,0000,00,9,99,python,2,1.html"
    html = askURL(url)
    print(html)



def getData(baseurl):
    datalist = []


def askURL(url):
    head = {  # 模拟浏览器头部信息
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36"
    }  # 用户代理 表示自己不是爬虫，而是浏览器身份标识，本质是告诉浏览器我们能接受什么水平的文件
    request = urllib.request.Request(url, headers=head)
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("gbk")
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
    return html


def getJobLink():
    pass



def saveData2DB(datalist, dbpath):
    init_db(dbpath)
    conn = sqlite3.connect(dbpath)
    cur = conn.cursor()
    for data in datalist:
        for index in range(len(data)):  # 给数据加引号拼装
            if index == 4 or index == 5:
                continue
            data[index] = '"' + data[index] + '"'

        # 每拼好一个存一次，注意在一个for循环里
        sql = '''
                insert into movie250 (
                info_link,pic_link,cname,
                ename,score,rated,
                introduction,info
                )
                values(%s)
            ''' % ",".join(data)
        # print(sql) # 调试时可以打印出来复制到sql中执行
        cur.execute(sql)
        conn.commit()
    cur.close()
    conn.close()


def init_db(dbpath):
    sql = '''
    create table 51job
    (
    id integer primary key autoincrement,
    job_link text,
    job_name text,
    com_name varchar,
    area varchar,
    salary text,
    edu text,
    info text
    )
    '''  # 创建数据表
    conn = sqlite3.connect(dbpath)
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()


if __name__ == "__main__":
    main()
