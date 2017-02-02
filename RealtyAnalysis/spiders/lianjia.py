# -*- coding: UTF-8 -*-

import string
import json
import scrapy
from RealtyAnalysis.items import LianjiaItem

class LianJiaSpider(scrapy.Spider):
    name = 'lianjia'
    allowed_domains = ['sz.lianjia.com']
    start_urls = [
        'http://sz.lianjia.com/zufang/'
    ]
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Referer': 'http://sz.lianjia.com/zufang/'
    }

    curPage = -1
    totalPage = -1

    def parse(self, response):
        print '======', response.url
        # 获取分页数据
        if (self.totalPage == -1):
            page = response.css('div.house-lst-page-box::attr(page-data)')[0].extract()
            page_json = json.loads(page)
            self.curPage = page_json['curPage']
            self.totalPage = page_json['totalPage']
            # 页数限制（测试）
            # self.totalPage = 2

        print '%d - %d' % (self.curPage, self.totalPage)

        # 抓取详情页
        house_lst = response.xpath('//*[@id="house-lst"]/li')
        for sel in house_lst:
            url = sel.xpath('div[2]/h2/a/@href').extract_first()
            yield scrapy.Request(url, callback=self.parse_detail, headers=self.headers)

        # 翻页
        if (self.curPage <= self.totalPage):
            print '====Next'
            self.curPage += 1
            url = '%spg%d/' % (self.start_urls[0], self.curPage)
            print url
            self.headers['Referer'] = url
            yield scrapy.Request(url, callback=self.parse, headers=self.headers)

    def parse_detail(self, response):

        print "------", response.url
        content = response.xpath('/html/body/div[@class="content-wrapper"]')[0]

        title_main = content.css('h1.main::text')[0].extract()
        title_sub = content.css('div.sub::text')[0].extract()
        price_total = content.css('span.total::text')[0].extract()
        price_unit = content.css('span.unit>span::text')[0].extract()
        tips = string.join(content.css('span.tips::text').extract(), ',')
        room = content.css('div.zf-room>p.lf::text').extract()
        area = room[0]
        house_type = room[1]
        storey = room[2]
        direction = room[3]

        court = content.css('div.zf-room>p')[5].css('a::text')[0].extract()

        location_lst = content.css('div.zf-room>p')[6].css('a::text').extract()
        location = string.join(location_lst, ' ')

        item = LianjiaItem()
        item['title_main'] = title_main
        item['title_sub'] = title_sub
        item['price_total'] = price_total
        item['price_unit'] = price_unit
        item['tips'] = tips
        item['area'] = area
        item['house_type'] = house_type
        item['storey'] = storey
        item['direction'] = direction
        item['court'] = court
        item['location'] = location
        return item
