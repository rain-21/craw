# -*- CODING = utf-8 -*-
# @TIME :  21:56
# @Author ： hwy
# @File : douban_flask.py
# @Software : PyCharm 21:56

from flask import Flask, render_template  # 导入渲染模版
import sqlite3

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/index')
def index1():
    # return render_template("index.html")
    return index()


@app.route('/movie')
def movie():
    datalist = []
    con = sqlite3.connect("movie.db")
    cur = con.cursor()
    sql = "select * from movie250"
    data = cur.execute(sql)
    for item in data:
        datalist.append(item)
    cur.close()
    con.close()
    return render_template("movie.html", movies=datalist)


@app.route('/team')
def team():
    return render_template("team.html")


@app.route('/word')
def word():
    return render_template("word.html")


@app.route('/score')
def score():
    score = []  # 评分
    num =[]   # 评分的数量
    con = sqlite3.connect("movie.db")
    cur = con.cursor()
    sql = "select score,count(score) from movie250 group by score"
    data = cur.execute(sql)
    for item in data:
        score.append(item[0])
        num.append(item[1])
    cur.close()
    con.close()
    return render_template("score.html",score=score,num=num)




if __name__ == '__main__':
    app.run(debug=True)  # 开启debug模式
