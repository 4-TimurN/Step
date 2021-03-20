# from selenium import webdriver
# import time
# import math

# link = "http://suninjuly.github.io/simple_form_find_task.html"
#
# try:
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     input1 = browser.find_element_by_tag_name("input")
#     input1.send_keys("Ivan")
#     input2 = browser.find_element_by_name("last_name")
#     input2.send_keys("Petrov")
#     input3 = browser.find_element_by_class_name("city")
#     input3.send_keys("Smolensk")
#     input4 = browser.find_element_by_id("country")
#     input4.send_keys("Russia")
#     button = browser.find_element_by_css_selector("button.btn")
#     button.click()
#
# finally:
#     # успеваем скопировать код за 30 секунд
#     time.sleep(30)
#     # закрываем браузер после всех манипуляций
#     browser.quit()
#
# # не забываем оставить пустую строку в конце файла

# link = "http://suninjuly.github.io/find_link_text"
# browser = webdriver.Chrome()
#
# try:
#     browser.get(link)
#     time.sleep(20)
#     secret_link = str(math.ceil(math.pow(math.pi, math.e)*10000))
#     link2 = browser.find_element_by_link_text(secret_link)
#     link2.click()
#     input1 = browser.find_element_by_tag_name("input")
#     input1.send_keys("Ivan")
#     input2 = browser.find_element_by_name("last_name")
#     input2.send_keys("Petrov")
#     input3 = browser.find_element_by_class_name("city")
#     input3.send_keys("Smolensk")
#     input4 = browser.find_element_by_id("country")
#     input4.send_keys("Russia")
#     button = browser.find_element_by_css_selector("button.btn")
#     button.click()
#
# finally:
#     time.sleep(10)
#     browser.quit()
#
# try:
#     browser = webdriver.Chrome()
#     browser.get("http://suninjuly.github.io/huge_form.html")
#     elements = browser.find_elements_by_css_selector('[type="text"]')
#     for element in elements:
#        element.send_keys("Fuck you")
#
#     button = browser.find_element_by_css_selector("button.btn")
#     button.click()
#
# finally:
#     # успеваем скопировать код за 30 секунд
#     time.sleep(30)
#     # закрываем браузер после всех манипуляций
#     browser.quit()


# link = "http://suninjuly.github.io/find_xpath_form"
# browser = webdriver.Chrome()
#
# try:
#     browser.get(link)
#     input1 = browser.find_element_by_tag_name("input")
#     input1.send_keys("Ivan")
#     input2 = browser.find_element_by_name("last_name")
#     input2.send_keys("Petrov")
#     input3 = browser.find_element_by_class_name("city")
#     input3.send_keys("Smolensk")
#     input4 = browser.find_element_by_id("country")
#     input4.send_keys("Russia")
#     button = browser.find_element_by_xpath("//button[text()='Submit']")
#     button.click()
#
# finally:
#     time.sleep(10)
#     browser.quit()

# old correct link
# from selenium import webdriver
# import time
#
# try:
#     link = "http://suninjuly.github.io/registration1.html"
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     input1 = browser.find_element_by_css_selector('[placeholder="Input your first name"]')
#     input1.send_keys("Алексей")
#     input2 = browser.find_element_by_css_selector('[placeholder="Input your last name"]')
#     input2.send_keys("Навальный")
#     input3 = browser.find_element_by_css_selector('[placeholder="Input your email"]')
#     input3.send_keys("fbk@fbk.info")
#
#     # Отправляем заполненную форму
#     button = browser.find_element_by_css_selector("button.btn")
#     button.click()
#
#     # Проверяем, что смогли зарегистрироваться
#     # ждем загрузки страницы
#     time.sleep(2)
#
#     # находим элемент, содержащий текст
#     welcome_text_elt = browser.find_element_by_tag_name("h1")
#     # записываем в переменную welcome_text текст из элемента welcome_text_elt
#     welcome_text = welcome_text_elt.text
#
#     # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
#     assert "Congratulations! You have successfully registered!" == welcome_text
#
# finally:
#     # ожидание чтобы визуально оценить результаты прохождения скрипта
#     time.sleep(10)
#     # закрываем браузер после всех манипуляций
#     browser.quit()


