import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def page(OPTIONS_):
    driver_options = webdriver.ChromeOptions()
    driver_options.page_load_strategy = "normal"
    for opt in OPTIONS_:
        driver_options.add_argument(opt)
    driver = webdriver.Chrome(options=driver_options)
    driver.implicitly_wait(2)
    yield driver
    driver.quit()

def open_page(page, url):
    page.get(url)

def select_element(page, selector, id):
    return page.find_element(selector, id)

def send_keys(input, keys):
    input.send_keys(keys)

def click_login(page):
    select_element(page, By.ID, "login-button").click()