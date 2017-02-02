# -*- coding: UTF-8 -*-

import random

from RealtyAnalysis import settings

class RandomProxy(object):

    def __init__(self):
        pass

    def process_request(self, request, spider):
        request.meta['proxy'] = settings.HTTP_PROXY
