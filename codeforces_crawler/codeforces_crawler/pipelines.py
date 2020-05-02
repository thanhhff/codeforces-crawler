# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import csv


class CodeforcesCrawlerPipeline:

    # def open_spider(self, spider):
    #     with open('contest-info.csv', 'r') as f:
    #         contest_info = []
    #         header = f.readline()
    #         for line in f.readlines():
    #             array = line.split(',')
    #             contest_id_url = [array[0], array[1]]
    #             contest_info.append(contest_id_url)
    #
    #     for info in contest_info[100:101]:
    #         contest_id = info[0]
    #         filename = 'contest/' + str(contest_id) + '.csv'
    #         with open('crawl-data/' + filename, 'w') as f:
    #             writer = csv.writer(f)
    #             writer.writerow(['submit_id', 'user_name', 'code', 'problem', 'lang', 'verdict', 'contest_id'])

    def __init__(self):
        self.items_nums = 0

    def process_item(self, item, spider):
        self.items_nums += 1

        filename = item['contest_id'] + '.csv'
        with open('crawl-data/contest/' + filename, 'a') as f:
            writer = csv.writer(f)
            writer.writerow(item.values())

        if self.items_nums % 100 == 0:
            print("%d items have been collected." % self.items_nums)

        return item
