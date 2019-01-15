import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import jieba
 
text_from_file_with_apath = open('/Users/wsm/WorkSpace/Python/test.txt').read()
font = 'simfang.ttf'
wordlist_after_jieba = jieba.cut(text_from_file_with_apath, cut_all = True)
wl_space_split = " ".join(wordlist_after_jieba)
 
my_wordcloud = WordCloud(font_path=font).generate(wl_space_split)
 
plt.imshow(my_wordcloud)
plt.axis("off")
plt.show()
 
