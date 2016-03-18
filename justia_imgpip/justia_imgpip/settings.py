# -*- coding: utf-8 -*-

# Scrapy settings for justia project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
import os
# from middlewares.proxy_middlewares import RandomUserAgentMiddleware
# from middlewares.proxy_middlewares import ProxyMiddleware
# from middlewares import csv_exporters

BOT_NAME = 'justia_imgpip'
SPIDER_MODULES = ['justia_imgpip.spiders']
NEWSPIDER_MODULE = 'justia_imgpip.spiders'
DOWNLOAD_DELAY=5

USER_AGENT_LIST = [
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7',
    'Mozilla/5.0 (Windows NT 6.2; Win64; x64; rv:16.0) Gecko/16.0 Firefox/16.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/534.55.3 (KHTML, like Gecko) Version/5.1.3 Safari/534.53.10'
]
HTTP_PROXY = 'https://127.0.0.1:8123'
DOWNLOADER_MIDDLEWARES = {
     'justia_imgpip.proxy_middlewares.RandomUserAgentMiddleware': 400,
     'justia_imgpip.proxy_middlewares.ProxyMiddleware': 410,
     'scrapy.downloadermiddleware.useragent.UserAgentMiddleware': None
    # Disable compression middleware, so the actual HTML pages are cached
}

# Custom exporter to enforce field order
FEED_EXPORTERS = {
    'csv': 'justia_imgpip.csv_exporters.JustiaImgPipItemExporter'
}

# ITEM_PIPELINES = { 'scrapy.pipelines.images.ImagesPipeline': 600
	
# }

###{{{ item pipelines for duplication checking and image downloading in particular profie photo for justia lawyers
# ITEM_PIPELINES = {
# 	# 'justia_imgpip.pipelines.JustiaImgPipDuplicatesPipeline':600,
# 	'justia_imgpip.pipelines.JustiaImgPipProfilePhotoPipeline':650,
# 	}
###}}}
IMAGES_STORE = os.path.join(os.getcwd(), 'justia_profile_photo_new')
IMAGES_EXPIRES = 90
COOKIES_ENABLED=False

FIELDS_TO_EXPORT = [
	'Source_Urls', 
	'Name', 
	'image_urls', 
	'Practice_Area', 
	'Badges', 
	'Practice_Area_Detail', 
	'Fees', 
	'Jurisdiction_Admitted_To_Practice', 
	'Languages', 
	'Professional_Experience', 
	'Education', 
	'Professional_Association', 
	'Website_Blog_Url', 
	'Telephone', 
	'image_paths'
	]

# LOG_LEVEL = 'INFO'	
RETRY_TIMES = 4
RETRY_HTTP_CODES = [500, 503, 504, 400, 403, 408]
COOKIES_ENABLED = False
HTTPCACHE_ENABLED = True
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.LeveldbCacheStorage'
DNSCACHE_ENABLED = True
# PROXY_LIST = 'eracareers/middlewares/proxies.txt'