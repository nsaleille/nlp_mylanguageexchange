# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DmozItem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
    desc = scrapy.Field()

class mylanguageexchangeItem(scrapy.Item):
	name = scrapy.Field()
	country = scrapy.Field()
	city = scrapy.Field()
	native = scrapy.Field()
	practicing = scrapy.Field()
	desc = scrapy.Field()