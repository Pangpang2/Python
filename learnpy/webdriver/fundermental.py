#coding=utf-8
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

#binary = FirefoxBinary(r'C:\Program Files (x86)\Mozilla Firefox\firefox.exe')
#driver = webdriver.Firefox(firefox_binary = binary)
driver = webdriver.Firefox()
first_url = 'http://www.baidu.com'
print('now access %s' %(first_url))
driver.get(first_url)

second_url ='http://news.baidu.com'
print('now access %s' %(second_url))
driver.get(second_url)

print("back to %s" % (first_url))
driver.back()

print("forward to %s" % (second_url))
#driver.forward()

print("maximize browser")
driver.maximize_window()
print("set windows width:480 height:800")
driver.set_window_size(480, 800)

print('title: %s'%driver.title)
print('url: %s'%driver.current_url)

#driver.execute_script('$("#kw").val("nihao");$("#su").click()')
searchbox = driver.find_element_by_css_selector('#kw')
searchbtn = driver.find_element_by_css_selector('#su')
driver.execute_script('$(arguments[0]).val("hi");$(arguments[1]).click()',searchbox,searchbtn)
#driver.quit()