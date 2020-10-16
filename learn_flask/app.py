# -*- CODING = utf-8 -*-
# @TIME :  17:45
# @Author ： hwy
# @File : app.py
# @Software : PyCharm 17:45
from flask import Flask, render_template, request  # 导入渲染模版
import datetime

app = Flask(__name__)

# 1.定义路径



# 路由解析，通过用户访问的路径，匹配相应的函数
# @app.route('/')
# def hello_world():
#     return 'hello world!'

@app.route('/index1')
def hello():
    return '您好'
# 路由路径不能重复 用户只能通过唯一路径来访问特定的函数
# 通过用户访问的路径，获取用户的字符串
@app.route('/user/<name>')
def welcome(name):
    return '您好,%s' % name


# 通过用户访问的路径，获取用户的整形参数    当然还有float类型
@app.route('/user/<int:id>')
def welcome_huiyuan(id):
    return '您好,会员%d' % id


# 2.返回给用户渲染后的网页文件

@app.route("/")
def index2():
    return render_template("index_test.html")


# 向页面传递一个变量
@app.route("/var")
def index3():
    time = datetime.date.today()    # 普通变量
    name = ["xz", "xw", "xl"]       # 列表类型变量
    task = {"任务": "打扫卫生", "时间": "3h"}  # 字典类型变量
    return render_template("index_test.html", var=time, list=name, task=task)

# 表单提交
@app.route("/test/register")
def register():
    return  render_template("test/register.html")
# 接收端的路由必须定制methods为post
@app.route("/result",methods=["POST", "GET"])
def result():
    if request.method == "POST":
        result = request.form  # result 其实转成字典
        return render_template("test/result.html", result=result)
    else:
        pass


if __name__ == '__main__':
    app.run(debug=True)  # 开启debug模式
