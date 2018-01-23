from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("http://www.eBay.com")
driver.find_element_by_id("gh-ac").send_keys("htc10")
driver.find_element_by_id("gh-ac").send_keys(Keys.ENTER)
