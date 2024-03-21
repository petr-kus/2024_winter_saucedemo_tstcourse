import pytest
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils import Log


default_url = "https://www.saucedemo.com/"

test_data = [
    # (name, password, expected)
    ("standard_user", "secret_sauce", "https://www.saucedemo.com/inventory.html"),
    ("locked_out_user", "secret_sauce", "Epic sadface: Sorry, this user has been locked out."),
    ("performance_glitch_user", "secret_sauce", "https://www.saucedemo.com/inventory.html"), # Performace glitch user should fail in test step 3.4 but does not!
    ("standard_user", "incorrect_password", "Epic sadface: Username and password do not match any user in this service"),
    ("mock_user", "", ""), # Mock data expected to fail it test step 5.4!
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
            wait = WebDriverWait(page, 2)
            self.log_pass()

            # [TEST STEP 2]
            page.get(default_url)
            wait.until(EC.presence_of_element_located((By.TAG_NAME, "html")))
            self.log_pass()

            # [TEST STEP 3]
            assert page.current_url == default_url
            self.log_pass()

            # [TEST STEP 4]
            name_form = wait.until(EC.element_to_be_clickable((By.ID, "user-name")))
            name_form.send_keys(name)

            password_form = wait.until(EC.element_to_be_clickable((By.ID, "password")))
            password_form.send_keys(password)

            wait.until(EC.element_to_be_clickable((By.ID, "login-button"))).click()

            try:
                error_button = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "error-message-container.error")))
                assert error_button.text == expected

            except TimeoutException:
                error_button = wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, "error-message-container.error")))
                assert page.current_url == expected

            self.log_pass()
      
            # [TEST STEP 5]
            page.quit()
            self.log_pass()

        except Exception as err:
            page.quit()
            self.log_fail()
            raise(err)