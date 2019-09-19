# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import  pymysql
import datetime;
import sys;
reload(sys);
sys.setdefaultencoding("utf8")

class CrawlEverythingPipeline(object):
    def __init__(self):
        # 连接MySQL数据库
        self.connect = pymysql.connect(host='localhost', user='root', password='root1234', db='crawl_everything', port=3307)
        self.cursor = self.connect.cursor()

    def process_item(self, item, spider):
        # 往数据库里面写入数据
        self.cursor.execute(
            'INSERT INTO crawl_everything.article_info( jk_source, jk_title, jk_url, jk_remark, jk_create) '
            'VALUES("{}","{}","{}","{}","{}")'.format(item['jk_source'], item['jk_title'],item['jk_url'],item['jk_remark'],datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        )
        self.connect.commit()
        return item
        # 关闭数据库

    def close_spider(self, spider):
        self.cursor.close()
        self.connect.close()

