import scrapy
from codeforces_crawler.items import CodeforcesCrawlerItem
import time

item = CodeforcesCrawlerItem()


class SubmissionsSpider(scrapy.Spider):
    name = "cf_submission"
    allowed_domains = ['codeforces.com']
    start_urls = ['https://codeforces.com/contest/9/status']

    # Lựa chọn ngôn ngữ chương trình muốn get về
    wanted_languages = ['GNU C11']

    # Kiểm tra verdict mong muốn
    wanted_verdicts = ['RUNTIME_ERROR', 'OK']

    def parse(self, response):
        print("Processing: ", response.url)

        submission_id_list = response.xpath('//tr/@data-submission-id').extract()

        for submission_id in submission_id_list:

            submission_id_save = response.xpath('//tr[@data-submission-id=%s]/td[1]/a/text()' % submission_id)[
                0].extract().strip()

            submission_user = response.xpath('//tr[@data-submission-id=%s]/td[3]/a/text()' % submission_id)[
                0].extract().strip()

            submission_problem = response.xpath('//tr[@data-submission-id=%s]/td[4]/a/text()' % submission_id)[
                0].extract().strip()

            if 'A' not in submission_problem[0] and 'B' not in submission_problem[0]:
                continue

            submission_lang = response.xpath('//tr[@data-submission-id=%s]/td[5]/text()' % submission_id)[
                0].extract().strip()

            # Kiểm tra xem có nằm trong các ngôn ngữ mình mong muốn
            if submission_lang not in self.wanted_languages:
                continue

            submission_verdict = response.xpath(
                '//tr[@data-submission-id=%s]/td[6]/span/@submissionverdict' % submission_id)[0].extract().strip()
            # if submission_verdict not in self.wanted_verdicts:
            #     continue

            code_link = 'https://codeforces.com' + (response.xpath(
                '//tr[@data-submission-id=%s]/td[1]/a[contains(@href, "submission")]/@href' % submission_id)[
                                                        0].extract().strip())

            # time.sleep(1.5)
            item['submission_id'] = submission_id_save
            item['submission_user'] = submission_user
            item['submission_lang'] = submission_lang
            item['submission_verdict'] = submission_verdict
            item['submission_problem'] = submission_problem

            yield scrapy.Request(url=code_link, meta={'item': item},
                                 callback=self.parse_code)

        # time.sleep(1.5)
        # TODO: generate next-page url
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

    def parse_code(self, response):
        submission_code = response.xpath('//pre[@id="program-source-text"]/text()').extract()
        # print(source_code)
        item = response.meta['item']
        item['submission_code'] = submission_code

        yield item