# new link with bug
# from selenium import webdriver
# import time
#
# try:
#     link = "http://suninjuly.github.io/registration1.html"
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     input1 = browser.find_element_by_xpath("//div[@class='form-group first_class']//input[contains(@placeholder,'name')]")
#     input1.send_keys("Алексей")
#     input2 = browser.find_element_by_css_selector('[placeholder="Input your last name"]')
#     input2.send_keys("Навальный")
#     input3 = browser.find_element_by_css_selector('[placeholder="Input your email"]')
#     input3.send_keys("fbk@fbk.info")
#
#     # Отправляем заполненную форму
#     button = browser.find_element_by_css_selector("button.btn")
#     button.click()
#
#     # Проверяем, что смогли зарегистрироваться
#     # ждем загрузки страницы
#     time.sleep(2)
#
#     # находим элемент, содержащий текст
#     welcome_text_elt = browser.find_element_by_tag_name("h1")
#     # записываем в переменную welcome_text текст из элемента welcome_text_elt
#     welcome_text = welcome_text_elt.text
#
#     # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
#     assert "Congratulations! You have successfully registered!" == welcome_text
#
# finally:
#     # ожидание чтобы визуально оценить результаты прохождения скрипта
#     time.sleep(10)
#     # закрываем браузер после всех манипуляций
#     browser.quit()


# from selenium import webdriver
# import math
# def calc(x):
#   return str(math.log(abs(12*math.sin(int(x)))))
#
# browser = webdriver.Chrome()
#
# try:
#     browser.get('http://suninjuly.github.io/math.html')
#     value_1 = browser.find_element_by_css_selector("[id=input_value]")
#     x = value_1.text
#     digit1 = calc(x)
#     x_element = browser.find_element_by_id('answer')
#     x_element.send_keys(digit1)
#
#     check_box = browser.find_element_by_css_selector("[id=robotCheckbox]")
#     check_box.click()
#     radio_btn = browser.find_element_by_css_selector("[id=robotsRule]")
#     radio_btn.click()
#     submit_btn = browser.find_element_by_css_selector("[type=submit]")
#     submit_btn.click()
#
# finally:
#     time.sleep(15)
#     browser.quit()


# from selenium import webdriver
# import math
# def calc(x):
#   return str(math.log(abs(12*math.sin(int(x)))))
#
# browser = webdriver.Chrome()
#
# try:
#     browser.get('http://suninjuly.github.io/get_attribute.html')
#     value_1 = browser.find_element_by_css_selector('[id=treasure]')
#     t = value_1.get_attribute("valuex")
#     digit1 = calc(t)
#     x_element = browser.find_element_by_id('answer')
#     x_element.send_keys(digit1)
#
#     check_box = browser.find_element_by_css_selector("[id=robotCheckbox]")
#     check_box.click()
#     radio_btn = browser.find_element_by_css_selector("[id=robotsRule]")
#     radio_btn.click()
#     submit_btn = browser.find_element_by_css_selector("[type=submit]")
#     submit_btn.click()
#
# finally:
#     time.sleep(15)
#     browser.quit()


# from selenium import webdriver
# from selenium.webdriver.support.ui import Select
#
# browser = webdriver.Chrome()
#
# try:
#     browser.get('http://suninjuly.github.io/selects2.html')
#     #browser.get('http://suninjuly.github.io/selects1.html')
#     num1 = int(browser.find_element_by_id('num1').text)
#     num2 = int(browser.find_element_by_id('num2').text)
#     summa = str(num1 + num2)
#     select = Select(browser.find_element_by_tag_name("select"))
#     select.select_by_value(summa)
#     submit_btn = browser.find_element_by_css_selector("[type=submit]")
#     submit_btn.click()
#
# finally:
#     time.sleep(15)
#     browser.quit()

# from selenium import webdriver
#
# browser = webdriver.Chrome()
# link = "https://SunInJuly.github.io/execute_script.html"
# browser.get(link)
# button = browser.find_element_by_tag_name("button")
# button.click()
# assert True

