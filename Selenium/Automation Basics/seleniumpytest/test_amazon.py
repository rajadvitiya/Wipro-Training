import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Edge()
    driver.maximize_window()
    driver.get("https://www.amazon.in")  # ✅ fixed URL
    yield driver
    driver.quit()


def test_open_amazon(driver):
    assert "amazon" in driver.current_url.lower(), "Amazon homepage not opened"
    print("\nOpened Amazon Homepage. Title verified")


def test_search_product(driver):
    wait = WebDriverWait(driver, 15)  # ⏱ increased timeout

    # ✅ Corrected locator and condition
    search_box = wait.until(EC.visibility_of_element_located((By.ID, "twotabsearchtextbox")))
    search_box.clear()
    search_box.send_keys("wireless mouse")

    search_button = driver.find_element(By.ID, "nav-search-submit-button")
    search_button.click()

    # Assertions
    assert "wireless" in driver.current_url.lower(), "Search results page did not load"
    assert "wireless" in driver.title.lower(), "Search result page did not open"
    print("\nSearch result page loaded successfully.")




def test_find_element_amazon(driver):
    wait = WebDriverWait(driver, 15)

    # ✅ More reliable selector for product titles
    first_product = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "span.a-text-normal"))
    )
    print("\nFirst Product:", first_product.text)

    # ✅ Get all product titles
    product_titles = driver.find_elements(By.CSS_SELECTOR, "span.a-text-normal")
    print(f"\nFound {len(product_titles)} product titles on page one.\n")

    # Print first 5 product titles
    for i, title in enumerate(product_titles[:5], start=1):
        print(f"{i}. {title.text}")

    # ✅ Assertion
    assert len(product_titles) > 0, "No products found on Amazon page results"