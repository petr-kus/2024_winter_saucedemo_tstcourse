from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
driver = webdriver.Chrome()
second_driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
time.sleep(5)
driver.find_element(By.ID,"user-name").send_keys("standard_user")
time.sleep(3)
driver.find_element(By.ID,"password").send_keys("secret_sauce")
time.sleep(3)
driver.find_element(By.ID,"login-button").click()
time.sleep(3)
driver.find_element(By.ID,"item_4_title_link").click()
time.sleep(3)
driver.find_element(By.ID,"back-to-products").click()
time.sleep(3)
for item_id in range(1, 10):  
    item_id_str = f"item_{item_id}_title_link"
    try:
        driver.find_element(By.ID, item_id_str).click()
        time.sleep(3)   
        driver.find_element(By.ID,"back-to-products").click()               
    except NoSuchElementException:
        print(f"Element with ID {item_id_str} not found")

second_driver.get("https://www.saucedemo.com/static/media/sauce-backpack-1200x1500.0a0b85a3.jpg")
time.sleep(3)
driver.find_element(By.ID,"react-burger-menu-btn").click()
time.sleep(3)
driver.find_element(By.ID,"react-burger-cross-btn").click()
time.sleep(20)
driver.close()
second_driver.close()
driver.quit()
second_driver.quit()