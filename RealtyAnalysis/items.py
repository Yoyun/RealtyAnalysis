# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class RealtyanalysisItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class XiaozhuItem(scrapy.Item):
    latlng = scrapy.Field()     # 坐标
    title = scrapy.Field()      # 标题
    price = scrapy.Field()      # 价格 每晚
    single = scrapy.Field()     # 单间 或整租
    bed = scrapy.Field()        # 床
    people = scrapy.Field()     # 宜住几人
    score = scrapy.Field()      # 评分
    comment = scrapy.Field()    # 点评数
