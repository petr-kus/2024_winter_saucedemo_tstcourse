import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils import Log, wait


default_url = "https://www.saucedemo.com/"

test_data = [
    # (name, password, expected)
    ("standard_user", "secret_sauce", "https://www.saucedemo.com/inventory.html"),
    ("locked_out_user", "secret_sauce", "Epic sadface: Sorry, this user has been locked out."),
    ("standard_user", "incorrect_password", "Epic sadface: Username and password do not match any user in this service"),
    ("", "", ""), # Mock data expected to fail
    ("standard_user", "", "Epic sadface: Password is required"),
    ("", "", "Epic sadface: Username is required"),
    ("", "secret_sauce", "Epic sadface: Username is required"),
    ]


@pytest.fixture
def page():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    options.add_argument("start-maximized")
    options.add_argument("--headless=new")
    driver = webdriver.Chrome(options=options)
    yield driver


class TestSauceDemo(Log):
    @pytest.mark.parametrize("name, password, expected", test_data)
    def test_login_functionality(
        self, page: webdriver.Chrome,
        name, password, expected):

        try:
            # [TEST STEP 1]
            wait()
            self.log_pass()

            # [TEST STEP 2]
            page.get(default_url)
            wait()
            self.log_pass()

            # [TEST STEP 3]
            assert page.current_url == default_url
            wait()
            self.log_pass()

            # [TEST STEP 4]
            name_form = page.find_element(By.ID, "user-name")
            name_form.send_keys(name)
            wait()

            password_form = page.find_element(By.ID, "password")
            password_form.send_keys(password)
            wait()

            page.find_element(By.ID, "login-button").click()

            if page.current_url == default_url:
                error_button = page.find_element(By.CLASS_NAME, "error-message-container.error")
                assert error_button.text == expected
            else:
                assert page.current_url == expected
            wait()
            self.log_pass()
      
            # [TEST STEP 5]
            page.quit()
            wait()
            self.log_pass()

        except Exception as err:
            page.quit()
            wait()
            self.log_fail()
            raise(err)