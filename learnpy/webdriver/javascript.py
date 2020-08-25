#coding = utf-8
from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get('http://www.baidu.com')

#driver.execute_script('$("#kw").val("nihao");$("#su").click()')
searchbox = driver.find_element_by_css_selector('#kw')
searchbtn = driver.find_element_by_css_selector('#su')
driver.execute_script('$(arguments[0]).val("selenium");$(arguments[1]).click()',searchbox,searchbtn)
time.sleep(3)

js_ = "var q = document.documentElement.scrollTop=1000"
driver.execute_script(js_)

time.sleep(3)

#driver.quit()