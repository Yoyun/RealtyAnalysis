# -*- coding: UTF-8 -*-

import scrapy

from RealtyAnalysis.items import XiaozhuItem

class XiaozhuSpider(scrapy.Spider):
    name = "xiaozhu"
    allowed_domains = ["xiaozhu.com"]
    start_urls = [
        'http://sz.xiaozhu.com'
    ]

    def parse(self, response):
        haveNext = response.xpath('//*[@id="page_list"]/div[@class="pagination_v2 pb0_vou"]/a/text()').extract()[-1]
        if (haveNext == '>'):
            url = response.xpath('//*[@id="page_list"]/div[@class="pagination_v2 pb0_vou"]/a/@href').extract()[-1]
            print url
            yield scrapy.Request(url, callback=self.parse)

        selList = response.xpath('//*[@id="page_list"]/ul/li')
        for sel in selList:
            item = XiaozhuItem()
            item['latlng'] = sel.xpath('@latlng').extract()[0]
            item['title'] = sel.xpath('div[2]/div/a/span/text()').extract()[0]
            item['price'] = float(sel.xpath('div[2]/span[1]/i/text()').extract()[0])

            temp = sel.xpath('div[2]/div/em/text()').extract()[0].strip().split('/')
            item['single'] = temp[0]
            item['bed'] = temp[1]
            item['people'] = int(temp[2][2])

            temp = sel.xpath('div[2]/div/em/span/text()').extract()[0].replace('-', '').strip().split('/')
            item['score'] = float(temp[0][:-1] if len(temp) > 1 else -1)
            item['comment'] = int(temp[1 if len(temp) > 1 else 0][:-3])
            yield item
