from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

class Akce:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        self.driver.get("https://www.saucedemo.com/")
        time.sleep(5)
        self.driver.find_element(By.ID, "user-name").send_keys(username)
        time.sleep(3)
        self.driver.find_element(By.ID, "password").send_keys(password)
        time.sleep(3)
        self.driver.find_element(By.ID, "login-button").click()
        time.sleep(3)

    def click_all_items(self):
        item_id = 1
        while True:
            item_id_str = f"item_{item_id}_title_link"
            if not self.driver.find_elements(By.ID, item_id_str):
                print(f"Element with ID {item_id_str} not found")
                break

            try:
                self.driver.find_element(By.ID, item_id_str).click()
                time.sleep(3)
                self.driver.find_element(By.ID, "back-to-products").click()
                item_id += 1
            except NoSuchElementException:
                print(f"Element with ID {item_id_str} not found")
                break

    def open_and_close_menu(self):
        self.driver.find_element(By.ID, "react-burger-menu-btn").click()
        time.sleep(3)
        self.driver.find_element(By.ID, "react-burger-cross-btn").click()
        time.sleep(10)

    def close_browser(self):
        self.driver.close()
        self.driver.quit()


driver = webdriver.Chrome()
web_actions = Akce(driver)

# metody triedy Webactions na testovanie
username = "standard_user"
password = "secret_sauce"
web_actions.login(username, password)
web_actions.click_all_items()
web_actions.open_and_close_menu()
web_actions.close_browser()