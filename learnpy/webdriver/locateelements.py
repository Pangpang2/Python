#coding = utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Firefox()

driver.get('https://www.sojump.com/jq/8504418.aspx')

#inputs = driver.find_elements_by_tag_name('input')
inputs = driver.find_elements_by_css_selector('#divquestion3 .jqCheckbox')

for input in inputs:
	input.click()

print(len(inputs))

inputs.pop().click()

print(len(driver.find_elements_by_css_selector('#divquestion3 .jqCheckbox.jqChecked')))


