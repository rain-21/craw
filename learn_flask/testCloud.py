# -*- CODING = utf-8 -*-
# @TIME :  14:37
# @Author ： hwy
# @File : testCloud.py
# @Software : PyCharm 14:37

import jieba  # 分词
from matplotlib import pyplot as plt  # 绘图  可视化
from wordcloud import wordcloud, WordCloud  # 词云
from PIL import Image  # 图片处理
import numpy as np  # 矩阵运算
import sqlite3  # 数据库

# 准备词云所需的文字
con = sqlite3.connect('movie.db')
cur = con.cursor()
sql = "select introduction from movie250"
data = cur.execute(sql)
text = ""  # 将字符串连起来
for item in data:
    # print(item[0])
    text = (text + item[0]).replace(">", "")
# print(text)
cur.close()
con.close()


# 分词
cut = jieba.cut(text)
string = " ".join(cut)
# print(string)

# 绘图
img = Image.open(r'static\assets\img\tree.jpg')
img_array = np.array(img)   # 将图片转化为数组
wc = WordCloud(
    background_color = "white",
    mask = img_array,
    font_path = "SIMLI.TTF",   # 字体所在位置c:/windows/Fonts
)
wc.generate_from_text(string)

# 绘制图片
fig = plt.figure(1)
plt.imshow(wc)
plt.axis("off")  # 是否显示坐标轴
# plt.show()  # 显示图片
# 输出图片到文件
plt.savefig(r'.\static\assets\img\word.jpg', dpi=1200)







