# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import JustiaImgPipItem
from scrapy.selector import Selector
import urlparse


class JustiaLawyersImgPipSpider(CrawlSpider):
    name = "justia_lawyers_imgpip"
    allowed_domains = ["justia.com"]
    start_urls = (
        # 'http://www.justia.com/lawyer',
        'https://www.justia.com/lawyers/arkansas',
        # 'https://www.justia.com/lawyers/bankruptcy-and-debt/california/anaheim',
        # 'https://lawyers.justia.com/lawyer/gregory-alumit-1482993',
        # 'https://lawyers.justia.com/lawyer/bahram-madaen-1490971',
        # 'https://www.justia.com/lawyers/workers-compensation/illinois/chicago',
        # 'https://lawyers.justia.com/lawyer/arthur-joseph-travieso-138325',
    )
    # rules = (
    #     Rule(LinkExtractor(allow=('/collection/', ), deny=('/users/', '/collections/'), unique=True), follow=True),
    #     Rule(LinkExtractor(allow=('/p/(.*)+', ), unique=True), callback='parse_item', follow=True),
    # )

    rules = (
        Rule(
            #\/pub\/\w.+
            # LinkExtractor(allow=('(/pub/(\w+\-\w+\-\w+))|(/pub/(\w+\-\w+))')),
            # deny=('/users/', '/collections/'), unique=True
            # LinkExtractor(allow=(r'/lawyer/(\w+)-*(\w+)-*\w+-*(\d+)'),deny=(r'/contact', r'/vcard')), #working Latestv1
            # LinkExtractor(allow=(r'/lawyer/(((\w+)-*(\w+)-*\w+-*-*\w+-*)|((\w+)-*(\w+)-*\w+-*)|((\w+)-*(\w+)))(\d+)'),deny=(r'/contact', r'/vcard')), #working Latestv1
            # LinkExtractor(allow=(r'/lawyer/\w.+-(\d+)'),deny=(r'/contact', r'/vcard'), follow=True), #working Latestv1 
            # lastest2
            LinkExtractor(allow=(r'/lawyer/\w.+$'), deny=(r'/contact', r'/vcard', r'/questions', r'tel'),), #working Latestv1
            # /lawyer/(\w+)*-*(\w+)*-*(\w+)*-*\d+[^/]
            # /pub/\w.+$
            # /lawyer/\w.+-(\d+)
            # (\w+-?)+$
            # LinkExtractor(allow=(r'/lawyer/\w+-*\w+-*\w+-*\w+-*\w+-*\d+'),), #working
            # LinkExtractor(allow=(r'/lawyer/(\w+)*-*(\w+)*-*(\w+)*-*\d+$')), #trying to not include contact
            #/lawyer/(\w+)*-*(\w+)*-*(\w+)*-*\d+
            process_links='process_links',
            callback='parse_links',
            follow=True, 
            # max_pages=5
            ),
        )
    # rules = (
    #     Rule(LinkExtractor(allow=('/collection/', ), deny=('/users/', '/collections/'), unique=True), follow=True),
    #     Rule(LinkExtractor(allow=('/p/(.*)+', ), unique=True), callback='parse_item', follow=True),
    # )

    def parse_links(self, response):
    	#Lawer Name
    	#('h1[@class="fn layer-name"]/text()').extract()
    	item = JustiaImgPipItem()
    	sel = Selector(response)
    	# names_data = sel.xpath('.//h1[@class="fn layer-name"]/text()').extract()
    	urls_data = response.url
    	names_data = sel.xpath('//div[@class="lawyer-coreinfo has-padding-30 has-no-bottom-padding"]/h1/text()').extract()
    	profile_photo_data = sel.xpath('//div[@class="lawyer-avatar"]/img[@class="-avatar"]/@src').extract()
        # download_page_rep = response.xpath('//div[@class="fengmian"]/img/@src').extract()
        # if profile_photo_data:                                                    
        image_url = profile_photo_data
        item['image_urls'] = image_url
            # return item 
        practice_area_data = sel.xpath('//ul[@class="lawyer-key-info list-gutter--tiny has-no-padding has-no-top-margin"]/li/text()').extract()
    	# practice_area_detail_data = sel.xpath('//div[@id="practice-areas-block"]/ul[@class="has-no-list-styles"]/li/text()').extract() #not working
    	practice_area_detail_data = sel.xpath('//div[@id="practice-areas-block"]/div[@class="block-wrapper"]/ul[@class="has-no-list-styles"]/li/text()').extract()
    	badges_data = sel.xpath('.//div[@class="wrapper jcard has-padding-30 blocks"]/div[1]//span//text()').extract() #Badges
    	# fees_data = sel.xpath('//div[@class="wrapper jcard has-padding-30 blocks"]/div[2]//ul/li/text()').extract()
    	fees_data = sel.xpath('//div[@class="wrapper jcard has-padding-30 blocks"]/div[3]//ul//text()').extract()

    	jurisdiction_admitted_to_practice_data = sel.xpath('//div[@class="wrapper jcard has-padding-30 blocks"]/div[4]//dl//text()').extract() # for Jurisdiction
    	languages_data = sel.xpath('//div[@class="wrapper jcard has-padding-30 blocks"]/div[5]//ul//text()').extract()
    	professional_experience_data = sel.xpath('//div[@class="wrapper jcard has-padding-30 blocks"]/div[6]//text()').extract()[1:3]
    	education_data = sel.xpath('//div[@class="wrapper jcard has-padding-30 blocks"]/div[7]//text()').extract()
    	professional_association_data = sel.xpath('//div[@class="wrapper jcard has-padding-30 blocks"]/div[8]//text()').extract()
    	website_blog_data = sel.xpath('//div[@class="wrapper jcard has-padding-30 blocks"]/div[9]//@href').extract()
    	telephone_data = sel.xpath('//div[@class="lawyer-contact-info"]/a/span[@class="txt"]/text()').extract()

    	item['Source_Urls'] = urls_data
    	item['Name'] = names_data
    	# item['image_url'] = profile_photo_data
    	item['Practice_Area'] = practice_area_data
    	item['Badges'] = badges_data
    	item['Practice_Area_Detail'] = practice_area_detail_data
    	item['Fees'] = fees_data
    	item['Jurisdiction_Admitted_To_Practice'] = jurisdiction_admitted_to_practice_data
    	item['Languages'] = languages_data
    	item['Professional_Experience'] = professional_experience_data
    	item['Education'] = education_data
    	item['Professional_Association'] = professional_association_data
    	item['Website_Blog_Url'] = website_blog_data
    	item['Telephone'] = telephone_data
    	# item['Profile_Photo'] = profile_photo_data

    	return item
