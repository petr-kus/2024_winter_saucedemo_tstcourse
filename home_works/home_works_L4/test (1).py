from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

# Nastavení instance WebDriveru
driver = webdriver.Chrome()

# Otevření webu Sauce Demo
driver.get("https://www.saucedemo.com")

# Vyhledání elementů pro přihlašovací jméno a heslo
username_field = driver.find_element(By.ID, "user-name")
password_field = driver.find_element(By.ID, "password")

# Zadání uživatelského jména a hesla
username_field.send_keys("standard_user")
password_field.send_keys("secret_sauce")

# Odeslání formuláře
password_field.send_keys(Keys.RETURN)

# Kontrola úspěšného přihlášení
try:
    products_label = driver.find_element(By.CLASS_NAME, "product_label")
    assert "Products" in products_label.text
    print("Přihlášení úspěšné - Smoke Test prošel.")
except NoSuchElementException:
    print("Přihlášení selhalo - Smoke Test neúspěšný.")

# Ukončení instance WebDriveru
driver.quit()


