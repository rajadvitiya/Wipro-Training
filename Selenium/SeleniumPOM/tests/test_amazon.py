from pages.home_page import HomePage


def test_open_amazon(driver):
    assert "amazon" in driver.current_url.lower(), "Amazon homepage not opened"
    print("\nOpened Amazon Homepage. Title verified")


def test_search_product(driver):
    homepage = HomePage(driver)

    homepage.type_search_input()
    homepage.click_search_button()

    assert homepage.is_amazon_page_loaded() ,  'Search results page did not load'
