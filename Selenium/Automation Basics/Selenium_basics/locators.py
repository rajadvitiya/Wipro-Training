import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.relative_locator import locate_with

# from Selenium_basics.google_homepage_test import browser

# browser = input('brower')

driver_path = r"C:\Wipro Training\Selenium\Automation Basics\resources\msedgedriver.exe"
service = Service(driver_path)
driver = webdriver.Edge(service=service)
# driver.get("https://www.google.com")

#ID
# search_input = driver.find_element(By.ID,"APjFqb")
# search_input.send_keys("selenium")
# time.sleep(3)
# search_input.clear()
# driver.quit()

#name
# search_input = driver.find_element(By.NAME, "q")
# search_input.send_keys("locators")
# time.sleep(3)

#Name
# google_search_button = driver.find_element(By.NAME, "btnK")
# google_search_button.click()
# time.sleep(30)


#Classname
# imfl_button = driver.find_element(By.CLASS_NAME, "RNmpXc")
# imfl_button.click()
# time.sleep(30)


#tagname
# href_elements = driver.find_elements(By.TAG_NAME, "a")
# for elmt in href_elements:
#     print(f'{elmt.text} - {elmt.get_attribute("href")}')

#Linktext
# images_link = driver.find_element(By.LINK_TEXT, "Images")
# images_link.click()
# time.sleep(10)


#partial lt
# images_link = driver.find_element(By.PARTIAL_LINK_TEXT, "Images")
# images_link.click()
# time.sleep(10)

#cssSelector
# search_input = driver.find_element(By.CSS_SELECTOR, 'div > textarea')
# search_input.send_keys('selenium')
# time.sleep(5)



#xpath
# setting_text = driver.find_element(By.XPATH, "/html/body/div[2]/div[7]/div/div[2]/div[1]/a[1]")
#
# print(setting_text.text)
# time.sleep(3)

driver.get("https://the-internet.herokuapp.com/tables")

# time.sleep(3)
#
#
# #and / or exaample
# and_example = driver.find_element(By.XPATH,"//td[text()='Tim' and @class='first-name']")
# print(f"And Example :- Found with both conditions: {and_example.text}")
#
# or_example = driver.find_element(By.XPATH,"//td[text()='Tim' or @class='Frank']")
# print(f"Or Example :- Found with both conditions: {or_example.text}")
#
# # --- CHILD EXAMPLE ---
# # Select all <td> elements that are direct children of <tr> in the first table
# rows = driver.find_elements(By.XPATH, "//table[@id='table1']/tbody/tr/td")
# print(f"Child Example :- found {len(rows)} cells in the first table.")
#
# # --- PARENT EXAMPLE ---
# # Find the cell with specific text
# email_cell = driver.find_element(By.XPATH, "//table[@id='table1']//td[text()='jdoe@hotmail.com']")
#
# # Get the parent row of that cell
# parent_row = email_cell.find_element(By.XPATH, "./parent::tr")
#
# # Print the text of the entire row
# print("Parent Example :- Row text:", parent_row.text)
# # --- ANCESTOR EXAMPLE ---
# # Get the table element that is an ancestor of a specific cell
# ancestor_table = driver.find_element(By.XPATH, "//td[text()='jsmith@gmail.com']/ancestor::table")
# print(f"Ancestor Example -> Table ID : {ancestor_table.get_attribute('id')}")
#
# # --- DESCENDANT EXAMPLE ---
# # Find all descendants (cells) under the table body
# descendants = driver.find_elements(By.XPATH, "//table[@id='table1']/tbody//td")
# print(f"Descendant Example -> found {len(descendants)} cells under table body.")
#
# # Optional: print each cell's text
# for cell in descendants:
#     print(cell.text)
#
# driver.quit()



driver.get("https://www.saucedemo.com/")
time.sleep(5)
#element used for reference

# Locate username, password, and login button correctly
username_field = driver.find_element(By.ID, "user-name")
password_field = driver.find_element(By.ID, "password")
login_button = driver.find_element(By.ID, "login-button")  # <-- corrected ID

# --- ABOVE EXAMPLE ---
# Find the input element located above the password field (username field)
elmt_above_password = driver.find_element(
    locate_with(By.TAG_NAME, "input").above(password_field)
)
print(f"Above Example -> Placeholder above password: {elmt_above_password.get_attribute('placeholder')}")
elmt_above_password.send_keys('standard_user')
time.sleep(2)

# --- BELOW EXAMPLE ---
# Find the element located below the password field (login button)
elmt_below_password = driver.find_element(
    locate_with(By.TAG_NAME, "input").below(password_field)
)
print(f"Below Example -> Placeholder below password: {elmt_below_password.get_attribute('placeholder')}")
password_field.send_keys('secret_sauce')  # type into password field

# Click the login button
login_button.click()
time.sleep(2)



# 1. to_right_of: Finds the element to the right of Twitter
twitter_icon = driver.find_element(By.LINK_TEXT, "Twitter")
facebook_icon = driver.find_element(locate_with(By.TAG_NAME, "a").to_right_of(twitter_icon))

print(f"Facebook icon href: {facebook_icon.get_attribute('href')}")

# 2. to_left_of: Finds the element to the left of Facebook
left_icon = driver.find_element(locate_with(By.TAG_NAME, "a").to_left_of(facebook_icon))

print(f"Element to the left of Facebook href: {left_icon.get_attribute('href')}")

# 3. near: Finds an element within 50px of the Twitter icon
near_twitter = driver.find_element(locate_with(By.TAG_NAME, "a").near(twitter_icon))

print(f"Element near Twitter href: {near_twitter.get_attribute('href')}")

time.sleep(5)
driver.quit()














