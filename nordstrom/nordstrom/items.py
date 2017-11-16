# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NordstromItem(scrapy.Item):
    Name = scrapy.Field()
    Address = scrapy.Field()
    City = scrapy.Field()
    State = scrapy.Field()
    Zip = scrapy.Field()
    Telephone = scrapy.Field()
    URL = scrapy.Field()
    Manager = scrapy.Field()
    Image_URL = scrapy.Field()
    Monday_Open = scrapy.Field()
    Monday_Close = scrapy.Field()
    Tuesday_Open = scrapy.Field()
    Tuesday_Close = scrapy.Field()
    Wednesday_Open = scrapy.Field()
    Wednesday_Close = scrapy.Field()
    Thursday_Open = scrapy.Field()
    Thursday_Close = scrapy.Field()
    Friday_Open = scrapy.Field()
    Friday_Close = scrapy.Field()
    Saturday_Open = scrapy.Field()
    Saturday_Close = scrapy.Field()
    Sunday_Open = scrapy.Field()
    Sunday_Close = scrapy.Field()
