from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
import os
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/redirect_accept.html")
    browser.find_element(By.CLASS_NAME,"btn-primary").click()
    browser.switch_to.window(browser.window_handles[1])
    x = int(browser.find_element(By.ID,"input_value").text)
    x = calc(x)
    browser.find_element(By.ID,"answer").send_keys(x)
    time.sleep(1)
    browser.find_element(By.XPATH,"/html/body/form/div/div/button").click()
    e = browser.switch_to.alert.text
    print(e.split()[-1])
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла