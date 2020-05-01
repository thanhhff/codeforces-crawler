# -*- coding: utf-8 -*-
import scrapy
import numpy as np
import time
from codeforces_crawler.items import GetlinkContestSpiderItem

item = GetlinkContestSpiderItem()


class GetlinkContestSpider(scrapy.Spider):
    name = 'getlink_contest'
    allowed_domains = ['https://codeforces.com']
    start_urls = ['https://codeforces.com/contests']

    def parse(self, response):
        print("Processing: ", response.url)
        # Không lấy những contest đang thi
        black_list = ['1348', '1344', '1345', '1349', '1350', '1347', '1346']
        contest_list = response.xpath('//tr/@data-contestid').extract()

        contest_ids = np.setdiff1d(contest_list, black_list)
        # print(contest_ids)

        for contest_id in contest_ids:
            contest_name = response.xpath('//tr[@data-contestid=%s]/td[1]/text()' % contest_id)[0].extract().strip()

            if ('Div. 2' in contest_name or 'Div. 3' in contest_name):
                # print(contest_name)
                contest_link = 'https://codeforces.com/contest/' + str(contest_id) + '/status'

                item['contest_id'] = contest_id
                item['contest_name'] = contest_name
                item['contest_link'] = contest_link
                yield item
            else:
                continue

        time.sleep(3)

        # generate next-page url
        if response.selector.xpath('//span[@class="inactive"]/text()').extract():
            # '\u2192' is the unicode of 'right arrow' symbol
            if response.selector.xpath('//span[@class="inactive"]/text()')[0].extract() != u'\u2192':
                next_page_href = response.selector.xpath('//div[@class="pagination"]/ul/li/a[@class="arrow"]/@href')[0]
                next_page_url = response.urljoin(next_page_href.extract())
                yield scrapy.Request(next_page_url, meta={'item': item}, callback=self.parse, dont_filter=True)
        else:
            next_page_href = response.selector.xpath('//div[@class="pagination"]/ul/li/a[@class="arrow"]/@href')[1]
            next_page_url = response.urljoin(next_page_href.extract())
            yield scrapy.Request(next_page_url, meta={'item': item}, callback=self.parse, dont_filter=True)
