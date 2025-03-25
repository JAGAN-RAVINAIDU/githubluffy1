# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
# extracted data -> temporary containers(items) -> storing into database

import scrapy


class QuotetutorialItem(scrapy.Item):
    # define the fields for your item like:
    title = scrapy.Field()
    author = scrapy.Field()
    tag = scrapy.Field()

