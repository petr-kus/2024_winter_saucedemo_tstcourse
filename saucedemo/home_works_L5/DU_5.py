from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

def wait_time():
    time.sleep(3)

class TestWebPage():
    driver = webdriver.Chrome()
    def __init__(self,page):
        self.page_start(page)

    def page_start(self, webpage):
        try:
            self.driver.get(webpage)
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.ID, "user-name")))
        except Exception as e:
            print("An error occurred while loading the page:", e)

    def teardown(self):
        try:
            self.driver.close()
            self.driver.quit()
        except Exception as e:
            print("An error occurred while closing the browser:", e)

    def test_login(self, login_name, password):
        try:
            self.driver.find_element(By.ID,"user-name").send_keys(login_name)
            wait_time()
            self.driver.find_element(By.ID,"password").send_keys(password)
            wait_time()
            self.driver.find_element(login_button).click()
            wait_time()
        except Exception as e:
            print("An error occurred while logging in:", e)

    def test_add_to_cart(self):
        try:
            self.driver.find_element(By.ID,"item_4_title_link").click()
            wait_time()
            self.driver.find_element(By.ID,"add-to-cart-sauce-labs-backpack").click()
            wait_time()
            assert "1" == self.driver.find_element(By.CLASS_NAME,"shopping_cart_badge").text, "nebylo pridano do kosiku"
            print("INFO - prosel nakup")
        except Exception as e:
            print("ERROR - An error occurred while adding to cart:", e)

    def test_checkout(self):
        try:
            self.driver.find_element(By.ID,"shopping_cart_container").click()
            wait_time()
            self.driver.find_element(By.ID,"checkout").click()
            wait_time()
            self.driver.find_element(By.ID,"first-name").send_keys("Chandler")
            wait_time()
            self.driver.find_element(By.ID,"last-name").send_keys("Bing")
            wait_time()
            self.driver.find_element(By.ID,"postal-code").send_keys("70030")
            wait_time()
            self.driver.find_element(By.ID,"continue").click()
            wait_time()
            self.driver.find_element(By.ID,"finish").click()
            wait_time()
            self.driver.find_element(By.ID,"back-to-products").click()
            wait_time()
        except Exception as e:
            print("An error occurred while checking out:", e)

    def test_footerlink(self):
        try:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            wait_time()
            self.driver.find_element(By.ID, "page_wrapper").find_element(By.TAG_NAME, "footer").find_element(By.TAG_NAME, "ul").find_element(By.TAG_NAME, "li").find_element(By.TAG_NAME, "a").click()
            wait_time()
            self.driver.switch_to.window(self.driver.window_handles[0])
            wait_time()
        except Exception as e:
            print("An error occurred while clicking on footer link:", e)

    def test_logout(self):
        try:
            self.driver.find_element(By.ID, "react-burger-menu-btn").click()
            wait_time()
            self.driver.find_element(By.ID, "logout_sidebar_link").click()
            wait_time()
        except Exception as e:
            print("An error occurred while logging out:", e)

web_page = TestWebPage("https://www.saucedemo.com/")
web_page.test_login("standard_user","secret_sauce")
web_page.test_add_to_cart()
web_page.test_checkout()
web_page.test_footerlink()
web_page.test_logout()
web_page.teardown()

"""
Tak feedback k tomu funkcnimu.

Prvne k strukture (coz byl ukol):
- trida je dobry koncept i to tve zamyslene obecnejsi rozdeleni na veci co operuji s driverem a obecnyma vecma a na veci co jsou primo testy...
- naming metod... jeste se da posunout. page_start - by mohl byt treba go_to, test_teardown() urcite jen teardown (nejedna se o test), TestWebPage - tezko rict... mozna Test Page... jen Page?, TestWebPage ale neni spatne! wait_time by mohl byt neco jako artifial_slow_down ... nebo jen slow_down() ... zkratka co nejvic to pojmenovavat jasne a presne co to dela... . add_to_cart() - add_item_to_cart ...

- trida stranek muze obsahovat uz rovnou parametr, ktera stranka bude zakladana
aby jsi nemusel psat tyhle dva radky

web_page = TestWebPage()
web_page.page_start("https://www.saucedemo.com/")

ale jen
web_page= TestWebPage("https://www.saucedemo.com/") => vyrecnejsi a jasne (zde TestWebPage je kransy nazev!)
- zamyslel bych se jak oddelit identifikatory od kodu / zda je tam nechat. Soucasne reseni neni pro nas konkretni test spatne. ale mohlo by klidne nekde navrchu ci v jinem souboru byt pouzite preneseni do promenych

napr.
menu_button = "react-burger-menu-btn"
nebo jde zajit jeste dal
menu_button = (By.ID, "react-burger-menu-btn")

pak to vypada takto
menu_button = (By.ID, "react-burger-menu-btn")
self.driver.find_element(menu_button).click()

to je hezky pristup co zprehledni test a oddeli logiku od identifikatoru prvku... a zlepsi maintanance.

K obsahu/provedeni testu:
- chybi jakykoli záznam co bylo testované a prošlo (v tomto druhu jde doplnit logovaci funkci do souboru, nebo print do konzole?)
- libi se mi konstrukce try/except s konkretnim vypisem chyby ktera aspon castecne rekne co s estalo (muze byt jasnej a lip formatovana... napr. velke ERROR - an error occured during...", barveni, napsana obecna funkce na print message/logu atp.)
- muze se tam zapracovat na Expkicit/Implicit cekani
- silne tam postradam overovaci veci. Spolehas jen na to ze se raisne exceptna, ale na tech konkretnich stranakch nic neoverujes. Napriklad, jak overis ze se skutecne porvedl logout? To by tvuj test vubec neodhalil! - hlavne proto, ze je to posledni step!
"""