# -*- coding: utf-8 -*-
import scrapy
from crawl_everything.items import CrawlEverythingItem


class crawlEverythingSpiderSpider(scrapy.Spider):
    name = 'crawl_everything_spider'
    start_urls = [
        'https://www.douban.com/gallery/',#豆瓣
        'https://s.weibo.com/top/summary',#微博

    ]

    def parse(self, response):
        if response.url == self.start_urls[0]:#豆瓣
            yield from self.crawl_douban(response)
        if response.url == self.start_urls[1]:  # 微博
            yield from self.crawl_weibo(response)


    def crawl_douban(self, response):
        trends = response.css('ul.trend > li > a')
        for trend in trends:
            item = CrawlEverythingItem()
            item['jk_source'] = 'douban_spider'
            item['jk_title'] = trend.css('a::text').extract_first()
            item['jk_url'] = trend.css('a').attrib['href']
            item['jk_remark'] = ''
            yield item

    def crawl_weibo(self, response):
        trends = response.css('td.td-02 > a')
        for trend in trends:
            item = CrawlEverythingItem()
            item['jk_source'] = 'weibo_spider'
            item['jk_title'] = trend.css('a::text').extract_first()
            href = self.get_weibo_href(trend)
            item['jk_url'] = "https://s.weibo.com" + href
            item['jk_remark'] = ''
            yield item

    def get_weibo_href(self,trend):
        href = trend.css('a').attrib['href']
        if href.startswith('javascript'):  ##javascript:void(0)
            href = trend.css('a').attrib['href_to']
        return href