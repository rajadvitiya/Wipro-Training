from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class ProductListingPage:
    # ✅ Amazon product titles are usually inside span.a-text-normal
    PRODUCT_TITLES = (By.CSS_SELECTOR, "span.a-size-medium.a-color-base.a-text-normal")
    # ✅ More robust brand filter locator (Amazon uses checkboxes/labels)


    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)  # increased timeout

    def find_product_title(self):
        # Wait for at least one product title to be visible
        self.wait.until(EC.visibility_of_element_located(self.PRODUCT_TITLES))
        first_product = self.driver.find_element(*self.PRODUCT_TITLES)
        print("\nFirst Product:", first_product.text)

    def all_products(self):
        # Wait until at least one product is visible
        self.wait.until(EC.visibility_of_element_located(self.PRODUCT_TITLES))

        # Collect all product titles
        product_titles = self.driver.find_elements(*self.PRODUCT_TITLES)
        print(f"\nFound {len(product_titles)} product titles on page one.\n")

        # Print first 5 product titles
        for i, title in enumerate(product_titles[:5], start=1):
            print(f"{i}. {title.text}")

        return len(product_titles) > 0

    def brand_filter_locator(self, brandname):
        brandname_locator = (By.XPATH, "//span[text()='" + brandname + "']/parent::a/descendant::i")

        return  brandname_locator

    def select_brand_filter(self,brandname):
        # Wait for brand filter element and click
        brand_filter = self.wait.until(EC.element_to_be_clickable(self.brand_filter_locator(brandname)))

        self.driver.execute_script("arguments[0].click();", brand_filter)  # JS click for reliability
        print("\nBrand filter applied: Logitech")

    def check_product_titles_for_brand_filter(self, brand_name):
        # Wait until products are visible after filter
        self.wait.until(EC.visibility_of_element_located(self.PRODUCT_TITLES))
        product_titles = self.driver.find_elements(*self.PRODUCT_TITLES)

        # Check if any product contains the brand name
        for title in product_titles[:10]:  # check first 10 for speed
            if brand_name.lower() in title.text.lower():
                print(f"Brand filter verified: {title.text}")
                return True
        return False


    def mensize_locator(self, mensize):
        mensize_filter = self.driver.find_element(*self.mensize_locator(mesize)))
        return mensize_filter

    def select_mesize_filter(self, mensize):
        mensize_filter = self.driver.find_element(*self.mensize_locator())


