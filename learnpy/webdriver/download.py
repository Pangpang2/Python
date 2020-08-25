#coding = utf-8
from selenium import webdriver
import os

fp = webdriver.FirefoxProfile()

fp.set_preference("browser.download.folderList",2)
fp.set_preference("browser.download.manager.showWhenStarting",False)


driver = webdriver.Firefox(fp)
driver.get('http://pypi.python.org/pypi/selenium')
driver.find_element_by_partial_link_text('selenium-3').click()