from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import pytest

#standartni python logging
import logging

#LOAD PAGE OBJECTS
from PageObjects.LoginPage import LoginPage
from PageObjects.Menu import Menu
#from PageObjects.Browser import Browser

def slowdown():
    sleep_time = 0.5
    if sleep_time > 0:
        logging.debug(f"slowdown and sleep {sleep_time}s to be visible during test development")
        time.sleep(sleep_time)

#OLD FIXTURES
"""
@pytest.fixture
def webpage():
    return "https://www.saucedemo.com/"

@pytest.fixture
def credentials():
    return {"password"   : "secret_sauce", "login_name" : "standart_user"}
"""

# Used constrution wit global variable and autouse=True 
# Why? -  I don't have to pass it now as fixture/object to each test...
@pytest.fixture(autouse=True, scope="session")
def Browser():
    global browser
    logging.debug(f"Starting browser chrome...")
    browser = webdriver.Chrome()
    logging.info(f"Browser started")
    yield browser
    logging.debug(f"Ending browser chrome...")
    browser.close()
    browser.quit()
    logging.info(f"Browser closed")

@pytest.fixture()
def login_page():
    login_page = "https://www.saucedemo.com/"
    logging.debug(f"Going to login page '{login_page}'")
    browser.get(login_page)
    logging.info(f"Login page '{login_page}' loaded already.")
    yield
    current_page = browser.current_url
    try:
        logging.debug(f"Going make user logoff via page menu from page '{current_page}'")
        menu = Menu(browser)
        menu.logout()
        logging.info(f"Logoff from '{current_page}' already done.")
    except:
        logging.warn(f"The page '{current_page}' was not logged in!")

class TestWebPage:

    test_page = "https://www.saucedemo.com/"
    test_page_inventory = "https://www.saucedemo.com/inventory.html"
    login_error_box = (By.XPATH,"//h3[@data-test='error']")

    @pytest.mark.parametrize("loginame, password", 
                            [("standard_user", "secret_sauce"), 
                            ("problem_user", "secret_sauce"), 
                            ("performance_glitch_user", "secret_sauce"), 
                            ("error_user", "secret_sauce"), 
                            ("visual_user", "secret_sauce")])
    def test_Successful_Login_and_Logout(self, loginame, password):
        """ This is testing successful login and logout to the page"""

        loginPage = LoginPage(browser)
        menu = Menu(browser)

        #DIFFERENT SOLUTION - possible add drver also to Page Object Model
        #browser = Browser(driver)
        #browser.go_to_page(test_page)

        browser.get(self.test_page)
        slowdown()
        loginPage.login(loginame, password)
        slowdown()
        assert "inventory" in browser.current_url
        slowdown()
        menu.logout()
        assert self.test_page == browser.current_url
        browser.get(self.test_page_inventory)
        assert self.test_page == browser.current_url
        assert browser.find_element(*self.login_error_box)

        #TODO: passing also for performance glitch user - shoudl not - have to be added verifictaion for performance

    @pytest.mark.parametrize("loginame, password", [("locked_out_user", "secret_sauce")])
    def test_Unsuccessful_Login(self, loginame, password):
        """ This is testing unsuccessful login to the page"""

        loginPage = LoginPage(browser)
        browser.get(self.test_page)
        slowdown()
        loginPage.login(loginame, password)
        slowdown()
        assert "inventory" not in browser.current_url
        assert browser.find_element(*self.login_error_box)

    #Approach with usage fixture nad yield for teardown (logout)
    @pytest.mark.parametrize("loginame, password", 
                            [("standard_user", "secret_sauce"), 
                            ("problem_user", "secret_sauce"), 
                            ("performance_glitch_user", "secret_sauce"), 
                            ("error_user", "secret_sauce"), 
                            ("visual_user", "secret_sauce")])
    def test_Successful_Login(self, login_page, loginame, password):
        """ This is testing successful login to the page"""
        loginPage = LoginPage(browser)
        slowdown()
        loginPage.login(loginame, password)
        slowdown()
        assert "inventory" in browser.current_url