# -*- coding: utf-8 -*-
import scrapy
import numpy as np


class GetlinkContestSpider(scrapy.Spider):
    name = 'getlink_contest'
    allowed_domains = ['https://codeforces.com']
    start_urls = ['https://codeforces.com/contests']

    def parse(self, response):
        print("Processing: ", response.url)

        # for i in range(101):

        # Không lấy những contest đang thi
        black_list = ['1348', '1344', '1345', '1349', '1350', '1347', '1346']
        contest_list = response.xpath('//tr/@data-contestid').extract()

        contest_ids = np.setdiff1d(contest_list, black_list)
        # print(contest_ids)

        for contest_id in contest_ids:
            pass

        pass
