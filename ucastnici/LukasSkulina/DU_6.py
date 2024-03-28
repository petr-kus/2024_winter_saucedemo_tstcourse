import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def open_web_page(driver):
    driver.get("https://www.saucedemo.com/")
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "user-name")))

def slow_down():
    time.sleep(3)

class TestWebPage:

    @pytest.fixture(scope="class")
    def chrome_driver(self):
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)
        yield driver
        driver.quit()

    @pytest.mark.parametrize("username, password", [("standard_user","secret_sauce")])
    def test_login(self, chrome_driver, username, password):
        driver = chrome_driver
        try:
            open_web_page(driver)
            driver.find_element(By.ID, "user-name").send_keys(username)
            driver.find_element(By.ID, "password").send_keys(password)
            driver.find_element(By.ID, "login-button").click()
            print("Login successful!")
        except Exception as e:
            pytest.fail("An error occurred while logging in: {}".format(e))


    def test_add_item_to_cart(self, chrome_driver):
        driver = chrome_driver
        try:
            driver.find_element(By.ID, "item_4_title_link").click()
            driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
            print("Item added to cart successfully!")
        except Exception as e:
            pytest.fail("An error occurred while adding to cart: {}".format(e))

    @pytest.mark.parametrize("first_name, last_name, postal_code", [("Chandler","Bing","70030")])
    def test_checkout(self, chrome_driver, first_name, last_name, postal_code):
        driver = chrome_driver
        try:
            driver.find_element(By.ID, "shopping_cart_container").click()
            driver.find_element(By.ID, "checkout").click()
            driver.find_element(By.ID, "first-name").send_keys(first_name)
            driver.find_element(By.ID, "last-name").send_keys(last_name)
            driver.find_element(By.ID, "postal-code").send_keys(postal_code)
            driver.find_element(By.ID, "continue").click()
            driver.find_element(By.ID, "finish").click()
            driver.find_element(By.ID, "back-to-products").click()
            print("Checkout successful!")
        except Exception as e:
            pytest.fail("An error occurred while checking out: {}".format(e))


    def test_footerlink(self, chrome_driver):
        driver = chrome_driver
        try:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            driver.find_element(By.ID, "page_wrapper").find_element(By.TAG_NAME, "footer").find_element(By.TAG_NAME, "ul").find_element(By.TAG_NAME, "li").find_element(By.TAG_NAME, "a").click()
            driver.switch_to.window(driver.window_handles[0])
            print("Footer link clicked successfully!")
        except Exception as e:
            pytest.fail("An error occurred while clicking on footer link: {}".format(e))


    def test_logout(self, chrome_driver):
        driver = chrome_driver
        try:
            driver.find_element(By.ID, "react-burger-menu-btn").click()
            driver.find_element(By.ID, "logout_sidebar_link").click()
            print("Logout successful!")
        except Exception as e:
            pytest.fail("An error occurred while logging out: {}".format(e))


