# new link with bug
from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    #прошу заметить, запрос input1 является уникальным, первое поля в обоих ссылках заполнится корректно
    #считаю правильным, что тест по 2-ой ссылке должен упасть по ошибке: NoSuchElementException - placeholder="Input your last name
    input1 = browser.find_element_by_xpath("//div[@class='form-group first_class']//input[contains(@placeholder,'name')]")
    input1.send_keys("Алексей")
    input2 = browser.find_element_by_css_selector('[placeholder="Input your last name"]')
    input2.send_keys("Навальный")
    input3 = browser.find_element_by_css_selector('[placeholder="Input your email"]')
    input3.send_keys("fbk@fbk.info")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    time.sleep(2)

    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()