# from selenium import webdriver
# import math
# def calc(x):
#   return str(math.log(abs(12*math.sin(int(x)))))
#
# browser = webdriver.Chrome()
#
# try:
#     browser.get('http://suninjuly.github.io/get_attribute.html')
#     value_1 = browser.find_element_by_css_selector('[id=treasure]')
#     t = value_1.get_attribute("valuex")
#     digit1 = calc(t)
#     x_element = browser.find_element_by_id('answer')
#     x_element.send_keys(digit1)
#
#     check_box = browser.find_element_by_css_selector("[id=robotCheckbox]")
#     check_box.click()
#     radio_btn = browser.find_element_by_css_selector("[id=robotsRule]")
#     radio_btn.click()
#     submit_btn = browser.find_element_by_css_selector("[type=submit]")
#     submit_btn.click()
#
# finally:
#     time.sleep(15)
#     browser.quit()


# from selenium import webdriver
# from selenium.webdriver.support.ui import Select
# import math
#
# browser = webdriver.Chrome()
#
#
# def calc(x):
#     return str(math.log(abs(12 * math.sin(int(x)))))
#
#
# try:
#     browser.get('http://suninjuly.github.io/execute_script.html')
#     num1 = browser.find_element_by_id("input_value").text
#     x = calc(num1)
#     answer = browser.find_element_by_id("answer")
#     answer.send_keys(x)
#     box = browser.find_element_by_id("robotCheckbox")
#     box.click()
#     radio = browser.find_element_by_id("robotsRule")
#     browser.execute_script("return arguments[0].scrollIntoView(true);", radio)
#     radio.click()
#     submit_btn = browser.find_element_by_css_selector("[type=submit]")
#     submit_btn.click()
#     # select = Select(browser.find_element_by_tag_name("select"))
#     # select.select_by_value(summa)
#
#
# finally:
#     time.sleep(7)
#     browser.quit()


# from selenium import webdriver
# import time
# import os
#
# browser = webdriver.Chrome()
# current_dir = os.path.abspath(os.path.dirname('Start.py'))
# file = "test.py"
# file_path = os.path.join(current_dir, "test.txt")
#
# try:
#     link = "http://suninjuly.github.io/file_input.html"
#     browser.get(link)
#
#     input1 = browser.find_element_by_css_selector('[placeholder="Enter first name"]').send_keys("Алексей")
#     input2 = browser.find_element_by_css_selector('[placeholder="Enter last name"]').send_keys("Навальный")
#     input3 = browser.find_element_by_css_selector('[placeholder="Enter email"]').send_keys("fbk@fbk.info")
#     input4 = browser.find_element_by_id('file').send_keys(file_path)
#     submit_btn = browser.find_element_by_css_selector("[type=submit]").click()
#
# finally:
#     time.sleep(7)
#     browser.quit()


# from selenium import webdriver
# import time
import os
#
# browser = webdriver.Chrome()
from selenium.webdriver.support.ui import Select
# current_dir = os.path.abspath(os.path.dirname('Start.py'))
# file = "test.py"
# file_path = os.path.join(current_dir, "test.txt")
#
# try:
#     link = "https://vk.com/edit"
#     browser.get(link)
#     login = str(89527022225)
#     passw = "Cbrrbc1999!"
#
#     input0 = browser.find_element_by_id('email').send_keys(login)
#     input1 = browser.find_element_by_id('pass').send_keys(passw)
#     input2 = browser.find_element_by_id('login_button').click()
#     time.sleep(3)
#     input4 = browser.find_element_by_xpath("//li[@id='l_pr']//span[contains(@class,'left_label inl_bl')]").click()
#     time.sleep(3)
#     input3 = browser.find_element_by_xpath("//div//a[@id='profile_edit_act']").click()
#     time.sleep(3)
#     input5 = browser.find_element_by_id("dropdown2").click()
#     input6 = browser.find_element_by_id("option_list_options_container_2_3").click()
#     input7 = browser.find_element_by_xpath("//*[@id='container2']/table/tbody/tr/td[1]/input[1]")
#     t = input7.get_attribute("value")
#     print(t)
#     assert t == "Встречаюсь", "Нихуя не получилось"

