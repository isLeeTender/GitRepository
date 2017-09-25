import matplotlib.pyplot as plt
from wordcloud import WordCloud
import jieba
 
text_from_file_with_apath = open('./love.txt').read()
 
wordlist_after_jieba = jieba.cut(text_from_file_with_apath, cut_all = True)
wl_space_split = " ".join(wordlist_after_jieba)
 
my_wordcloud = WordCloud( font_path='/Library/Fonts/Microsoft/SimHei.ttf',#设置字体
                background_color="white", #背景颜色
                max_words=2000,# 词云显示的最大词数
                #mask=back_coloring,#设置背景图片
                max_font_size=60, #字体最大值
                random_state=42,
                )

my_wordcloud.generate(wl_space_split)
 
plt.imshow(my_wordcloud)
plt.axis("off")
plt.show()