import pytest

from pages.home_page import HomePage
from pages.product_listing_page import ProductListingPage


@pytest.mark.parametrize(("search_product","brandname"),("search_product","brandname","mensize"), [("wireless mouse"),("shoes","Nike","9")])
def test_product_odering(driver,search_product,brandname):
    homepage = HomePage(driver)

    homepage.type_search_input(search_product)
    homepage.click_search_button()
    product_listing_page = ProductListingPage(driver)

    product_listing_page.find_product_title()
    val = product_listing_page.all_products()

    assert homepage.is_amazon_page_loaded(), 'Search results page '