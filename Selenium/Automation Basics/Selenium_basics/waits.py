import time
from re import search

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.wait import WebDriverWait

driver_path = r"C:\Wipro Training\Selenium\Automation Basics\resources\msedgedriver.exe"
service = Service(driver_path)
driver = webdriver.Edge(service=service)


driver.get("https://www.google.com/")

# driver.implicitly_wait(5)
# search_box = driver.find_element(By.NAME, "btnK")
# search_box.click()
# time.sleep(30)


from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Explicit Wait: waits up to 10 seconds for element to be visible
# wait = WebDriverWait(driver, 10
#
# # Wait for search box
# search_box = wait.until(EC.visibility_of_element_located((By.NAME, "q")))
# search_box.send_keys("Explicit wait")
#
# # Wait for search button
# search_button = wait.until(EC.visibility_of_element_located((By.NAME, "btnK")))
# search_button.click()

# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import NoSuchElementException
#
# # Fluent Wait: waits up to 20 seconds, checks every 2 seconds
# fluent_wait = WebDriverWait(driver, timeout=20, poll_frequency=2, ignored_exceptions=[NoSuchElementException])
#
# # Wait for search box
# search_box = fluent_wait.until(EC.visibility_of_element_located((By.NAME, "q")))
# search_box.send_keys("Fluent wait")
#
# # Wait for search button
# search_button = fluent_wait.until(EC.element_to_be_clickable((By.NAME, "btnK")))
# search_button.click()

