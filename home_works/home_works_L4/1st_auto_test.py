from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
#############################################################
# Selenium test verifying user login and logout functionality.
# Author: 
#############################################################
# Initialize the Chrome WebDriver
driver = webdriver.Chrome()

# Navigate to the website
driver.get("https://www.saucedemo.com/")

# Maximize the browser window
driver.maximize_window()

# Verify if the title of the page contains the string "Swag"
assert "Swag" in driver.title
time.sleep(1)

# Print the current title and URL of the page
print("Page title is: " + driver.title)
print("Page Url is: " + driver.current_url)
time.sleep(1)

# Find the element with ID "user-name" 
element_user_name = driver.find_element(By.ID, "user-name")
    
# Send the keys "standard_user" to the username field
element_user_name.send_keys("standard_user")

# Find the element using CSS selector for the password field
element_password = driver.find_element(By.CSS_SELECTOR, '[data-test="password"]')

# Send the keys "secret_sauce" to the password field
element_password.send_keys("secret_sauce")

# Find the button with class "submit-button" and click on it
submit_button = driver.find_element(By.CLASS_NAME, "submit-button")
submit_button.click()
time.sleep(2)

# Verify if the string "Products" is not present on the page
assert "Products" in driver.page_source, "Error: User is not logged in."

# If the string "Products" is present on the page, print that the user is logged in
if "Products" in driver.page_source:
    print("User is logged in.")
time.sleep(2) 
# Refresh the page after login
driver.refresh()

# Find the button with ID "react-burger-menu-btn" and wait until it becomes visible and press the ENTER key
button_menu = WebDriverWait(driver, 5).until(
    EC.visibility_of_element_located((By.ID, "react-burger-menu-btn")))
button_menu.send_keys(Keys.ENTER)
time.sleep(2)

# Find the element with ID "logout_sidebar_link" and press the ENTER key
element_logout = driver.find_element(By.ID, "logout_sidebar_link")
element_logout.send_keys(Keys.ENTER)
time.sleep(2)

# If the string "login_credentials" is present on the page, print that the user is logged out and is on the home page
if "login_credentials" in driver.page_source:
    print("User is logged out and is on the home page.")

# Close the browser
driver.close()
