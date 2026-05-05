import time

from selenium import webdriver
from selenium.webdriver.edge.service import Service

driver_path = r"C:\Wipro Training\Selenium\Automation Basics\resources\msedgedriver.exe"
service = Service(driver_path)
driver = webdriver.Edge(service=service)


driver.get("https://www.google.com/")
time.sleep(3)


driver.get("https://www.wikipedia.com/")
time.sleep(3)

driver.back()
time.sleep(3)
driver.forward()
time.sleep(3)
driver.back()
time.sleep(3)
driver.refresh()
time.sleep(3)

driver.quit()

