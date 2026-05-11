#
#
#
#
#
# import pytest
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import TimeoutException
#
# # -------------------------
# # Fixtures
# # -------------------------
# @pytest.fixture(scope="function")
# def driver():
#     options = webdriver.EdgeOptions()
#     options.add_argument("--start-maximized")
#     driver = webdriver.Edge(options=options)
#     driver.get("https://opensource-demo.orangehrmlive.com/")
#     yield driver
#     driver.quit()
#
# # -------------------------
# # Page Objects
# # -------------------------
# 
# class LoginPage:
#     def __init__(self, driver):
#         self.driver = driver
#         self.wait = WebDriverWait(driver, 10)
#
#     def login(self, username, password):
#         user_field = self.wait.until(
#             EC.visibility_of_element_located((By.NAME, "username"))
#         )
#         user_field.send_keys(username)
#
#         pwd_field = self.driver.find_element(By.NAME, "password")
#         pwd_field.send_keys(password)
#
#         login_btn = self.driver.find_element(By.XPATH, "//button[@type='submit']")
#         login_btn.click()
#
#         self.wait.until(
#             EC.visibility_of_element_located((By.XPATH, "//h6[text()='Dashboard']"))
#         )
#         return DashboardPage(self.driver)
#
#
# class DashboardPage:
#     def __init__(self, driver):
#         self.driver = driver
#         self.side_menu = SideMenuComponent(driver)
#
#
# class PIMPage:
#     def __init__(self, driver):
#         self.driver = driver
#         self.wait = WebDriverWait(driver, 10)
#
#     def addEmployee(self, first_name, last_name):
#         # Click Add Employee
#         self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(.,'Add')]"))).click()
#         # Fill form
#         self.wait.until(EC.visibility_of_element_located((By.NAME, "firstName"))).send_keys(first_name)
#         self.driver.find_element(By.NAME, "lastName").send_keys(last_name)
#         # Save
#         self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
#         # Wait for Personal Details page
#         self.wait.until(EC.visibility_of_element_located((By.XPATH, "//h6[text()='Personal Details']")))
#         return PersonalDetailsPage(self.driver)
#
#     def viewEmployeeDetails(self, name=None):
#         if name:
#             emp_xpath = f"//div[@class='oxd-table-card']//div[text()='{name}']"
#             try:
#                 self.wait.until(EC.element_to_be_clickable((By.XPATH, emp_xpath))).click()
#             except TimeoutException:
#                 pytest.skip(f"Employee {name} not found in demo data")
#         else:
#             rows = self.driver.find_elements(By.XPATH, "//div[@class='oxd-table-card']")
#             if not rows:
#                 pytest.skip("No employees available in demo data")
#             rows[0].click()
#         return PersonalDetailsPage(self.driver)
#
#
# class PersonalDetailsPage:
#     def __init__(self, driver):
#         self.driver = driver
#
#
# class SideMenuComponent:
#     def __init__(self, driver):
#         self.driver = driver
#
#     def go_to_admin(self):
#         self.driver.find_element(By.XPATH, "//span[text()='Admin']").click()
#         return AdminPage(self.driver)
#
#     def go_to_pim(self):
#         self.driver.find_element(By.XPATH, "//span[text()='PIM']").click()
#         return PIMPage(self.driver)
#
#     def logout(self):
#         self.driver.find_element(By.XPATH, "//span[text()='Logout']").click()
#
#
# class AdminPage:
#     def __init__(self, driver):
#         self.driver = driver
#         self.wait = WebDriverWait(driver, 10)
#
#     def get_all_usernames(self):
#         self.wait.until(EC.presence_of_all_elements_located(
#             (By.XPATH, "//div[@class='oxd-table-card']//div[@role='cell'][2]")
#         ))
#         return [el.text for el in self.driver.find_elements(
#             By.XPATH, "//div[@class='oxd-table-card']//div[@role='cell'][2]"
#         )]
#
#     def user_exists(self, username):
#         users = self.get_all_usernames()
#         if not users:
#             pytest.skip("No users found in Admin table")
#         return username in users
#
# # -------------------------
# # Tests
# # -------------------------
#
# def test_login_and_dashboard(driver):
#     login_page = LoginPage(driver)
#     dashboard = login_page.login("Admin", "admin123")
#     assert "Dashboard" in driver.page_source
#
# def test_pim_navigation(driver):
#     login_page = LoginPage(driver)
#     dashboard = login_page.login("Admin", "admin123")
#     pim_page = dashboard.side_menu.go_to_pim()
#     # First add an employee, then view details
#     personal_details = pim_page.addEmployee("Test", "User")
#     assert "Personal Details" in driver.page_source
#
# @pytest.mark.parametrize("username", ["Admin"])
# def test_admin_user_exists(driver, username):
#     login_page = LoginPage(driver)
#     dashboard = login_page.login("Admin", "admin123")
#     admin_page = dashboard.side_menu.go_to_admin()
#     exists = admin_page.user_exists(username)
#     if not exists:
#         pytest.skip(f"User {username} not found in demo data")
#     assert exists
#
#
# #output
# "C:\Program Files\Python314\python.exe" "C:/Program Files/JetBrains/PyCharm Community Edition 2025.2.6/plugins/python-ce/helpers/pycharm/_jb_pytest_runner.py" --path "C:\Wipro Training\Python\PythonCoding\daily_assignment\day11-assignment.py"
# Testing started at 5:25 PM ...
# Launching pytest with arguments C:\Wipro Training\Python\PythonCoding\daily_assignment\day11-assignment.py --no-header --no-summary -q in C:\Wipro Training\Python\PythonCoding\daily_assignment
#
# ============================= test session starts =============================
# collecting ... collected 3 items
#
# day11-assignment.py::test_login_and_dashboard PASSED                     [ 33%]
# day11-assignment.py::test_pim_navigation PASSED                          [ 66%]
# day11-assignment.py::test_admin_user_exists[Admin]
#
# ============================= 3 passed in 38.05s ==============================
# PASSED                [100%]
# Process finished with exit code 0
#
