import scrapy
from codeforces_crawler.items import CodeforcesCrawlerItem
import time


class SubmissionsSpider(scrapy.Spider):
    name = "cf_submission"
    allowed_domains = ['codeforces.com']
    start_urls = ['https://codeforces.com/problemset/status/1082/problem/F']

    # Lựa chọn ngôn ngữ chương trình muốn get về
    wanted_languages = ['Java 8', 'Python 3', 'GNU C++11', 'Java 7', 'Java 6', 'Python 2']

    # Kiểm tra verdict mong muốn
    wanted_verdicts = ['RUNTIME_ERROR', 'OK']

    def parse(self, response):
        print("Processing: ", response.url)

        id = 0

        submission_id_list = response.xpath('//tr/@data-submission-id').extract()

        for submission_id in submission_id_list:
            if (id == 1):
                break

            submission_lang = response.xpath('//tr[@data-submission-id=%s]/td[5]/text()' % submission_id)[
                0].extract().strip()

            # Kiểm tra xem có nằm trong các ngôn ngữ mình mong muốn
            if submission_lang not in self.wanted_languages:
                continue

            submission_verdict = response.xpath(
                '//tr[@data-submission-id=%s]/td[6]/span/@submissionverdict' % submission_id)[0].extract().strip()
            if submission_verdict not in self.wanted_verdicts:
                continue

            code_link = 'https://codeforces.com' + (response.xpath(
                '//tr[@data-submission-id=%s]/td[1]/a[contains(@href, "submission")]/@href' % submission_id)[
                                                        0].extract().strip())

            time.sleep(0.1)
            item = CodeforcesCrawlerItem()
            item['submission_id'] = submission_id
            item['submission_lang'] = submission_lang
            item['submission_verdict'] = submission_verdict

            id += 1

            yield scrapy.Request(url=code_link, meta={'item': item},
                                 callback=self.parse_code)

    # Next page code
    # Todo

    def parse_code(self, response):
        source_code = response.xpath('//pre[@id="program-source-text"]/text()').extract()
        # print(source_code)
        item = response.meta['item']
        item['source_code'] = source_code

        # Xử lý output
        # Todo
        from selenium import webdriver
        driver = webdriver.Chrome("/Users/thanhhff/Google Drive/Thanhhff-Backup/Codeforces-crawler/"
                                  "chromedriver")
        driver.get(response.url)
        full_web = driver.find_element_by_link_text("Click").click()
        driver.close()

        yield item
