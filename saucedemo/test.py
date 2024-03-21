from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from PageObjects.LoginPage import LoginPage
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
        LoginPage = LoginPage(self.driver)
        LoginPage.login(loginame,password)
    
    def test_teardown(self):
        self.driver.close()
        self.driver.quit()