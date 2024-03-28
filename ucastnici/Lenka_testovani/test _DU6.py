import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="session")
def driver():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com")
    yield driver
    driver.quit()

@pytest.mark.parametrize("username,password", [
    ("standard_user", "secret_sauce"),
    ("locked_out_user", "secret_sauce"),
])
def test_login(driver, username, password):
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "user-name"))).send_keys(username)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "password"))).send_keys(password + Keys.RETURN)
    assert "Products" in WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "title"))).text



