from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
import os

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/file_input.html")
    browser.find_element(By.NAME,"firstname").send_keys("Dima")
    browser.find_element(By.NAME,"lastname").send_keys("Shelikhov")
    browser.find_element(By.NAME,"email").send_keys("sisajdioasdsdi")
    e = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'ReadMe.txt')
    browser.find_element(By.NAME,"file").send_keys(e)
    browser.find_element(By.XPATH,"/html/body/div/form/button").click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла