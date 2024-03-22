from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 

def slowdown():
    time.sleep(0.5)

class Menu:
    main_menu_button = "react-burger-menu-btn"
    logout_button = "//nav/*[text()='Logout']"

    def __init__(self, driver):
        self.driver = driver

    def logout(self):
        slowdown()
        self.driver.find_element(By.ID, self.main_menu_button).click()
        slowdown()
        WebDriverWait(self.driver,2).until(EC.visibility_of_element_located((By.XPATH,self.logout_button))).click()
        slowdown()