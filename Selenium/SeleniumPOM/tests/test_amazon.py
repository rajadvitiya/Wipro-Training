import pytest

from pages.home_page import HomePage
from pages.product_listing_page import ProductListingPage


def test_open_amazon(driver):
    assert "amazon" in driver.current_url.lower(), "Amazon homepage not opened"
    print("\nOpened Amazon Homepage. Title verified")

@pytest.mark.parametrize("search_product", [("wireless mouse"),("shoes")])
def test_search_product(driver, search_product):
    homepage = HomePage(driver)

    homepage.type_search_input(search_product)
    homepage.click_search_button()

    assert homepage.is_amazon_page_loaded(), 'Search results page did not load'

@pytest.mark.parametrize("search_product", [("wireless mouse"),("shoes")])
def test_find_element_amazon(driver,search_product):
    homepage = HomePage(driver)

    homepage.type_search_input(search_product)
    homepage.click_search_button()
    product_listing_page = ProductListingPage(driver)

    product_listing_page.find_product_title()
    val = product_listing_page.all_products()

    assert val, "No products found on Amazon search results"
@pytest.mark.parametrize(("search_product","brandname"), [("wireless mouse","Logitech"),("shoes","Campus")])
def test_brand_filter(driver,search_product,brandname):
    homepage = HomePage(driver)

    homepage.type_search_input(search_product)
    homepage.click_search_button()
    product_listing_page = ProductListingPage(driver)

    # ✅ Now dynamic: pass brand name
    product_listing_page.select_brand_filter(brandname)
    product_listing_page.check_product_titles_for_brand_filter(brandname)

    assert product_listing_page.check_product_titles_for_brand_filter("Logitech"), "Brand filter did not apply"
