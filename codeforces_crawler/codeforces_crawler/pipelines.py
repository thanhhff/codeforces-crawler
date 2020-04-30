# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class CodeforcesCrawlerPipeline:
    def process_item(self, item, spider):
        return item

    # def process_item(self, item, spider):
    #     self.items_nums += 1
    #     self.collection.insert(dict(item))
    #     if self.items_nums % 100 == 0:
    #         print("%d items have been collected." % self.items_nums)
    #     return item
    #
    # # spider_closed() function is deprecated.
    # def close_spider(self, spider):
    #     self.client.close()
