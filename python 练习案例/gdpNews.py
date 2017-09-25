#-*- coding:utf-8 -*-

import scrapy

from mySpider.items import gdptcNews

class GdpNewsScrapy(scrapy.spiders.Spider):
	name = 'gdpNews'
	start_urls = ['http://www.gdptc.cn/News-187.shtml']

	def parse(self,response):
		# filename = 'News.html'
		# open(filename,'w').write(response.body)
		# file = open('gdpNews.txt','w')

		items = []
		# for site in response.xpath('//div[@style="height: 20px; padding-top: 6px;"]'):
		for site in response.xpath('//span[@style="float: left;"]'):
			
			item = gdptcNews()

			news_title = site.xpath('a/text()').extract()
			unicode_news_title =news_title[0].encode('utf-8')
			# file.write(news_title[0].encode('utf-8'))
			# print unicode_news_title
			item['title'] = unicode_news_title
			items.append(item)

		

		return items
		# file.close()


