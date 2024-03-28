from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def wait_time():
    time.sleep(3)

class TestWebPage():
    driver = webdriver.Chrome()

    def page_start(self, webpage):
        try:
            self.driver.get(webpage)
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.ID, "user-name")))
        except Exception as e:
            print("An error occurred while loading the page:", e)

    def test_teardown(self):
        try:
            self.driver.close()
            self.driver.quit()
        except Exception as e:
            print("An error occurred while closing the browser:", e)

    def test_login(self, login_name, password):
        try:
            self.driver.find_element(By.ID,"user-name").send_keys(login_name)
            wait_time()
            self.driver.find_element(By.ID,"password").send_keys(password)
            wait_time()
            self.driver.find_element(By.ID,"login-button").click()
            wait_time()
        except Exception as e:
            print("An error occurred while logging in:", e)

    def test_add_to_cart(self):
        try:
            self.driver.find_element(By.ID,"item_4_title_link").click()
            wait_time()
            self.driver.find_element(By.ID,"add-to-cart-sauce-labs-backpack").click()
            wait_time()
        except Exception as e:
            print("An error occurred while adding to cart:", e)

    def test_checkout(self):
        try:
            self.driver.find_element(By.ID,"shopping_cart_container").click()
            wait_time()
            self.driver.find_element(By.ID,"checkout").click()
            wait_time()
            self.driver.find_element(By.ID,"first-name").send_keys("Chandler")
            wait_time()
            self.driver.find_element(By.ID,"last-name").send_keys("Bing")
            wait_time()
            self.driver.find_element(By.ID,"postal-code").send_keys("70030")
            wait_time()
            self.driver.find_element(By.ID,"continue").click()
            wait_time()
            self.driver.find_element(By.ID,"finish").click()
            wait_time()
            self.driver.find_element(By.ID,"back-to-products").click()
            wait_time()
        except Exception as e:
            print("An error occurred while checking out:", e)

    def test_footerlink(self):
        try:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            wait_time()
            self.driver.find_element(By.ID, "page_wrapper").find_element(By.TAG_NAME, "footer").find_element(By.TAG_NAME, "ul").find_element(By.TAG_NAME, "li").find_element(By.TAG_NAME, "a").click()
            wait_time()
            self.driver.switch_to.window(self.driver.window_handles[0])
            wait_time()
        except Exception as e:
            print("An error occurred while clicking on footer link:", e)

    def test_logout(self):
        try:
            self.driver.find_element(By.ID, "react-burger-menu-btn").click()
            wait_time()
            self.driver.find_element(By.ID, "logout_sidebar_link").click()
            wait_time()
        except Exception as e:
            print("An error occurred while logging out:", e)

web_page = TestWebPage()
web_page.page_start("https://www.saucedemo.com/")
web_page.test_login("standard_user","secret_sauce")
web_page.test_add_to_cart()
web_page.test_checkout()
web_page.test_footerlink()
web_page.test_logout()
web_page.test_teardown()
