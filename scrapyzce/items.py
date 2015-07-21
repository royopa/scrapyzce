# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyZceItem(scrapy.Item):
    # define the fields for your item here like:
    candidate_name = scrapy.Field()
    cert_name = scrapy.Field()
    candidate_id = scrapy.Field()
    cert_date = scrapy.Field()
    company_name = scrapy.Field()
    city = scrapy.Field()
    state_region = scrapy.Field()
    country = scrapy.Field()
    links = scrapy.Field()
    photo_url = scrapy.Field()
    pass
