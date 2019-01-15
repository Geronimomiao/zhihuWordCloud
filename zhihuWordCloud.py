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

wordlist_after_jieba = jieba.cut(contents, cut_all=True)
wl_space_split = " ".join(wordlist_after_jieba)

wc = WordCloud(
    font_path=font,
    width=1000,
    height=860,
    background_color="white",
    margin=2,
    mask=bg_coloring
).generate(wl_space_split)


# 使用 图片的背景色 做图片背景色
plt.imshow(wc.recolor(color_func=image_colors))
plt.axis("off")
plt.show()
