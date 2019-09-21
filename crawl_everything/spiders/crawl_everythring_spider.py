# -*- coding: utf-8 -*-
import scrapy
from crawl_everything.items import CrawlEverythingItem
import json #引用json模块
import re
class crawlEverythingSpiderSpider(scrapy.Spider):
    name = 'crawl_everything_spider'
    start_urls = [
        'https://www.douban.com/gallery/',#豆瓣
        'https://s.weibo.com/top/summary',#微博
        'http://tieba.baidu.com/hottopic/browse/topicList?res_type=1&red_tag=h1923737578',  # 百度贴吧
        'https://bbs.hupu.com/all-gambia',  # 虎扑
        'https://github.com/trending',  # github
        'http://top.baidu.com/buzz?b=341&c=513&fr=topbuzz_b1_c513',  # 百度今日热点
    ]

    def parse(self, response):
        if response.url == self.start_urls[0]:#豆瓣
            yield from self.crawl_douban(response)
        if response.url == self.start_urls[1]:  # 微博
            yield from self.crawl_weibo(response)
        if response.url == self.start_urls[2]:  # 百度贴吧
            yield from self.crawl_tieba(response)
        if response.url == self.start_urls[3]:  # 虎扑
            yield from self.crawl_hupu(response)
        if response.url == self.start_urls[4]:  # github
            yield from self.crawl_github(response)
        if response.url == self.start_urls[5]:  # 百度今日热点
            yield from self.crawl_topbaidu(response)


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

    def crawl_tieba(self, response):
        trends = response.css('div.main > ul > li  a')
        for trend in trends:
            item = CrawlEverythingItem()
            item['jk_source'] = 'tieba_spider'
            item['jk_title'] = trend.css('a::text').extract_first()
            item['jk_url'] = trend.css('a').attrib['href']
            item['jk_remark'] = ''
            yield item

    def crawl_hupu(self, response):
        trends = response.css('div.list> ul > li >span:nth-child(1) >a')
        for trend in trends:
            item = CrawlEverythingItem()
            item['jk_source'] = 'hupu_spider'
            item['jk_title'] = trend.css('a').attrib['title']
            item['jk_url'] ="https://bbs.hupu.com"+trend.css('a').attrib['href']
            item['jk_remark'] = ''
            yield item

    def crawl_github(self, response):
        trends = response.css('div> article.Box-row ')
        for trend in trends:
            item = CrawlEverythingItem()
            item['jk_source'] = 'github_spider'
            jk_title="".join(trend.css('p::text').extract())
            re.sub(r'[\\*|“<>:/()（）0123456789]', '', jk_title)
            jk_title.replace('\n', '').replace('  ', '')
            item['jk_title'] = jk_title
            item['jk_url'] = "https://github.com" + trend.css('h1>a').attrib['href']
            item['jk_remark'] = ''
            yield item

    def crawl_topbaidu(self, response):
        trends = response.css('td.keyword >a:nth-child(1) ')
        for trend in trends:
            item = CrawlEverythingItem()
            item['jk_source'] = 'topbaidu_spider'
            item['jk_title'] = trend.css('a::text').extract_first()
            item['jk_url'] = trend.css('a').attrib['href']
            item['jk_remark'] = ''
            yield item



    def get_weibo_href(self,trend):
        href = trend.css('a').attrib['href']
        if href.startswith('javascript'):  ##javascript:void(0)
            href = trend.css('a').attrib['href_to']
        return href