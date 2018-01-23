from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
class selenium:

        driver = webdriver.Firefox()
        driver.implicitly_wait(10)
        driver.get("http://www.eBay.com")
        driver.find_element_by_id("gh-ac").send_keys("htc10")
        driver.find_element_by_id("gh-ac").send_keys(Keys.ENTER)
        #seting the currncy to USD
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.ID, "e1-2")))
        driver.find_element_by_id("e1-2").click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "custLink")))
        driver.find_element_by_id("custLink").click()
        driver.find_element_by_id("e1-15").click()
        driver.find_element_by_id("e1-3").click()
        #selecting the first htc10 mobile
        driver.find_element_by_css_selector("#item2f1242c1dc>.lvtitle>.vip").click()
        #select color
        color=Select(driver.find_element_by_css_selector(".msku-sel")).select_by_index(1)
        #add to cart
        driver.find_element_by_id("isCartBtn_btn").click()
        #the total value in teh cart
        total=driver.find_element_by_id("syncTotal").text

        if total<=500:
            driver.find_element_by_id("ptcBtnRight").click()
            driver.find_element_by_id("ptcBtnRight").click()
            driver.find_element_by_id("gtChk").click()
            driver.find_element_by_id("af-first-name").send_keys("test")
            driver.find_element_by_id("af-last-name").send_keys("test123")
            driver.find_element_by_id("af-address1").send_keys("sapce")
            driver.find_element_by_id("af-city").send_keys("colo")
            driver.find_element_by_id("af-state").send_keys("walla")
            driver.find_element_by_id("af-zip").send_keys("12345")
            driver.find_element_by_id("af-email").send_keys("12345@fdsgdsg.com")
            driver.find_element_by_id("af-email-confirm").send_keys("12345@fdsgdsg.com")
            driver.find_element_by_css_selector(".input-field.ipt-phone").send_keys("123456")

        else:
            print("Add more product")


