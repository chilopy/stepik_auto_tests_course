import time 
import math
from selenium import webdriver

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/redirect_accept.html"

try:
  chrome_options = webdriver.ChromeOptions()
  chrome_options.add_argument("--remote-debugging-port=9222")  # this
  browser = webdriver.Chrome(chrome_options=chrome_options)
  browser.get(link)
  
  button = browser.find_element_by_css_selector("button.trollface")
  button.click()
  
  browser.switch_to.window(browser.window_handles[1])

  x = browser.find_element_by_id("input_value").text
  y = calc(x)
  ans = browser.find_element_by_id("answer")
  ans.send_keys(y)

  button = browser.find_element_by_css_selector("button.btn")
  button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла 
