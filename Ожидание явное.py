from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math
import os
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"),"100")
    )
    browser.find_element(By.XPATH,"/html/body/div/div/div/button").click()
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