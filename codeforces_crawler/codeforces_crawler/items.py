# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CodeforcesCrawlerItem(scrapy.Item):
    # submissionID
    submission_id = scrapy.Field()
    submission_code = scrapy.Field()
    submission_user = scrapy.Field()
    submission_problem = scrapy.Field()
    submission_lang = scrapy.Field()
    submission_verdict = scrapy.Field()
    contest_id = scrapy.Field()
    # output = scrapy.Field()


class GetlinkContestSpiderItem(scrapy.Item):
    contest_id = scrapy.Field()
    contest_name = scrapy.Field()
    contest_link = scrapy.Field()
