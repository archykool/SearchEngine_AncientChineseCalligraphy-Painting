# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TpmItem(scrapy.Item):
    title = scrapy.Field ()
    dynasty = scrapy.Field()
    classify = scrapy.Field()
    author = scrapy.Field()
    image = scrapy.Field()
    title2 = scrapy.Field()
    content = scrapy.Field()
    collection_detail_url = scrapy.Field()
