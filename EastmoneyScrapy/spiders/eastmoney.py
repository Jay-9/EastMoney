# -*- coding: utf-8 -*-
import scrapy
from ScrapyEastmoney.items import ScrapyeastmoneyItem
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider
import json


class EastmoneySpider(scrapy.Spider):
    name = 'eastmoney'
    allowed_domains = ['eastmoney.com']
    start_urls = ['http://quote.eastmoney.com/center/gridlist.html#hs_a_board']

    def parse(self, response):
        title = response.xpath('/html/head/title/text()').getall()
        # print(the_title)
        item = ScrapyeastmoneyItem(title=title)
        yield item
