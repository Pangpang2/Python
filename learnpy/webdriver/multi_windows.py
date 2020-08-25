#coding = utf -8
from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get('https://tieba.baidu.com/index.html')

#get current window
nowhandle = driver.current_window_handle

driver.find_element_by_css_selector('.u_reg a').click()
allhandles = driver.window_handles

for handle in allhandles:
	if handle != nowhandle:
		driver.switch_to_window(handle)
		print('now register window!')
		time.sleep(5)
		driver.find_element_by_partial_link_text('百度用户协议').click()
		time.sleep(5)
		driver.close()

driver.switch_to_window(nowhandle)

driver.find_element_by_id('kw').send_keys(u'注册成功')
