# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JustiaImgPipItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    Source_Urls = scrapy.Field()
    Name = scrapy.Field()
    image_urls =  scrapy.Field()
    Practice_Area = scrapy.Field()
    Badges = scrapy.Field()
    Practice_Area_Detail = scrapy.Field()
    Fees = scrapy.Field()
    Jurisdiction_Admitted_To_Practice = scrapy.Field()
    Languages = scrapy.Field()
    Professional_Experience = scrapy.Field()
    Education = scrapy.Field()
    Professional_Association = scrapy.Field()
    Website_Blog_Url = scrapy.Field()
    Telephone = scrapy.Field()
    image_paths = scrapy.Field()  
    pass

		# item['Source_Urls'] = urls_data
  #   	item['Name'] = names_data
  #   	item['Profile_Photo'] = profile_photo_data
  #   	item['Practice_Area'] = practice_area_data
  #   	item['Badges'] = badges_data
  #   	item['Practice_Area_Detail'] = practice_area_detail_data
  #   	item['Fees'] = fees_data
  #   	item['Jurisdiction_Admitted_To_Practice'] = jurisdiction_admitted_to_practice_data
  #   	item['Languages'] = languages_data
  #   	item['Professional_Experience'] = professional_experience_data
  #   	item['Education'] = education_data
  #   	item['Professional_Association'] = professional_association_data
  #   	item['Website_Blog_Url'] = website_blog_data
  #   	item['Telephone'] = telephone_data
  #   	