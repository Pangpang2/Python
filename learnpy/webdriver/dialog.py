#coding = utf-8
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Firefox()

driver.get('https://www.baidu.com')

driver.find_element_by_link_text('登录').click()

WebDriverWait(driver, 10).until(lambda driver:driver.find_element_by_css_selector('[name=userName]'),'timeout')