###{{{
    	#<div class="lawyer-contact-info">
    	#<a target="_blank" href="tel:8008725925" class="cnt-item" data-button-tag="call">
    	#<span class="jicon jicon-phone blue">
    	#</span><span class="txt">(800) 872-5925</span></a><a href="/lawyer/gregory-alumit-1482993/contact" class="cnt-item" data-button-tag="email">
    	#<span class="jicon jicon-email blue"></span><span class="txt">email lawyer</span></a><a target="_blank" href="http://www.howardlawpc.com/lawyer-attorney-1415595.html" class="cnt-item" data-button-tag="website"><span class="jicon jicon-website blue"></span><span class="txt">visit website</span></a></div>
    	#}}}


    	# <div class="lawyer-coreinfo has-padding-30 has-no-bottom-padding">
    # <h1 itemprop="name" class="fn lawyer-name">Arthur Joseph Travieso</h1><strong><em><a class="color-guardsman-red" href="/claim/138325" rel="nofollow">Update your profile now!</a></em></strong></div>
    	# practice_area_data = sel.xpath('//ul[@class="jicon jicon-gavel jicon-inline"]/text()').extract()

    	    	# <span class="jicon jicon-gavel jicon-inline"></span>
    	#<span class="jicon jicon-gavel jicon-inline"></span>Bankruptcy, Employment Law, Foreclosure Defense...
    	#<ul class="lawyer-key-info list-gutter--tiny has-no-padding has-no-top-margin"><li class="iconed-line text-ellipsis"><span class="jicon jicon-gavel jicon-inline"></span>Bankruptcy, Employment Law, Foreclosure Defense...</li><li class="iconed-line"><span class="jicon jicon-jurisdictions jicon-inline"></span>California, Michigan</li></ul>
    	#<ul class="has-no-list-styles"><li>Bankruptcy</li><li>Employment Law</li><li>Foreclosure Defense</li><li>Personal Injury</li><li>Probate</li><li>Social Security Disability/SSI</li><li>Consumer Law</li></ul>
    	# <div id="practice-areas-block" class="block"><div class="heading-3 block-title iconed-heading"><span class="jicon -large jicon-gavel"></span>Practice Areas</div><div class="block-wrapper"><ul class="has-no-list-styles"><li>Bankruptcy</li><li>Employment Law</li><li>Foreclosure Defense</li><li>Personal Injury</li><li>Probate</li><li>Social Security Disability/SSI</li><li>Consumer Law</li></ul></div></div>

    	# <div class="heading-3 block-title iconed-heading"><span class="jicon -large jicon-fee"></span>Fees</div>
    	# //*[@id="profile-page"]/div/div[1]/div/div[3]/div[2]/ul/li
    	# //*[@id="profile-page"]/div/div[1]/div/div[3]/div[2]/ul/li/text()
    	# //*[@id="profile-page"]/div/div[1]/div
    	# <div class="wrapper jcard has-padding-30 blocks"
    	