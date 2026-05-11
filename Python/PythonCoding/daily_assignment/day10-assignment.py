# # Exercise 1: Navigation and Title Verification
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import pytest
#
# def test_navigation_and_title():
#     driver = webdriver.Edge()
#     driver.get("https://www.amazon.in")
#
#     # Verify title contains "Amazon"
#     assert "Amazon" in driver.title
# 
#     wait = WebDriverWait(driver, 10)
#
#     # Navigate to Mobiles category (use explicit wait + robust locator)
#     mobiles_link = wait.until(
#         EC.element_to_be_clickable((By.XPATH, "//a[text()='Mobiles']"))
#     )
#     mobiles_link.click()
#
#     # Go back to home page
#     driver.back()
#     driver.quit()
#
#
# # Exercise 2: Basic Locators and Search
# def test_search_wireless_headphones():
#     driver = webdriver.Edge()
#     driver.get("https://www.amazon.in")
#
#     wait = WebDriverWait(driver, 10)
#
#     # Locate search bar by id
#     search_box = wait.until(
#         EC.presence_of_element_located((By.ID, "twotabsearchtextbox"))
#     )
#     search_box.send_keys("Wireless Headphones")
#
#     # Locate search button by xpath
#     search_button = driver.find_element(By.XPATH, "//input[@id='nav-search-submit-button']")
#     search_button.click()
#
#     # Verify results page contains expected text
#     assert "Wireless Headphones" in driver.page_source
#
#     driver.quit()
#
#
# # Exercise 3: Implementing Implicit and Explicit Waits
# def test_search_laptop_with_waits():
#     driver = webdriver.Edge()
#     driver.implicitly_wait(10)  # Implicit wait
#
#     driver.get("https://www.amazon.in")
#     driver.find_element(By.ID, "twotabsearchtextbox").send_keys("Dell Laptop")
#     driver.find_element(By.ID, "nav-search-submit-button").click()
#
#     # Explicit wait for results grid
#     wait = WebDriverWait(driver, 15)
#     first_result = wait.until(
#         EC.visibility_of_element_located((By.CSS_SELECTOR, "div.s-main-slot div[data-component-type='s-search-result']"))
#     )
#
#     # Click first result
#     first_result.click()
#     driver.quit()
#
#
# # Exercise 4: Advanced Locators (CSS Selectors & Links)
# def test_footer_about_us():
#     driver = webdriver.Edge()
#     driver.get("https://www.amazon.in")
#
#     wait = WebDriverWait(driver, 10)
#
#     # Scroll to footer and click About Us (Amazon India uses "About Amazon")
#     about_us_link = wait.until(
#         EC.element_to_be_clickable((By.LINK_TEXT, "About Amazon"))
#     )
#     about_us_link.click()
#
#     # Find element by link_text and print text
#     element = wait.until(
#         EC.presence_of_element_located((By.LINK_TEXT, "Careers"))
#     )
#     print("Footer About Us Page Element:", element.text)
#
#     driver.quit()
#
# def test_filter_smart_watches():
#     driver = webdriver.Edge()
#     driver.get("https://www.amazon.in")
#
#     wait = WebDriverWait(driver, 25)
#
#     # Search for Smart Watches
#     search_box = wait.until(
#         EC.presence_of_element_located((By.ID, "twotabsearchtextbox"))
#     )
#     search_box.send_keys("Smart Watches")
#     driver.find_element(By.ID, "nav-search-submit-button").click()
#
#     # Scroll down to filters section to trigger lazy loading
#     driver.execute_script("window.scrollBy(0, 2000);")
#
#     # Expand "See more" under Brand filter if present
#     try:
#         see_more = wait.until(
#             EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'See more')]/ancestor::a"))
#         )
#         driver.execute_script("arguments[0].click();", see_more)
#     except Exception:
#         pass  # If "See more" is not present, continue
#
#     # Robust locator for brand filter (case-insensitive, matches NOISE)
#     brand_filter_xpath = (
#         "//span[contains(translate(., 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'noise')]"
#         "/ancestor::label//input[@type='checkbox']"
#     )
#
#     brand_filter = wait.until(EC.presence_of_element_located((By.XPATH, brand_filter_xpath)))
#     driver.execute_script("arguments[0].scrollIntoView(true);", brand_filter)
#     driver.execute_script("arguments[0].click();", brand_filter)
#
#     # Wait for products to refresh after filter
#     wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "span.a-text-normal")))
#
#     products = driver.find_elements(By.CSS_SELECTOR, "span.a-text-normal")
#     print(f"Found {len(products)} Noise Smart Watches on first page.")
#
#     driver.quit()
#
#
#     #output
#     == == == == == == == == == == == == == == = test
#     session
#     starts == == == == == == == == == == == == == == =
#     collecting...collected
#     5
#     items
#
#     day10 - assignment.py::test_navigation_and_title
#     PASSED[20 %]
#     day10 - assignment.py::test_search_wireless_headphones
#     PASSED[40 %]
#     day10 - assignment.py::test_search_laptop_with_waits
#     PASSED[60 %]
#     day10 - assignment.py::test_footer_about_us
#     PASSED[80 %]
#     Footer
#     About
#     Us
#     Page
#     Element: Careers
#
#     day10 - assignment.py::test_filter_smart_watches
#     FAILED[100 %]
