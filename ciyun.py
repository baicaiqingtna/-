#!/usr/bin/python
#encoding:utf-8
import itchat as it
it.login()
friends=it.get_friends(update=True)[0:]
print(type(friends))
import re
siglist = []
for i in friends:#将截取的个性签名写入文件，name为text
    signature = i["Signature"].strip().replace('span','').replace('class','').replace('emoji','').replace('\n','')
    rep = re.compile("1f\d+\w*|[<>/=]")
    signature = rep.sub("", signature)
    siglist.append(signature)
text = "".join(siglist)
#分词 将text文件中的文字进行拆分，组成一个新的文字组
import jieba
wordlist = jieba.cut(text, cut_all=True)
word_space_split = " ".join(wordlist)
print(word_space_split)
#绘制词云
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator
import numpy as np
import PIL.Image as Image
coloring = np.array(Image.open("timg.jpg"))#自定义词云的图片
my_wordcloud = WordCloud(background_color="white", max_words=2000,
                         mask=coloring, max_font_size=60, random_state=42,font_path='simhei.ttf',scale=2).generate(word_space_split)

image_colors = ImageColorGenerator(coloring)
plt.imshow(my_wordcloud.recolor(color_func=image_colors))
plt.imshow(my_wordcloud)
plt.axis("off")
plt.show()
