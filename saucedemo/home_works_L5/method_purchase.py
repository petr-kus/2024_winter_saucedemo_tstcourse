# This script is going to be testing product search, choose,
# add to basket, remove from basket and return back to the homepage.
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from pages.porduct_list import product_list
import time

def wait():
    time.sleep(2)

def page_load(url, id_cookies):
    driver = webdriver.Chrome()
    driver.get(url)
    driver.maximize_window()
    cookie = driver.find_element(By.ID, id_cookies).click()
    wait()
    return driver

# product searching
def find_product():
    write = driver.find_element(By.CLASS_NAME, "c-search__input")
    write.send_keys("Sluchátka Samsung")
    write.send_keys(Keys.RETURN)    
    wait()

# check-box click with particular price
def price_range(id_range):
    range = driver.find_element(By.ID, id_range)
    action = ActionChains(driver)
    action.click(range)
    action.perform()
    wait()

# products view in grid
def product_view(class_view):
    grid = driver.find_element(By.CLASS_NAME, class_view)
    action = ActionChains(driver)
    action.reset_actions()
    action.click(grid) 
    action.perform()
    wait()
    
# product choose
def product_click(class_product):
    confirm = driver.find_element(By.CLASS_NAME, class_product)
    action = ActionChains(driver)
    action.reset_actions()
    action.click(confirm) 
    action.perform()
    wait()
    
# buy by Heureka
def buy(class_buy):
    buy_button = driver.find_element(By.CLASS_NAME, class_buy)
    action = ActionChains(driver)
    action.reset_actions()
    action.click(buy_button)
    action.perform()
    wait()

def buy_confirmation(class_buy_confirmation):
    confirmation_button = driver.find_element(By.CLASS_NAME, class_buy_confirmation)
    action = ActionChains(driver)
    action.reset_actions()
    action.click(confirmation_button)
    action.perform()
    wait()

# going to basket
def basket(class_basket):
    basket_confirmation = driver.find_element(By.CLASS_NAME, class_basket)
    action = ActionChains(driver)
    action.reset_actions()
    action.click(basket_confirmation)
    action.perform()
    wait()

def empty_basket(class_empty):
    empty_button = driver.find_element(By.CLASS_NAME, class_empty)
    action = ActionChains(driver)
    action.reset_actions()
    action.click(empty_button)
    action.perform()
    wait()

def confirm_empty_basket(class_empty_basket):
    empty_confirm = driver.find_element(By.CLASS_NAME, class_empty_basket)
    action = ActionChains(driver)
    action.reset_actions()
    action.click(empty_confirm)
    action.perform()
    wait()

def heureka_homepage(class_heureka):
    homepage = driver.find_element(By.CLASS_NAME, class_heureka)
    action = ActionChains(driver)
    action.reset_actions()
    action.click(homepage)
    action.perform()
    wait()
    driver.quit()    
    
driver = page_load("https://www.heureka.cz", "didomi-notice-agree-button")
find_product()
price_range("price-4")
product_view("c-preferred-layout__label")
product_click("c-product__link")
buy("c-top-offer__buy-text")
buy_confirmation("c-variant__button")
basket("c-cart-confirm__button--cart")
empty_basket("e-icon--md")
confirm_empty_basket("e-button--primary")
heureka_homepage("l-header__logo")

"""
Ahoj,

krasne. heureka :-). Jsem rad ze jsi si to zkusil nad necim "beznym".
Neni uplne dobre testovat nad necim co nemas dohodnute :-). Nekdo to muze vzit jako utok/nepovolene uzitit... .
Jen upozorneni... .

feedback k strukture (to byl ukol):

- funkce nejsou spatne. ale vyuziti "." (teckove konvence) by bylo o dost lepsi. Tedy prepsat to do objektu doporucuji. Priklad:

page.test_login("user", "password")

Zvysuje citelnost a udrzitelnost a lip se tam pak aplikuji veci na cele objekty.
Dokonce page by mohla mit jemeno te stranky... musel by jsi vytvorit vice objektu...

porduct_list.select_price_group(4)
cart.confirm_buy()

- Naming Dela Nejvic!
wait_time by mohl byt neco jako artifial_slow_down ... nebo jen slow_down() ... zkratka co nejvic to pojmenovavat jasne a presne co to dela... .

page_load - go_to_page?
find_product(class_input) - class_input bych pojmenoval nak lip a asi byh to pojmenoval ... product_class pokud trvas na te clase.
Ten click na grid dle me klikne proste na prvni polozku nebo se nak nahodne vybere? Pokud se nevybere nahodne... asi bych tomu nerikal grid... .

Podivej -

driver = page_load("https://www.heureka.cz", "didomi-notice-agree-button")
find_product("c-search__input")
price_range("price-4")
product_view("c-preferred-layout__label")
product_click("c-product__link")
buy("c-top-offer__buy-text")
buy_confirmation("c-variant__button")
basket("c-cart-confirm__button--cart")
empty_basket("e-icon--md")
confirm_empty_basket("e-button--primary")
heureka_homepage("l-header__logo")

Tohle by melo byt maximalne srozumitelny...

ad 1) ty ID/classy a tak dale... nekam schovat!
bud za dobre pojmenovanou promenou a nebo dovnitr tech funkci...

napr. nekde nahore muze byt promena
basket_confirmation_button = (By.CLASS_NAME, "c-cart-confirm__button--cart")
a vevnitr funkce uz jen
basket_confirmation = driver.find_element(basket_confirmation_button)

ad 2) Ty funkce to je mor. Pokud funkce zachovat snazit se o vice popisne pojmenovani jeste.
a treba i neco sloucit.

empty_basket("e-icon--md")
confirm_empty_basket("e-button--primary")
napr.
empty_basket_and_confirm()

by stacilo...

feedback k valstnimu testu:
- moc nechapu proc je tam
cookie = driver.find_element(By.ID, id_cookies).click()
neprijde mi ze by slo o overeni selhanim... .

- pouziti action chains - to je hezke. Sam jsem to musel nastudovat. Libi se mi ze hledas cesty jak to udelat lip.
Pochopil jsme ze to prinasi sirsi moznosti pro delani scenaru. Proc ne... . :-)

- silne tam postradam overovaci veci. Spolehas jen na to ze se raisne exceptna v dalsim kroku (to muze byt matouci kdyz to vyhodi vyjimku) , ale na tech konkretnich stranakch nic neoverujes. Napriklad, jak overis ze se skutecne porvedl heureka_homepage? To by tvuj test vubec neodhalil! - hlavne proto, ze je to posledni step!

- chybi i jakykoli záznam co bylo testované a prošlo (v tomto druhu jde doplnit logovaci funkci do souboru, nebo print do konzole?)
"""