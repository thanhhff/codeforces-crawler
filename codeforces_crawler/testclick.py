from selenium import webdriver
import scrapy
import time

start = time.time()

driver = webdriver.Chrome("/Users/thanhhff/Google Drive/Thanhhff-Backup/Codeforces-crawler/"
                          "chromedriver")
driver.get('https://codeforces.com/contest/1342/submission/78372282')
# button = driver.find_elements_by_xpath('//href[@class="click-to-view-tests"]')[0]
# button = driver.find_elements_by_xpath('//div[contains(@href, "click-to-view-tests")]')[0]

driver.find_element_by_link_text("Click").click()

# caption = driver.find_elements_by_xpath('//span[@class="test"]')[0].text
# infoline = driver.find_elements_by_xpath('//div[contains(@class, "infoline tm_infoline")]/div[@class=name]')[0].text
# file_input = driver.find_elements_by_xpath('//div[contains(@class, "file input-view")]')[0].text
# file_output = driver.find_elements_by_xpath('//div[contains(@class, "file output-view")]')[0].text
# file_answer = driver.find_elements_by_xpath('//div[contains(@class, "file answer-view")]')[0].text
# file_checker = driver.find_elements_by_xpath('//div[contains(@class, "caption titled")]')[0].text
# file_checker_comment = driver.find_elements_by_xpath('//div[contains(@class, "file checker-comment-view")]')[0].text

# print(infoline, file_input, file_output, file_answer, file_checker_comment)

# print(file_answer)
end = time.time()

print(end - start)
driver.close()
