# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LianjiaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    pattern = scrapy.Field()
    title = scrapy.Field()
    location = scrapy.Field()
    direction = scrapy.Field()
    money = scrapy.Field()
    year = scrapy.Field()
    lastupdate = scrapy.Field()
    url = scrapy.Field()
    pass
