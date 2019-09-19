# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CrawlEverythingItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #内容来源网站
    jk_source = scrapy.Field()
    # 文章标题
    jk_title = scrapy.Field()
    # 文章链接
    jk_url = scrapy.Field()
    # 文章时间有可能没有
    jk_date = scrapy.Field()
    jk_remark=scrapy.Field()

