# -*- coding: utf-8 -*-
import scrapy


class EastmoneySpider(scrapy.Spider):
    name = 'eastmoney'
    allowed_domains = ['eastmoney.com']
    start_urls = ['http://quote.eastmoney.com/center/gridlist.html#hs_a_board']

    def parse(self, response):
        the_title = response.xpath('/html/head/title/text()').getall()
        print(the_title)
