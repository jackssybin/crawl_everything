# coding: utf-8
from scrapy.cmdline import execute
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# execute(['scrapy', 'crawl', 'douban_spider'])  # 你需要将此处的douban_spider替换为你自己的爬虫名称

# execute(['scrapy', 'crawl', 'weibo_spider'])  # 你需要将此处的douban_spider替换为你自己的爬虫名称

execute(['scrapy', 'crawl', 'crawl_everything_spider'])  # 你需要将此处的douban_spider替换为你自己的爬虫名称

