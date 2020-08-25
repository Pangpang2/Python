#coding = utf-8
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time

driver = webdriver.Firefox()
driver.get('http://www.baidu.com')

searchbox = WebDriverWait(driver,10).until(lambda driver: driver.find_element_by_css_selector('#kw'),'haha')
searchbox.send_keys("selenium")

driver.implicitly_wait(30)
driver.find_element_by_css_selector('#su').click()

time.sleep(5)

