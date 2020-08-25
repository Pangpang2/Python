#coding = utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()
driver.get('http://www.baidu.com')

searchbox = driver.find_element_by_css_selector('#kw')
searchbox.send_keys("selenium")
time.sleep(3)

searchbox.send_keys(Keys.BACK_SPACE)
time.sleep(3)

searchbox.send_keys(Keys.SPACE)
searchbox.send_keys(u"教程")
time.sleep(3)

searchbox.send_keys(Keys.CONTROL, 'a')
time.sleep(3)

searchbox.send_keys(Keys.CONTROL, 'x')
time.sleep(3)


searchbox.send_keys(Keys.CONTROL, 'v')
time.sleep(3)

searchbox.send_keys(Keys.ENTER)
time.sleep(3)