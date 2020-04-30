# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CodeforcesCrawlerItem(scrapy.Item):
    # submissionID
    submission_id = scrapy.Field()
    submission_lang = scrapy.Field()
    submission_verdict = scrapy.Field()
    source_code = scrapy.Field()
    output = scrapy.Field();
    pass
