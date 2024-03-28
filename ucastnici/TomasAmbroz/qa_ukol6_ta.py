from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pytest

@pytest.fixture
def webpage():
    return "https://www.saucedemo.com/"

@pytest.fixture
def login_name():
    return "problem_user"

@pytest.fixture
def password():
    return "secret_sauce"

def my_wait():
    time.sleep(1)
class TestWebPage:
    driver = webdriver.Chrome()
    
    def test_setup(self, webpage):
        self.driver.get(webpage)
        my_wait()

    def test_login(self, login_name, password):
        """ This is testing login to the page"""
        self.driver.find_element(By.ID,"user-name").send_keys(login_name)
        my_wait()
        self.driver.find_element(By.ID,"password").send_keys(password)
        my_wait()
        self.driver.find_element(By.ID,"login-button").click()
        my_wait()
        self.driver.find_element(By.ID,"item_4_title_link").click()
        my_wait()
        self.driver.find_element(By.ID,"add-to-cart-sauce-labs-fleece-jacket").click()

    def test_teardown(self):
        self.driver.close()
        self.driver.quit()
