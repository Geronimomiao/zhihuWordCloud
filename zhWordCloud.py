# 解决 mac 无法使用 matplotlib
import matplotlib
matplotlib.use('TkAgg')

from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import jieba


class ZhiHuWordCloud(object):
    def __init__(self, questionid, picname):
        # 问题ID
        self.questionid = questionid

        # 设置默认字体集
        self.font = 'simfang.ttf'

        # 设置词云 背景图片
        self.d = path.dirname(__file__)
        self.bg_coloring = np.array(Image.open(path.join(self.d, picname)))

        # 使用 图片的背景色
        self.image_colors = ImageColorGenerator(self.bg_coloring)

        # 停词表 过滤文本中 不需要展示却高频的词语
        self.stopwords = ([
            "然而","这样","但是","因此","我们","一个","如果",'很多',
            '它们','具有','人们','可以','这个','这种','不能','因为',
            '或者','没有','这些','一种','非常','干货','他们','而且',
            '所有','也许','知乎','东西','不要','优质','确定','所以',
            '任何','发生','比如','能够','过去','对于','知道','这是',
            '现在','不同','时候','然后','还是','变得','什么','不是',
            '那么','一点','已经','之间','如何','仍然','喜欢','自己',
            '就是','觉得','开始','各种','变强','强大','不会','一样',
            '真的','一样','其实','那个','而是','一样','一些','可能',
            '问题','人生','意义','在于','只有','来说','生命','生活',
            '认为','世界','人类','优秀','事情','','','','','','','','','','','',
        ])

        # 获取文本内容 以生成词云
        with open('text/' + self.questionid + '.txt', 'rb') as f:
            self.contents = f.read()

        self.wordlist_after_jieba = jieba.cut(self.contents)
        self.wl_space_split = " ".join(self.wordlist_after_jieba)

    def run(self):
        wc = WordCloud(
            font_path=self.font,
            width=600,
            height=1200,
            background_color="white",
            margin=2,
            mask=self.bg_coloring,
            stopwords=self.stopwords
        ).generate(self.wl_space_split)

        # 使用 图片的背景色 做图片背景色
        plt.imshow(wc.recolor(color_func=self.image_colors))
        plt.axis("off")
        plt.show()

        wc.to_file("img/"+ self.questionid +".png")


if __name__ == '__main__':
    ZhiHuWordCloud('21650774', 'test4.jpg').run()


