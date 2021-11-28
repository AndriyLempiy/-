from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


def scroll(element):
    browser.execute_script("return arguments[0].scrollIntoView(true);", element)

try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get(link)

    x = browser.find_element_by_id('input_value').text
    y = calc(x)

    answer = browser.find_element_by_id('answer')
    scroll(answer)
    answer.send_keys(y)

    check_box = browser.find_element_by_id('robotCheckbox')
    scroll(check_box)
    check_box.click()
    radio_btn = browser.find_element_by_id('robotsRule')
    scroll(radio_btn)
    radio_btn.click()
    submit_btn = browser.find_element_by_class_name('btn')
    scroll(submit_btn)
    submit_btn.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
