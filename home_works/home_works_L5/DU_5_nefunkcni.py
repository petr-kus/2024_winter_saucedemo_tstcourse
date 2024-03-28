from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


class WebPage_Executor():

    def __init__(self):
        self.driver = webdriver.Chrome()

    def page_start(self, webpage):
        self.driver.get(webpage)
        

    def wait_time(self, seconds=4):
        time.sleep(seconds)

    def tear_down(self):
        self.driver.close()
        self.driver.quit()

class Test_Cases():
    
    def __init__(self, web_executor):
        self.web_executor = web_executor

    def wait_time(self, seconds=4):
        time.sleep(seconds)

    def test_login(self, login_name, password):
        self.web_executor.driver.find_element(By.ID,"user-name").send_keys(login_name)
        self.wait_time()
        self.web_executor.driver.find_element(By.ID,"password").send_keys(password)
        self.wait_time()
        self.web_executor.driver.find_element(By.ID,"login-button").click()
        self.wait_time()

    def test_add_to_cart(self):
        try:
            self.wait_time()
            self.web_executor.driver.find_element(By.ID,"item_4_title_link").click()
            self.wait_time()
            self.web_executor.driver.find_element(By.ID,"add-to-cart-sauce-labs-backpack").click()
            self.wait_time()
        except Exception as e:
            print(f"Chyba při pokusu o kliknutí na produkt: {e}")

    def test_checkout(self):
        self.web_executor.driver.find_element(By.ID,"shopping_cart_container").click()
        self.wait_time()
        self.web_executor.driver.find_element(By.ID,"checkout").click()
        self.wait_time()
        self.web_executor.driver.find_element(By.ID,"first-name").send_keys("Chandler")
        self.wait_time()
        self.web_executor.driver.find_element(By.ID,"last-name").send_keys("Bing")
        self.wait_time()
        self.web_executor.driver.find_element(By.ID,"postal-code").send_keys("70030")
        self.wait_time()
        self.web_executor.driver.find_element(By.ID,"continue").click()
        self.wait_time()
        self.web_executor.driver.find_element(By.ID,"finish").click()
        self.wait_time()
        self.web_executor.driver.find_element(By.ID,"back-to-products").click()
        self.wait_time()

    def test_footerlink(self):
        self.web_executor.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.wait_time()
        self.web_executor.driver.find_element(By.ID, "page_wrapper").find_element(By.TAG_NAME, "footer").find_element(By.TAG_NAME, "ul").find_element(By.TAG_NAME, "li").find_element(By.TAG_NAME, "a").click()
        self.wait_time()
        self.web_executor.driver.switch_to.window(self.web_executor.driver.window_handles[0])
        self.wait_time()

    def test_logout(self):
        self.web_executor.driver.find_element(By.ID, "react-burger-menu-btn").click()
        self.wait_time()
        self.web_executor.driver.find_element(By.ID, "logout_sidebar_link").click()
        self.wait_time()

web_executor = WebPage_Executor()
test_cases = Test_Cases(web_executor)

web_executor.page_start("https://www.saucedemo.com/")
test_cases.test_login("standard_user","secret_sauce")

web_executor.tear_down()
