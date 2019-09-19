# -*- coding: utf-8 -*-
import scrapy
from crawl_everything.items import CrawlEverythingItem

class DoubanSpiderSpider(scrapy.Spider):
    name = 'douban_spider'
    allowed_domains = ['www.douban.com']
    start_urls = ['https://www.douban.com/gallery/']

    def parse(self, response):
        trends=response.css('ul.trend > li > a')
        for trend in trends:
            item = CrawlEverythingItem()
            item['jk_source']='douban_spider'
            item['jk_title']=trend.css('a::text').extract_first()
            item['jk_url'] = trend.css('a').attrib['href']
            item['jk_remark'] = ''

            yield item

