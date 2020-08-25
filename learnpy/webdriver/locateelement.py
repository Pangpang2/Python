#coding= utf-8
from selenium import webdriver

driver = webdriver.Firefox()
driver.get('http://news.baidu.com')

#by link text
driver.find_element_by_link_text("国内")
#by partial link text
driver.find_element_by_partial_link_text("国")
#by xpath
#driver.find_element_by_xpath('/html/div[2]/input')
#driver.find_element_by_xpath('//input[@id= "input"]')
#by css
driver.find_element_by_css_selector("ul>li")
