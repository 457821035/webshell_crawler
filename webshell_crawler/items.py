# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WebshellCrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    request_url = scrapy.Field()
    response_header = scrapy.Field()
    response_body = scrapy.Field()
    response_status = scrapy.Field()
    post = scrapy.Field()