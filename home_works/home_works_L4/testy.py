from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")



time.sleep(2)
user_name = driver.find_element(By.ID, "user-name").send_keys("standard_user")
time.sleep(2)
password = driver.find_element(By.ID, "password").send_keys("secret_sauce")
time.sleep(2)
login_button = driver.find_element(By.ID, "login-button")
login_button.click()
time.sleep(3)


driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
time.sleep(1)
driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()
time.sleep(1)
driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
time.sleep(1)
driver.find_element(By.ID, "add-to-cart-sauce-labs-fleece-jacket").click()
time.sleep(1)
driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()
time.sleep(1)
driver.find_element(By.ID, "add-to-cart-test.allthethings()-t-shirt-(red)").click()
time.sleep(3)

driver.find_element(By.ID, "shopping_cart_container").click()
time.sleep(3)

driver.find_element(By.ID, "remove-sauce-labs-backpack").click()
time.sleep(1)
driver.find_element(By.ID, "remove-sauce-labs-bike-light").click()
time.sleep(1)
driver.find_element(By.ID, "remove-sauce-labs-bolt-t-shirt").click()
time.sleep(1)
driver.find_element(By.ID, "remove-sauce-labs-fleece-jacket").click()
time.sleep(1)
driver.find_element(By.ID, "remove-sauce-labs-onesie").click()
time.sleep(1)
driver.find_element(By.ID, "remove-test.allthethings()-t-shirt-(red)").click()
time.sleep(3)

driver.find_element(By.ID, "react-burger-menu-btn").click()
time.sleep(1)
driver.find_element(By.ID, "inventory_sidebar_link").click()
time.sleep(3)

driver.find_element(By.ID, "react-burger-menu-btn").click()
time.sleep(1)
driver.find_element(By.ID, "logout_sidebar_link").click()
time.sleep(5)

driver.close
driver.quit