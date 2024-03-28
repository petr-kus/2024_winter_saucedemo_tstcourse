from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest


products =["sauce-labs-backpack", "sauce-labs-bike-light", "sauce-labs-bolt-t-shirt",
            "sauce-labs-fleece-jacket", "sauce-labs-onesie", "test.allthethings()-t-shirt-(red)" ]

@pytest.fixture
def webpage():
        return "https://www.saucedemo.com/"
    
@pytest.fixture
def credentials():
    credentials = {"login" : "standard_user", "password" : "secret_sauce"}
    return credentials
    
    
@pytest.fixture
def product_list():
    return products

class TestWebPageChrome():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
        
    def test_webpage(self, webpage):
         self.driver.get(webpage)
    
       
    def test_sign_in(self, credentials):
        try:
            login = credentials["login"]
            password = credentials["password"]
            self.driver.find_element(By.ID, "user-name").send_keys(credentials["login"])
            self.driver.find_element(By.ID, "password").send_keys(credentials["password"])
            assert login == self.driver.find_element(By.ID, "user-name").get_attribute("value")
            assert password == self.driver.find_element(By.ID, "password").get_attribute("value")
            print("Text entered succesfully!")
        except Exception as e:
            print("Error: Text not in text field")
        
    def test_log_in(self):
        try:
            login_button = self.wait.until(EC.element_to_be_clickable((By.ID, "login-button")))
            login_button.click()
            assert "Products" == self.driver.find_element(By.CLASS_NAME,"title").text
            print("Logged in succesfully")
        except Exception as e:
            print("Error occured during logging in", e), 
        

    def test_add_to_cart(self, product_list):
            try:
                cart_badge = 0
                for product in product_list:
                    add_to_card_button = self.wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-"+product)))
                    add_to_card_button.click()
                    cart_badge += 1
                assert cart_badge == int(self.driver.find_element(By.CLASS_NAME,"shopping_cart_badge").text)
                print("All items succesfully in cart")
            except Exception as e:
                print("Error occured during adding items to shopping cart", e)

    def test_shopping_cart(self):
        try:
            shopping_card_button = self.wait.until(EC.element_to_be_clickable((By.ID, "shopping_cart_container")))
            shopping_card_button.click()
            assert "Your Cart" == self.driver.find_element(By.CLASS_NAME,"title").text
            print("Succesfully redirected to shopping cart page")
        except Exception as e:
            print("Error occured during adding items to shopping cart", e)


    def test_remove_item(self, product_list):
        for product in product_list:
            remove_button = self.wait.until(EC.element_to_be_clickable((By.ID, "remove-"+product)))
            remove_button.click()
            

    def test_menu(self):
        menu_button = self.wait.until(EC.element_to_be_clickable((By.ID, "react-burger-menu-btn")))
        menu_button.click()
        inventory_link = self.wait.until(EC.element_to_be_clickable((By.ID, "inventory_sidebar_link")))
        inventory_link.click()
              
    def test_log_out(self):
        menu_button = self.wait.until(EC.element_to_be_clickable((By.ID, "react-burger-menu-btn")))
        menu_button.click()
        logout_link = self.wait.until(EC.element_to_be_clickable((By.ID, "logout_sidebar_link")))
        logout_link.click()

    def test_shutdown(self):
        self.driver.close
        self.driver.quit
