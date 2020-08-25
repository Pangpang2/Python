from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support.select import Select




def login(driver):
    login_url = 'https://testrail.internetbrands.com/testrail/index.php?/auth/login'
    driver.get(login_url)
    username_input = driver.find_element_by_css_selector('#name')
    username_input.send_keys('may.li@internetbrands.com')

    password_input = driver.find_element_by_css_selector('#password')
    password_input.send_keys('Liapaopao2')

    login_btn = driver.find_element_by_css_selector('.button-ok')
    login_btn.click()

def update_auto_info(driver, url, automation_name, suite_name):
    driver.get(url)

    # edit_btn = driver.find_element_by_css_selector('.button-edit')
    # edit_btn.click()

    try:
        type_element = driver.find_element_by_css_selector('#type_id')
        type_selector = Select(type_element)
        type_selector.select_by_visible_text('Automated')

        automation_name_input = driver.find_element_by_css_selector('#custom_automation_test_name')
        automation_name_input.clear()
        automation_name_input.send_keys(automation_name)

        suite_name_input = driver.find_element_by_css_selector('#custom_automation_suite_name')
        suite_name_input.clear()
        suite_name_input.send_keys(suite_name)

        save_btn = driver.find_element_by_css_selector('#accept')
        save_btn.click()
    except Exception as e:
        print e.message

if __name__ == '__main__':

    driver = WebDriver()
    login(driver)
    with open('./auto_info.txt', 'r') as f:
        for line in f.readlines():
            list_info = line.split(' ')
            url = 'https://testrail.internetbrands.com/testrail/index.php?/cases/edit/{id}/1'\
                .format(id=list_info[0].strip(' ').replace('\n', '').replace('\r', ''))
            print url
            print list_info[1] + '  ' + list_info[2] + '  '
            update_auto_info(driver, url, list_info[2], list_info[1])

        driver.close()

