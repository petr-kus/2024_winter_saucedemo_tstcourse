from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

import pytest

#############################################################
# Pytest verifying user login and logout functionality.
# Author: Patrik Sova
#############################################################

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.mark.parametrize("login_name, password", [("standard_user", "secret_sauce")])
def test_login_and_logout(browser, login_name, password):
    browser.get("https://www.saucedemo.com/")
    browser.maximize_window()
    assert "Swag" in browser.title, "Error: Bad webpage"

    element_user_name = browser.find_element(By.ID, "user-name")
    element_user_name.send_keys(login_name)
    element_password = browser.find_element(By.XPATH, '//*[@id="password"]')
    element_password.send_keys(password)
    submit_button = browser.find_element(By.CLASS_NAME, "submit-button")
    submit_button.click()

    WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "inventory_list")))
    assert "Products" in browser.page_source, "Error: User is not logged in."
    print("User is logged in.")

    browser.refresh()
    button_menu = WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.ID, "react-burger-menu-btn")))
    button_menu.click()

    WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.ID, "logout_sidebar_link"))).click()

    WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.ID, "login_credentials")))
    assert "login_credentials" in browser.page_source, "Error: User is not logged out."
    print("User is logged out and is on the home page.")
