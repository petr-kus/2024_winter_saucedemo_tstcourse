from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
import time
import pytest

@pytest.fixture(scope="module")
def browser():
    driver = webdriver.Chrome()
    return Browser(driver)

@pytest.fixture(scope="module")
def login_page(browser):
    return LoginPage(browser.driver)

@pytest.fixture(scope="module")
def shop_page(browser):
    return ShopPage(browser.driver)

class Browser:
    def __init__(self, driver):
        self.driver = driver

    def close_browser(self):
        self.driver.quit()

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        self.driver.find_element(By.ID, "user-name").send_keys(username)
        time.sleep(3)
        self.driver.find_element(By.ID, "password").send_keys(password)
        time.sleep(3)
        self.driver.find_element(By.ID, "login-button").click()
        time.sleep(3)

        # Overenie, ze prihlasenie bolo uspesne 
        assert "inventory" in self.driver.current_url
        print("Prihlasenie bolo uspesne.")

class ShopPage:
    def __init__(self, driver):
        self.driver = driver

    def click_all_items(self):
        item_id = 0
        while True:
            item_id_str = f"item_{item_id}_title_link"
            if not self.driver.find_elements(By.ID, item_id_str):
                print(f"Element with ID {item_id_str} not found")
                break

            try:
                self.driver.find_element(By.ID, item_id_str).click()
                time.sleep(3)
                self.driver.find_element(By.ID, "back-to-products").click()
                item_id += 1
            except NoSuchElementException:
                print(f"Element with ID {item_id_str} not found")
                break

        print("Vsetky polozky v obchode boli prekliknute.")

    def open_and_close_menu(self):
        self.driver.find_element(By.ID, "react-burger-menu-btn").click()
        time.sleep(3)
        self.driver.find_element(By.ID, "react-burger-cross-btn").click()
        time.sleep(10)

        print("Otvoril a zatvoril menu.")


def test_login(browser, login_page):
    username = "standard_user"
    password = "secret_sauce"
    login_page.login(username, password)

def test_shop_page(browser, shop_page):
    shop_page.click_all_items()
    shop_page.open_and_close_menu()
    browser.close_browser()
    print("Testovanie stranky obchodu bolo uspesne.")