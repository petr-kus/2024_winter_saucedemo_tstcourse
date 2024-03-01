

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time
driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
time.sleep(3)
driver.find_element(By.ID,"user-name").send_keys("standard_user")
time.sleep(3)
driver.find_element(By.ID,"password").send_keys("secret_sauce")
time.sleep(3)
driver.find_element(By.ID,"login-button").click()
time.sleep(3)
driver.close()
driver.quit()