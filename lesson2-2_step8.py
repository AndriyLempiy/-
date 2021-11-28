from selenium import webdriver
import time
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    inputs = browser.find_elements_by_css_selector('.form-group  input')
    for i in inputs:
        i.send_keys("Ivan")

    with open('test1.txt', 'w') as file:
        file.write('test1 for mls 228')
    path = os.getcwd() + '/' + file.name

    input_file = browser.find_element_by_id('file')
    input_file.send_keys(path)

    submit_btn = browser.find_element_by_class_name('btn')
    submit_btn.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
