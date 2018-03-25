# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
from scrapy import log
import read_url
from CodeEye import settings
from CodeEye.items import CodeeyeItem

class CodeeyePipeline(object):
    def __init__(self):
        self.connect = pymysql.connect(
            host=settings.MYSQL_HOST,
            db=settings.MYSQL_DBNAME,
            user=settings.MYSQL_USER,
            passwd=settings.MYSQL_PASSWD,
            port = settings.MYSQL_PORT,
            charset='utf8mb4',
            )
        self.cursor = self.connect.cursor()
    def process_item(self, item, spider):
        if item.__class__ == CodeeyeItem:
            sql_insert = 'insert into coin_github(coin_id,coin_name,name,base_url,type,description,language,core_code,watch,star,fork,issues,pull_requests,projects,commits,branches,releases,contributors,updated_at,created_at,pushed_at) values("%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s")' % (item['coin_id'],item['coin_name'],item['name'],item['base_url'],item['type'],item['description'],item['language'],item['core_code'], item['watch'], item['star'], item['fork'],item['issues'], item['pull_requests'], item['projects'], item['commits'], item['branches'],item['releases'], item['contributors'], item['updated_at'][0],item['created_at'][0],item['pushed_at'])
            self.cursor.execute(sql_insert)
            self.connect.commit()
            print('successful')
            return item

        
        else:
            pass


