from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pytest

def my_wait():
    time.sleep(3)

@pytest.fixture 
def webpage():
        return "https://www.saucedemo.com/"
    
@pytest.fixture
def credentials():
        return {"login_name" : "standard_user",
                "password" : "secret_sauce"}
    
@pytest.fixture(scope="module")
def driver ():
        driver = webdriver.Chrome()
        yield driver
        driver.close()
        driver.quit()



class TestWebPage:
    driver = webdriver.Chrome()

    def test_setup(self, driver , webpage):
        self.driver.get(webpage)
        my_wait()
        

    def test_login(self, driver, credentials):
        self.driver.find_element(By.ID,"user-name").send_keys(credentials["login_name"])
        my_wait()
        self.driver.find_element(By.ID,"password").send_keys(credentials["password"])
        my_wait()
        self.driver.find_element(By.ID,"login-button").click()
        my_wait()

    def test_product(self, driver, product):
        self.driver.find_element(By.ID,product).click() 
        my_wait()

    def test_cart(self):
         self.driver.find_element(By.ID,"shopping_cart_container").click()
         my_wait()

    def test_continue_button(self):
        self.driver.find_element(By.ID,"continue-shopping").click() 
        my_wait()

    def test_teardown(self):
        self.driver.close()
        self.driver.quit()