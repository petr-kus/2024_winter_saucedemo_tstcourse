from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time 
import pytest

def my_wait():
    time.sleep(1)

@pytest.fixture
def webpage():
    return "https://www.saucedemo.com/"

@pytest.fixture
def credentials():
    return {"password"   : "secret_sauce", "login_name" : "standart_user"}
"""
@pytest.fixture 
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.close()
    driver.quit()
"""

class TestWebPage:
    driver = webdriver.Chrome()

    def test_setup(self, webpage):
        self.driver.get(webpage)
        my_wait()

    @pytest.mark.parametrize("password,loginame", [("secret_sauce","standart_user")])
    def test_login(self, password, loginame):
        """ This is testing login to the page"""

        self.driver.find_element(By.ID,"user-name").send_keys(loginame)
        my_wait()
        self.driver.find_element(By.ID,"password").send_keys(password)
        my_wait()
        self.driver.find_element(By.ID,"login-button").click()
        my_wait()
    
    def test_teardown(self):
        self.driver.close()
        self.driver.quit()