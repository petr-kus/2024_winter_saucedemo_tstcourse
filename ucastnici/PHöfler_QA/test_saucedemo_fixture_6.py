from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pytest

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    return driver

@pytest.fixture
def webpage():
    return "https://www.saucedemo.com"

@pytest.fixture
def webpage_product():
    return "https://www.saucedemo.com/inventory.html"

product_description = (By.CLASS_NAME, "inventory_item_name")

class TestWebPage:
    driver = webdriver.Chrome()
    def test_web_loading(self, webpage):
        self.driver.get(webpage)
        assert "Swag Labs" == self.driver.title

    @pytest.mark.parametrize("username, password", [("standard_user", "secret_sauce")])
    def test_login(self, username, password, webpage_product):
        self.driver.find_element(By.ID, "user-name").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()
        assert "inventory" in webpage_product

    """"Zde jsem zkoušel ověřit přidání zboží do košíku, na základě definovaného product_description výše, ale nevím, jak na to.
    def test_product_click(self):
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_badge").click()
        assert "Sauce Labs" in product_description
        self.driver.quit()"""