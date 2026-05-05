import pytest
import pytest_check as check   # ✅ use pytest-check for soft assertions
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Edge()
    driver.maximize_window()
    driver.get('https://www.google.com')   # ✅ fixed URL
    yield driver
    driver.quit()


def test_ghpload(driver):
    pagetitle = driver.title
    check.equal(pagetitle, 'Google', 'Google Home Page Not Loaded')   # soft assert


def test_imagesload(driver):
    driver.find_element(By.LINK_TEXT, 'Images').click()
    pagetitle = driver.title
    check.is_in('Google Images', pagetitle, 'Images Page Not Loaded')   # soft assert


def test_businessload(driver):
    driver.find_element(By.PARTIAL_LINK_TEXT, 'Business').click()

    wait = WebDriverWait(driver, 10)
    wait.until(EC.title_contains('Business'))
    wait.until(EC.url_contains('business'))   # ✅ lowercase

    # Soft assertions
    check.is_in('Business', driver.title, 'Business Page is not loaded - title check')
    check.is_in('business', driver.current_url.lower(), 'Business Page is not loaded - url check')
