from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

try:
    #link = "http://suninjuly.github.io/selects1.html"
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get(link)

    num1 = browser.find_element_by_id('num1').text
    num2 = browser.find_element_by_id('num2').text
    y = int(num1) + int(num2)

    select = Select(browser.find_element_by_id('dropdown'))
    select.select_by_value(str(y))

    submit_btn = browser.find_element_by_class_name('btn-default')
    submit_btn.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
