#coding=utf-8

#导入urllib包
import urllib
#导入bs4包
from bs4 import BeautifulSoup

#打开目标网址主目录
htmlfrist = urllib.urlopen("http://pingguo7.com/")
soup = BeautifulSoup(htmlfrist)

#获取目标网址二级目录的链接
soupContent = soup.select(".index-title span a ")
moreContentStr = str(soupContent[0])
leftCharIndex = moreContentStr.find('http')
rightCharIndex = moreContentStr.rfind('/"')
moreHTML = moreContentStr[leftCharIndex:rightCharIndex]

#打开目标网址二级目录的链接
htmlsecond = urllib.urlopen(moreHTML)
soup = BeautifulSoup(htmlsecond)
priceEveryDay = soup.select(".content ul li")

for price in priceEveryDay:
	
	#转换为字符串
	tempStr = str(price)
	#获取三级目录的网址
	priceLeftCharIndex = tempStr.find('http')
	priceRightCharIndex = tempStr.rfind('.html')
	priceHTML = tempStr[priceLeftCharIndex:priceRightCharIndex+5]
	# print priceHTML

	#打开链接获取数据
	#出现乱码的位置↓
	htmlPrice = urllib.urlopen(priceHTML)
	soup = BeautifulSoup(htmlPrice)
	strTemp = 'u'+str(soup.select('title'))
	print strTemp.encode('raw_unicode_escape')
	#
	#测试第一条数据，所以用了break
	break






