#coding = utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Firefox()
driver.get('https://msdn.microsoft.com/en-us/library/bing-ads-api(v=msads.100).aspx')

#passowrd = driver.find_element_by_css_selector('#passowrd')
#nick = driver.find_element_by_css_selector('#nick')

action = ActionChains(driver)
#action.context_click(nick) # 右击
#action.drag_and_drop(mail,nick)
#action.move_to_element(passowrd)
#action.double_click(nick)
#action.click_and_hold(nick)


driver.find_element_by_link_text('Programs').click()
time.sleep(2)
menu = driver.find_element_by_link_text('Subscriptions')

action.move_to_element(menu).perform()