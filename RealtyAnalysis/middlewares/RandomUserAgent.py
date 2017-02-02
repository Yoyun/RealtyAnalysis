# -*- coding: UTF-8 -*-

import random

'''
随机生成UserAgent
'''

class RandomUserAgent(object):

    def __init__(self, agents):
        self.agents = agents

    @classmethod
    def from_crawler(cls, crawler):
        # 返回本类实例
        print '======USER_AGENT======'
        return cls(crawler.settings.getlist('USER_AGENT'))

    def process_request(self, request, spider):
        request.headers.setdefault('User-Agent', random.choice(self.agents))
