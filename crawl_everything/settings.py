# -*- coding: utf-8 -*-

BOT_NAME = 'crawl_everything'

SPIDER_MODULES = ['crawl_everything.spiders']
NEWSPIDER_MODULE = 'crawl_everything.spiders'


USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.54 Safari/536.5'

ROBOTSTXT_OBEY = False
# 下载延时
DOWNLOAD_DELAY = 0.5

ITEM_PIPELINES = {
   'crawl_everything.pipelines.CrawlEverythingPipeline': 400
}