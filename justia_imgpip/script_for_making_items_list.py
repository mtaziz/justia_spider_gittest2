import re
import os
import sys 

with open('items_list.txt', 'r') as fread:
    #find scrapy.Field()
    #and remove from it 
    readfile = fread.read()
    print readfile 


# # Source_Urls = scrapy.Field()
#     Name = scrapy.Field()
#     image_urls =  scrapy.Field()
#     Practice_Area = scrapy.Field()
#     Badges = scrapy.Field()
#     Practice_Area_Detail = scrapy.Field()
#     Fees = scrapy.Field()
#     Jurisdiction_Admitted_To_Practice = scrapy.Field()
#     Languages = scrapy.Field()
#     Professional_Experience = scrapy.Field()
#     Education = scrapy.Field()
#     Professional_Association = scrapy.Field()
#     Website_Blog_Url = scrapy.Field()
#     Telephone = scrapy.Field()
#     image_paths = scrapy.Field()  