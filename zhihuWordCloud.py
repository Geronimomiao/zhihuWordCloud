# 解决 mac 无法使用 matplotlib
import matplotlib

matplotlib.use('TkAgg')

from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import jieba

# 设置默认字体集
font = 'simfang.ttf'

# 设置词云 背景图片
d = path.dirname(__file__)
bg_coloring = np.array(Image.open(path.join(d, "t11.png")))

# 使用 图片的背景色
image_colors = ImageColorGenerator(bg_coloring)

with open('test.txt', 'rb') as f:
    contents = f.read()

wordlist_after_jieba = jieba.cut(contents)
wl_space_split = " ".join(wordlist_after_jieba)

# 停词表 过滤文本中 不需要展示却高频的词语
stopwords = ([
    "然而","这样","但是","因此","我们","一个","如果",'很多',
    '它们','具有','人们','可以','这个','这种','不能','因为',
    '或者','没有','这些','一种','非常','干货','他们','而且',
    '所有','也许','知乎','东西','不要','优质','确定','所以',
    '任何','发生','比如','能够','过去','对于','知道','这是',
    '现在','不同','时候','然后','还是','变得','什么','不是',
    '那么','一点','已经','之间','如何','仍然','喜欢','自己'
])


wc = WordCloud(
    font_path=font,
    width=600,
    height=1200,
    background_color="white",
    margin=2,
    mask=bg_coloring,
    stopwords=stopwords
).generate(wl_space_split)


# 使用 图片的背景色 做图片背景色
plt.imshow(wc.recolor(color_func=image_colors))
plt.axis("off")
plt.show()
