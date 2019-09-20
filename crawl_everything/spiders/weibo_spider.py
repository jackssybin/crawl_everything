# -*- coding: utf-8 -*-
import scrapy
from crawl_everything.items import CrawlEverythingItem


class WeiboSpiderSpider(scrapy.Spider):
    name = 'weibo_spider'
    allowed_domains = ['s.weibo.com']
    start_urls = ['https://s.weibo.com/top/summary']

    def parse(self, response):
        trends = response.css('td.td-02 > a')
        for trend in trends:
            item = CrawlEverythingItem()
            item['jk_source'] = 'weibo_spider'
            item['jk_title'] = trend.css('a::text').extract_first()
            href =self.get_href(trend)
            item['jk_url'] = "https://s.weibo.com"+href
            item['jk_remark'] = ''

            yield item

    def get_href(self,trend):
        href = trend.css('a').attrib['href']
        if href.startswith('javascript'):  ##javascript:void(0)
            href = trend.css('a').attrib['href_to']
        return href