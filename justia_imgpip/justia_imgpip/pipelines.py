# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy import Request
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem
# from pymongo import MongoClient
# from scrapy.exceptions import DropItem

## Duplicate Items 
# class JustiaImgPipDuplicatesPipeline(object):
#     def __init__(self):
#         self.ids_seen = set()

#     def process_item(self, item, spider):
#         if item['id'] in self.ids_seen:
#             raise DropItem("Duplicate item found: %s" % item)
#         else:
#             self.ids_seen.add(item['id'])
#             return item

class JustiaImgPipPipeline(object):
    def process_item(self, item, spider):
        return item

# #{{{ Justia Images Pipeline when multiple images required to be downloaded	
# class JustiaImgPipProfilePhotoPipeline(ImagesPipeline):
# 	# if item['Image_urls'] and item[]
# 	def get_media_requests(self, item, info):
# 		for image_url in item['image_urls']:
# 			yield scrapy.Request(image_url) 
	
# 	def item_completed(self, results, item, info):
# 		image_paths = [x['path'] for ok, x in results if ok]
# 		if not image_paths:
# 			raise DropItem('JustiaProfilePhotoItem does not contain images.')
# 		item['image_paths'] = image_paths
# 		return item
##}}}


# from scrapy.contrib.pipeline.images import ImagesPipeline
# from scrapy import Request
###{{{ For Single Image 
class JustiaImgPipProfilePhotoPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        yield Request(image_urls)

    def item_completed(self, results, item, info):
        images = [x for ok, x in results if ok]
        if images:
            image = images[0]
            path = image['path'].split('/')[-1]
            item['image_urls'] = path
        return item
