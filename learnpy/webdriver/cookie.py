#coding = utf-8
from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get('http://www.youdao.com')

cookie = driver.get_cookies()
print(cookie)

driver.add_cookie({'name':'key-aaaa','value':'value-bbb'})

print(driver.get_cookie('key-aaaa'))

for cookie in driver.get_cookies():
	print('%s->%s'%(cookie['name'],cookie['value']))

driver.delete_cookie('key-aaa')
driver.delete_all_cookies()

driver.get('http://mail.163.com')
driver.implicitly_wait(5)
driver.switch_to_frame('x-URS-iframe')
time.sleep(4)
mail = driver.find_element_by_css_selector('#account-box input')
pwd = driver.find_element_by_css_selector('#login-form input[name=password]')
login = driver.find_element_by_css_selector('#dologin')
mail.send_keys('yueting2li')
pwd.send_keys('liapaopao@')
login.click()
print('---------------------------------')
print(driver.get_cookies())

