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

class LianjiaItem(scrapy.Item):
    title_main = scrapy.Field()     # 主标题
    title_sub = scrapy.Field()      # 副标题
    price_total = scrapy.Field()    # 价格
    price_unit = scrapy.Field()     # 单位
    tips = scrapy.Field()           # 标签
    area = scrapy.Field()           # 面积
    house_type = scrapy.Field()     # 户型
    storey = scrapy.Field()         # 楼层
    direction = scrapy.Field()      # 朝向
    court = scrapy.Field()          # 小区
    location = scrapy.Field()       # 位置

