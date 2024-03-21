from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
#############################################################
# Selenium modify(OOP) test verifying user login and logout functionality.
# Author: PatrikS
#############################################################
def wait_time():
    time.sleep(2)

class TestWeb:
    driver = webdriver.Chrome()

    def test_setup(self, webpage):
        self.driver.get(webpage)
        self.driver.maximize_window()
        print("The test is started")
        assert "Swag" in self.driver.title, "Error: Bad webpage"
        wait_time()
        print("Page title is: " + self.driver.title)
        print("Page Url is: " + self.driver.current_url)
        wait_time()

    def test_teardown(self):
        print("The test is done")
        self.driver.close()
        self.driver.quit()    

    def test_login_in(self, login_name, password):
        element_user_name = self.driver.find_element(By.ID, "user-name")
        element_user_name.send_keys(login_name)
        element_password = self.driver.find_element(By.XPATH, '//*[@id="password"]')
        element_password.send_keys(password)
        submit_button = self.driver.find_element(By.CLASS_NAME, "submit-button")
        submit_button.click()
        wait_time()
        assert "Products" in self.driver.page_source, "Error: User is not logged in."
        if "Products" in self.driver.page_source:
            print("User is logged in.")

    def test_log_out(self):
        self.driver.refresh()
        button_menu = WebDriverWait(self.driver, 5).until(
        EC.visibility_of_element_located((By.ID, "react-burger-menu-btn")))
        button_menu.send_keys(Keys.ENTER)
        wait_time()
        element_logout = self.driver.find_element(By.ID, "logout_sidebar_link")
        element_logout.send_keys(Keys.ENTER)
        wait_time()
        if "login_credentials" in self.driver.page_source:
            print("User is logged out and is on the home page.")


web_page = TestWeb()
web_page.test_setup("https://www.saucedemo.com/")
web_page.test_login_in("standard_user","secret_sauce")
web_page.test_log_out()
web_page.test_teardown()





    


























