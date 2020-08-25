#coding = utf-8
from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get('http://www.baidu.com')

driver.find_element_by_css_selector('#u1 .pf').click()
driver.find_element_by_css_selector('.setpref').click()

driver.find_element_by_css_selector("div #gxszButton .prefpanelgo").click()

time.sleep(5)
alert = driver.switch_to_alert()
print(alert.text)
time.sleep(5)

#alert.dismiss()
#alert.send_keys('xxx')
alert.accept()