# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SpiderProjectItem(scrapy.Item):
    # define the fields for your item here like:
    taskid = scrapy.Field()
    data = scrapy.Field()