# try:
    # browser.get('http://suninjuly.github.io/selects2.html')
    # browser.get('http://suninjuly.github.io/selects1.html')
    # num1 = int(browser.find_element_by_id('num1').text)
    # num2 = int(browser.find_element_by_id('num2').text)
    # summa = str(num1 + num2)
    # select = Select(browser.find_element_by_tag_name("select")).select_by_value(summa)
    # nub = browser.find_element_by_tag_name("select").get_attribute("value")
    # print(nub)
#     submit_btn = browser.find_element_by_css_selector("[type=submit]")
#     submit_btn.click()
#
# finally:
#     time.sleep(15)
#     browser.quit()


# from selenium import webdriver
# from selenium.webdriver.support.ui import Select
# import math
#
# browser = webdriver.Chrome()
#
#
# def calc(x):
#     return str(math.log(abs(12 * math.sin(int(x)))))
#
#
# try:
#     browser.get('http://suninjuly.github.io/execute_script.html')
#     num1 = browser.find_element_by_id("input_value").text
#     x = calc(num1)
#     answer = browser.find_element_by_id("answer")
#     answer.send_keys(x)
#     box = browser.find_element_by_id("robotCheckbox")
#     box.click()
#     radio = browser.find_element_by_id("robotsRule")
#     browser.execute_script("arguments[0].scrollIntoView(true);", radio)
#     radio.click()
#     submit_btn = browser.find_element_by_css_selector("[type=submit]")
#     submit_btn.click()
#     # select = Select(browser.find_element_by_tag_name("select"))
#     # select.select_by_value(summa)
#
#
# finally:
#     time.sleep(7)
#     browser.quit()

# from selenium import webdriver
# from selenium.webdriver.support.ui import Select
# import math
#
# browser = webdriver.Chrome()
#
#
# def calc(x):
#     return str(math.log(abs(12 * math.sin(int(x)))))
#
#
# try:
#     browser.get('http://suninjuly.github.io/alert_accept.html')
#     box = browser.find_element_by_css_selector('[type = "Submit"]').click()
#     t = browser.switch_to.alert
#     t.accept()
#     a = browser.find_element_by_id("input_value").text
#     c = calc(a)
#     r = browser.find_element_by_id("answer").send_keys(c)
#     submit_btn = browser.find_element_by_css_selector("[type=submit]").click()
#     # select = Select(browser.find_element_by_tag_name("select"))
#     # select.select_by_value(summa)
#
#
# finally:
#     time.sleep(7)
#     browser.quit()


# from selenium import webdriver
# from selenium.webdriver.support.ui import Select
# import math
# import time
#
# browser = webdriver.Chrome()
#
#
# def calc(x):
#     return str(math.log(abs(12 * math.sin(int(x)))))
#
#
# try:
#     browser.get('http://suninjuly.github.io/redirect_accept.html')
#     box = browser.find_element_by_css_selector('[type = "Submit"]').click()
#     e = browser.window_handles
#     print(e)
#     second_window = browser.window_handles[1]
#     second_window_switch = browser.switch_to.window(second_window)
#     i = browser.current_window_handle
#     print(i)
#     a = browser.find_element_by_id("input_value").text
#     c = calc(a)
#     r = browser.find_element_by_id("answer").send_keys(c)
#     submit_btn = browser.find_element_by_css_selector("[type=submit]").click()
#     # select = Select(browser.find_element_by_tag_name("select"))
#     # select.select_by_value(summa)
#
#
# finally:
#     time.sleep(7)
#     browser.quit()

from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
#
# browser = webdriver.Chrome()
#
# browser.get("http://suninjuly.github.io/wait2.html")
#
# # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
# button = WebDriverWait(browser, 5).until(
#         EC.element_to_be_clickable.find_element_by_id("verify")
#     )
# button.click()
# message = browser.find_element_by_id("verify_message")
#
# assert "successful" in message.text


from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

browser = webdriver.Chrome()

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser.get('http://suninjuly.github.io/explicit_wait2.html')
    price = WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '$100'))
    book_btn = browser.find_element(By.ID, 'book').click()

    a = browser.find_element_by_id("input_value").text
    c = calc(a)
    r = browser.find_element_by_id("answer").send_keys(c)
    submit_btn = browser.find_element_by_css_selector("[type=submit]").click()


finally:
    time.sleep(5)
    browser.quit()