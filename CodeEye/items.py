# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CodeeyeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    coin_id = scrapy.Field()
    coin_name = scrapy.Field()
    name = scrapy.Field()
    base_url = scrapy.Field()
    type = scrapy.Field()
    description = scrapy.Field()
    language = scrapy.Field()
    core_code = scrapy.Field()
    watch = scrapy.Field()
    star = scrapy.Field()
    fork = scrapy.Field()
    issues = scrapy.Field()
    pull_requests = scrapy.Field()
    projects = scrapy.Field()
    commits = scrapy.Field()
    branches = scrapy.Field()
    releases = scrapy.Field()
    contributors = scrapy.Field()
    updated_at = scrapy.Field()
    created_at = scrapy.Field()
    pushed_at = scrapy.Field()

    pass
