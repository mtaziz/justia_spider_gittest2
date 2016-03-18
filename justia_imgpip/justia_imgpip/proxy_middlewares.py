import os
import random
from scrapy import signals, log
from twisted.internet import reactor
from scrapy.crawler import Crawler
from scrapy.settings import Settings
from scrapy.conf import settings 

# from scrapy.crawler import settings
class RandomUserAgentMiddleware(object):
    def process_request(self, request, spider):
        ua  = random.choice(settings.get('USER_AGENT_LIST'))
        if ua:
            request.headers.setdefault('User-Agent', ua)

class ProxyMiddleware(object):
    def process_request(self, request, spider):
        request.meta['proxy'] = settings.get('HTTP_PROXY')