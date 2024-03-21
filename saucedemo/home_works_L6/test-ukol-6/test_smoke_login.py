import json
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from utils import log, timer
from funcs import *


OPTIONS = ["--start-maximized", "--headless=new"]
DATA_TABLE = "data_table.json"
DEFAULT_URL = "https://www.saucedemo.com/"
EXPECTED_URL = "https://www.saucedemo.com/inventory.html"
DEFAULT_TITLE = "Swag Labs"


with open(DATA_TABLE, "r") as file:
    DATA_TABLE = json.load(file)


@pytest.mark.autotest
@pytest.mark.parametrize("OPTIONS_", [OPTIONS])
@pytest.mark.parametrize("DATA_TABLE_", DATA_TABLE)
class TestLogin:
    @timer
    def test_smoke_login(self, page: webdriver.Chrome, DATA_TABLE_):
        try:
            open_page(page, DEFAULT_URL)
            assert page.title == DEFAULT_TITLE and page.current_url == DEFAULT_URL
            log.info(f"PASSED - go to url: '{DEFAULT_URL}'")
        
            username = select_element(page, By.ID, "user-name")
            send_keys(username, DATA_TABLE_["name"])
            log.info(f"PASSED - select 'user-name' form and enter: '{DATA_TABLE_['name']}'")

            password = select_element(page, By.ID, "password")
            send_keys(password, DATA_TABLE_["password"])
            log.info(f"PASSED - select 'password' form and enter: '{DATA_TABLE_['password']}'")

            click_login(page)
            log.info(f"PASSED - select 'login-button' and click it")

            if DATA_TABLE_["expected"] == True:
                assert page.title == DEFAULT_TITLE and page.current_url == EXPECTED_URL

            elif DATA_TABLE_["expected"] == False:
                assert page.title == DEFAULT_TITLE and page.current_url == DEFAULT_URL
            log.info(f"PASSED - verify login status")
            
        except Exception as e:
            log.error(f"FAILED - {str(e)[:30]} ...")
            raise