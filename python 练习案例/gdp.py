#coding=utf-8

#导入urllib包
import urllib
#导入bs4包
from bs4 import BeautifulSoup

def getNewsTitle(html):

	htmlfrist = urllib.urlopen(html)
	soup = BeautifulSoup(htmlfrist)
	soupContent = soup.select(".right_box span a")

	i = 1
	for content in soupContent:
		stringt = str(content)
		leftCharIndex = stringt.find('title="')
		rightCharIndex = stringt.find("</a>")
		# print("第%d条新闻:"%i)
		# print(stringt[leftCharIndex+7:rightCharIndex])
		# print('\n')
		i+=1

	#select = raw_input('是否感兴趣？(输入1：打印出来我看看  输入其他：我不感兴趣）：')
	select = '1'
	if select == '1':
		#获取新闻内容链接
		getNewsContent(soup)
		
	else:
		pass

def getNewsContent(soup):
	#获取新闻内容链接
	soupContent = soup.select(".right_box span")
	
	for urlString in soupContent:
		#获取新闻链接
		urlString = str(urlString).decode('unicode-escape')
		leftCharIndex = urlString.find('href=')
		rightCharIndex = urlString.find('.shtml')
		newsURL = urlString[leftCharIndex+6:rightCharIndex+6]
	
		#打开新闻内容链接	
		newsHtmlString = 'http://www.gdptc.cn/'+newsURL
		if(newsHtmlString.endswith('.shtml')):
			# print newsHtmlString		
			newsHtml = urllib.urlopen(newsHtmlString)
			soup = BeautifulSoup(newsHtml)
			soupContent = soup.select(".content")
			for paragraph in soupContent:
				item = paragraph.replace("<p>", "").replace("</p>", "").replace("<br />", "")
            	print paragraph.replace("<p>", "").replace("</p>", "").replace("<br />", "")
            
			
			#print str(soupContent).decode('unicode-escape')
			# urllib.urlretrieve
			# break


		#获取新闻数据
		#将新闻数据保存到本地

#打开目标网址主目录
urlString = "http://www.gdptc.cn/News-187.shtml"
getNewsTitle(urlString)
	




# print stringt.decode('unicode-escape')

# moreContentStr = str(soupContent[0])
# leftCharIndex = moreContentStr.find('http')
# rightCharIndex = moreContentStr.rfind('/"')
# moreHTML = moreContentStr[leftCharIndex:rightCharIndex]

# #打开目标网址二级目录的链接
# htmlsecond = urllib.urlopen(moreHTML)
# soup = BeautifulSoup(htmlsecond)
# priceEveryDay = soup.select(".content ul li")

# for price in priceEveryDay:
	
# 	#转换为字符串
# 	tempStr = str(price)
# 	#获取三级目录的网址
# 	priceLeftCharIndex = tempStr.find('http')
# 	priceRightCharIndex = tempStr.rfind('.html')
# 	priceHTML = tempStr[priceLeftCharIndex:priceRightCharIndex+5]
# 	# print priceHTML

# 	#打开链接获取数据
# 	#出现乱码的位置↓
# 	htmlPrice = urllib.urlopen(priceHTML)
# 	soup = BeautifulSoup(htmlPrice)
# 	strTemp = 'u'+str(soup.select('title'))
# 	print strTemp.encode('raw_unicode_escape')
# 	#
# 	#测试第一条数据，所以用了break
# 	break






