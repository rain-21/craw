# -*- coding = utf-8 -*-
# @TIME :  15:16
# @Author ： hwy
# @File : douban.py
# @Software : PyCharm 15:16

# def main():
#     print("hello")
# if __name__ == "__main__":
#     # 调用函数，控制流程，保证入口
#     main()
# 灰的是因为没有调用
from bs4 import BeautifulSoup  # 网页解析，数据获取
import re  # 正则表达式
import urllib.request  # 制定URL 获取网页数据
import xlwt  # 进行excel操作
import sqlite3  # 操作sqlite数据库操作


def main():
    baseurl = "https://movie.douban.com/top250?start="
    # 1 爬取网页
    datalist = getData(baseurl)
    savepath = "豆瓣电影top250.xls"
    # 3 保存数据到excel
    saveData(datalist, savepath)
    # 3 保存数据到数据库
    dbpath = "movie.db"
    saveData2DB(datalist, dbpath)


# 定义规则
# 影片详情连接的规则
findLink = re.compile(r'<a href="(.*?)">')  # 创建正则表达式对象，表达规则
# 图片连接的规则
findImgSrc = re.compile(r'<img.*src="(.*?)"', re.S)  # re.S 忽略换行
# 影片的片名
findTitle = re.compile(r'<span class="title">(.*)</span>')
# 影片的评分
findRating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
# 找到评价人数
findJudge = re.compile(r'<span>(\d*)人评价</span>')
# 找到概况
findInq = re.compile(r'<span class="inq"(.*)</span>')
# 找到影片的相关内容
findBd = re.compile(r'<p class="">(.*?)</p>', re.S)


# 爬取网页
def getData(baseurl):
    datalist = []
    for i in range(0, 10):  # 调用十次，250条
        url = baseurl + str(i * 25)
        html = askURL(url)  # 保存获取的网页源码
        # 2逐个解析数据
        soup = BeautifulSoup(html, "html.parser")
        for item in soup.find_all("div", class_="item"):  # 查找符合要求的字符串，形成列表
            # print(item) # 测试：查看电影贴膜全部信息
            data = []  # 保存一部电影所有信息
            item = str(item)
            # print(item)
            # break
            # 影片详情的超链接
            link = re.findall(findLink, item)[0]  # re库通过正则表达式查找指定字符串
            # print(link)
            data.append(link)  # 添加链接

            imgSrc = re.findall(findImgSrc, item)[0]
            data.append(imgSrc)  # 添加图片

            titles = re.findall(findTitle, item)  # 片名可能只有一个
            if len(titles) == 2:
                ctitile = titles[0]
                data.append(ctitile)  # 添加中文名
                otitle = titles[1].replace("/", "")  # 去掉无关的符号
                data.append(otitle)  # 添加外国名
            else:
                data.append(titles[0])
                data.append('')  # 外文名留空 防止错位

            rating = re.findall(findRating, item)[0]
            data.append(rating)  # 加评分

            judge = re.findall(findJudge, item)[0]
            data.append(judge)  # 加评价人数

            inq = re.findall(findInq, item)
            if len(inq) != 0:
                inq = inq[0].replace("。", "")
                data.append(inq)  # 添加概述
            else:
                data.append(" ")  # 留空

            bd = re.findall(findBd, item)[0]
            bd = re.sub('<br(\s+)?/>(\s+)?', " ", bd)  # 去掉br
            bd = re.sub('/', " ", bd)  # 替换去掉/
            data.append(bd.strip())  # 去掉前后的空格

            datalist.append(data)  # 把处理好的一部电影的数据放入datalist
    # print(datalist)
    return datalist


# 得到指定的一个url的网页内容
def askURL(url):
    # 少就用键值对，多就用列表
    head = {  # 模拟浏览器头部信息
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36"
    }  # 用户代理 表示自己不是爬虫，而是浏览器身份标识，本质是告诉浏览器我们能接受什么水平的文件
    request = urllib.request.Request(url, headers=head)
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
        # print(html)
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
    return html


# 3 保存数据到excel
def saveData(datalist, savepath):
    book = xlwt.Workbook(encoding="utf-8")  # 创建workbook 对象
    sheet = book.add_sheet("豆瓣电影250", cell_overwrite_ok=True)  # 创建工作表
    col = ("电影详情链接", "图片链接", "影片中文名", "外文名", "评分", "评价数", "概况", "相关信息")
    for i in range(0, len(col)):
        sheet.write(0, i, col[i])
    for i in range(0, 250):
        print("第%d条" % i)
        data = datalist[i]
        for j in range(0, 8):
            sheet.write(i + 1, j, data[j])  # 写入数据
    book.save("savepath")  # 保存数据表
    pass


# 3 保存数据到数据库
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


# 初始化数据库
def init_db(dbpath):
    sql = '''
    create table movie250
    (
    id integer primary key autoincrement,
    info_link text,
    pic_link text,
    cname varchar,
    ename varchar,
    score numeric,
    rated numeric,
    introduction text,
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
    # 调用函数，控制流程，保证入口

    # init_db("movietest.db")   # 测试sqlite语句
    main()
