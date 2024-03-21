from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
def my_wait():
    time.sleep(1)
def test_setup(webpage):
    driver = webdriver.Chrome()
    driver.get(webpage)
    my_wait()
    return driver
def test_teardown(driver):
    driver.close()
    driver.quit()
def test_login(driver,login_name,password):
    """ This is testing login to the page"""
    driver.find_element(By.ID,"user-name").send_keys(login_name)
    my_wait()
    driver.find_element(By.ID,"password").send_keys(password)
    my_wait()
    driver.find_element(By.ID,"login-button").click()
    my_wait()
    driver.find_element(By.ID,"item_4_title_link").click()
    my_wait()
    driver.find_element(By.ID,"add-to-cart-sauce-labs-fleece-jacket").click()
driver = test_setup("https://www.saucedemo.com/")
test_login(driver,"problem_user","secret_sauce")
test_teardown(driver)