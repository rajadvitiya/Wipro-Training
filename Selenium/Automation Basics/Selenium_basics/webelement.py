import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service

# driver_path = r"C:\Wipro Training\Selenium\Automation Basics\resources\msedgedriver.exe"
# service = Service(driver_path)
# driver = webdriver.Edge(service=service)

driver = webdriver.Edge()
driver.maximize_window()


driver.get("https://www.selenium.dev/selenium/web/web-form.html")
time.sleep(2)


text_input = driver.find_element(By.ID, "my-text-id" )
text_input.clear()
text_input.send_keys("Selenium webdriver demo")


password_input = driver.find_element(By.NAME, "my-password")
password_input.clear()
password_input.send_keys("secret123")

textarea = driver.find_element(By.NAME, 'my-textarea')
textarea.clear()
textarea.send_keys("This is a sample message")


chcekbox = driver.find_element(By.ID, "my-check-2")
chcekbox.click()


radio = driver.find_element(By.ID, "my-radio-2")
radio.click()


dropdown = driver.find_element(By.NAME, 'my-select')
dropdown.click()
option = driver.find_element(By.CSS_SELECTOR, "select[name='my-select'] option[value='2']")
option.click()


multi_select = driver.find_element(By.NAME, "my-datalist")
multi_select.send_keys('New York')
time.sleep(5)


fileupload = driver.find_element(By.NAME, 'my-file')
fileupload.send_keys(r"C:/Wipro Training/Selenium/Automation Basics/Selenium_basics/waits.py")




range_slider = driver.find_element(By.NAME, 'my-range')
driver.execute_script("arguments[0].value = 10;", range_slider)

time.sleep(10)


color_picker = driver.find_element(By.NAME, 'my-colors')
color_picker.send_keys('#00ff00')


date_input = driver.find_element(By.NAME, 'my-date')
date_input.send_keys("2025-12-25")


submit_btn = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
time.sleep(20)
submit_btn.click()

time.sleep(20)
driver.quit()







