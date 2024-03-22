from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

#1.	Otevřete stránku www.saucedemo.com
driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
time.sleep(1)

#2.	Přihlaste se s uživatelským jménem standar_user a heslem secret_sauce
driver.find_element(By.ID,"user-name").send_keys("standard_user")
time.sleep(1)
driver.find_element(By.ID,"password").send_keys("secret_sauce")
time.sleep(1)
driver.find_element(By.ID,"login-button").click()
time.sleep(1)

#3.	Ověřte, že se zobrazí stránka s produkty. Jde zautomatizovat?

#4.	Vyberte produkt a přidejte ho do košíku
product_name = driver.find_element(By.ID,"add-to-cart-sauce-labs-backpack").click() 
time.sleep(1)

#5.	Klikněte na ikonku košíku
driver.find_element(By.ID,"shopping_cart_container").click()
time.sleep(1)


#6.	Klikněte na checkout nebo na continue shopping
driver.find_element(By.ID,"continue-shopping").click() or driver.find_element(By.ID,"checkout").click()

driver.close()
driver.quit()