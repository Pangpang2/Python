#coding= utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Firefox()
driver.get('https://www.baidu.com/')
driver.set_window_size(600,800)

searchbox = driver.find_element_by_css_selector('#kw')
searchbox.send_keys("selenium")
searchbox.clear()
searchbox.send_keys("webdriver")

searchbtn = driver.find_element_by_css_selector(".bg.s_btn")
searchbtn.submit()

print("百度搜索框宽高：%s"%searchbox.size)
print("百度搜索框内容：%s"%searchbox.get_attribute('value'))
print("百度搜索框属性type：%s"%searchbox.get_attribute('type'))
print("百度搜索框属性is displayed：%s"%searchbox.is_displayed())



