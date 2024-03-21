from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
time.sleep(3)
#Verifying that users can log in to the website using valid credentials.
    #1. Enter username "standard_user"
driver.find_element(By.ID,"user-name").send_keys("standard_user")
time.sleep(3)
    #2.Enter password "secret_sauce"
driver.find_element(By.ID,"password").send_keys("secret_sauce")
time.sleep(3)
    #2.Click on the "Login" button.
driver.find_element(By.ID,"login-button").click()
time.sleep(3)

#This step test the functionality of adding product to the shopping cart
    #1. Click on any product displayed on the homepage.
product_detail_link = driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[1]/a/div").click()
time.sleep(3)
    #2. Click on the "Add to Cart" button.
driver.find_element(By.ID,"add-to-cart-sauce-labs-backpack").click()
time.sleep(3)

#Ensuring that users can review the contents of their shopping cart and proceed to checkout.
    #1. Go to cart by clicking on the cart icon in the top right corner.
driver.find_element(By.ID,"shopping_cart_container").click()
time.sleep(3)
    #2.Click on the "checkout" button.
driver.find_element(By.ID,"checkout").click()
time.sleep(3)

#Adding First name
driver.find_element(By.XPATH,"/html/body/div/div/div/div[2]/div/form/div[1]/div[1]/input").send_keys("Lukáš")
time.sleep(3)
#Adding Last Name
driver.find_element(By.XPATH,"//*[@id='last-name']").send_keys("Skulina")
time.sleep(3)
#Adding Postal Code
driver.find_element(By.ID,"postal-code").send_keys("70030")
time.sleep(3)
#Click on continue
driver.find_element(By.ID,"continue").click()
time.sleep(3)
#Finishing an order
driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div/div[2]/div[9]/button[2]").click()
time.sleep(3)
#Back to HomePage
driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/button").click()
time.sleep(3)

#This step ensures that footer links are functioning correctly and lead to the expected pages.
    #1. Scroll down to the botom of the homepage.
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(3)
    #2.Clinck on each footer link to verify they lead to the correct pages. → Twitter
driver.find_element(By.XPATH, "/html/body/div/div/footer/ul/li[1]/a").click()
time.sleep(5)
driver.switch_to.window(driver.window_handles[0])
time.sleep(5)

#This step confirms that users can log out of their accounts.
    #Click on the three commas in the top left corner
driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div[1]/div[1]/div/div[1]/div/button").click()
time.sleep(3)
    #Select "Logout"
driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div[1]/div[1]/div/div[2]/div[1]/nav/a[3]").click()
time.sleep(3)

driver.close()
driver.quit()