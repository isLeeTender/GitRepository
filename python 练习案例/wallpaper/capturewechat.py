# -*- coding:utf-8 -*-
import itchat
import re
import jieba
import matplotlib.pyplot as plt
from wordcloud import WordCloud,ImageColorGenerator
import numpy as np
import PIL.Image as Image
from os import path
from scipy.misc import imread

itchat.auto_login()

friends = itchat.get_friends(update=True)[0:]

#获取好友性别信息
male = female = other = 0

for i in friends[1:]:
	sex = i['Sex']
	if sex == 1:
		male += 1
	elif sex == 2:
		female +=1
	else:
		other +=1

total = len(friends[1:])

print('男生好友：%.2f%%' % (float(male)/total*100) + '\n' +
'女生好友：%.2f%%' % (float(female)/total*100) + '\n' +
'不明性别好友：%.2f%%' % (float(other)/total*100) + '\n' )

# str = itchat.get_friends(update=True)[0]

# print(str)

# #获取好友签名信息
# siglist = []

# for i in friends:
# 	signature = i['Signature'].strip().replace('span','').replace('class','').replace('emoji','')
# 	rep = re.compile('1f\d+\w*|[<>/=]')
# 	signature = rep.sub('',signature)
# 	siglist.append(signature)

# text = ''.join(siglist)

# #写入本地文件
# textfile = open('info.txt','w')
# textfile.write(text)
# text_from_file_with_apath = open('./info.txt').read()
# wordlist = jieba.cut(text_from_file_with_apath, cut_all = True)
# word_space_split = " ".join(wordlist)


# #画图
# coloring = plt.imread('./haha.jpg')
# my_wordcloud = WordCloud(background_color='white',
# 						max_words=2000,
# 						mask=coloring,
# 						max_font_size=100,
# 						random_state=42,
# 						font_path='/Library/Fonts/Microsoft/SimHei.ttf').generate(word_space_split)
						
# image_colors = ImageColorGenerator(coloring)

# plt.imshow(my_wordcloud)
# plt.axis('off')
# plt.show()

# # 保存图片
# my_wordcloud.to_file(path.join(d, "签名.png"))

#发送信息给自己
#itchat.send_msg(text)