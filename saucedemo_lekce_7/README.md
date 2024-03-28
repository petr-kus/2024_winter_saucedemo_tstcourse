# Povšimněte si...
V kódu z lekce 7 si obzvláště povšimněte těchot konstrukcí.

## POM - Page Object Model

V souboru s testy (test.py) jsou tyto související řádky:
```python
...
from PageObjects.LoginPage import LoginPage
...
loginPage = LoginPage(browser)
...
loginPage.login(loginame, password)
...
```
.\PageObjects\LoginPage.py
```python
class LoginPage:

    password_field = (By.ID,'password')
    login_name_field = (By.ID,'user-name')
    login_button = (By.ID,'login-button')

    def __init__(self,driver):
        self.driver = driver
        
    def login(self,name,password):
        self.driver.find_element(*self.login_name_field).send_keys(name)
        self.driver.find_element(*self.password_field).send_keys(password)
        self.driver.find_element(*self.login_button).click()
```
Této konstrukci, kdy vše související se stránkou či komponentou oddělí bokem se říká Page Object Model. Jedná se o často používaný automatizační pattern.

Výhody jsou:
- snadná udržitelnost. Když něco měním, tak to měním na jednom místě a né na spoustě řádků. Třeba si představte, že se změní přístup k tlačítku z By.ID na By.XPATH a nebo se změní způsob zalogovaní - přidá se captha např.
- vše co je u sebe je pohormadě i v kodu (aneb proximity principle). Dlouho to nehledám a nemusím v kodu skákat. Rychle to chápu.
- složitý a nečitelný kod je odstíněn a schován za Page Object Model = umožňuje to budování tzv. 'Doménového Jazyka'
```python
#příklady
loginPage.login('jméno','heslo')
menu.logout()
```


- při psaní kódu mě stačí napsat 
```python
loginPage.
```
a editor mi za tečkou hned napovídá co mohu dělat (volat metody) a nebo jaké property (zde adresy prvků) mohu využít.

## Centralizace adresace, jejího způsobu a parametrizace stránek

Prostě věcí co se opakují dáváme do proměných, aby se někde přehledně nastavovali a dali se ovládat centrálně a nemuseli jsme je přepisovat na spoustě řádků.
Když toho je opravdu hodně, dají se použít i definice v externích souborech.

test.py:
```python
...
class TestWebPage:

    test_page = "https://www.saucedemo.com/"
    test_page_inventory = "https://www.saucedemo.com/inventory.html"
    login_error_box = (By.XPATH,"//h3[@data-test='error']")
    ...

    def test_Successful_Login_and_Logout(self, loginame, password):
        ...
        assert self.test_page == browser.current_url
        browser.get(self.test_page_inventory)
        assert self.test_page == browser.current_url
        assert browser.find_element(*self.login_error_box)
        ...
    
    def test_Unsuccessful_Login(self, loginame, password):
        ...
        browser.get(self.test_page)
        ...
        assert browser.find_element(*self.login_error_box)
```

Specificky si všimněte konstrukce:
```python
login_error_box = (By.XPATH,"//h3[@data-test='error']")
...
assert browser.find_element(*self.login_error_box)
```
Kde se využívá společného uložení způsobu jak najít prvek (By.ID/By.XPATH...) i s adresou u sebe v tuplu.
A pak se pomocí * (*self.login_error_box) rozbaluje jako parametry dane metody, aby se to na tom místě nemuselo psát znovu.
Toto je dobrý tríček.

## Uživateli blízký způsob adresace
Je tam použito i na jendom místě "měkké adresování" pomocí relativní XPATH, přesně dle toho co vidí uživatel na obarzovce (dle textu 'Logof' ve vyjížděcím menu).
- to testuje danou věc jako by to uživatel četl (změní se text => najde to chybu)

Menu.py:
```python
class Menu:
    ...
    logout_button = (By.XPATH,"//nav/*[text()='Logout']")
    ...

    def logout(self):
        ...
        WebDriverWait(self.driver,2).until(EC.visibility_of_element_located(self.logout_button)).click()
        ...
```

## Explicitní čekání na dynamický prvek stránky
Specificky se čeká na prvek, který nemusí být viditelný pokud stránka bude reagovat pomalu.
Prvek není vázaný na načtení celé stranky - jedná se o dynamickou věc (vyjížděcí menu po levé straně). Má zde tedy smysl použít explicitní čekání.
U většiny prvků na této stránce si vystačíme s implicitním čekáním nebo strategi načtení complete.

Menu.py:
```python
...
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
...

class Menu:
    ...
    def logout(self):
        ...
        WebDriverWait(self.driver,2).until(EC.visibility_of_element_located(self.logout_button)).click()
        ...
```

## Využití parametrizace pytestu pro data-driven test přístup/pattern
Data-Driven test - sežere data z tabulky (můžou tam být i očekávané výsledky ne jen vstupni parametry). 
A pro všechny hodnoty z dané tabulky zkusí opakovaně zapsaný scénář.
Přidání dalšího test casu zahrnuje pouze dopsaní dalšího řádku se vstupními a očekavanými výstupními daty do tabulky. 

Jedná se o další silnou vlastnost Pytestu.

test.py:
```python
class TestWebPage:

    ...

    @pytest.mark.parametrize("loginame, password", 
                            [("standard_user", "secret_sauce"), 
                            ("problem_user", "secret_sauce"), 
                            ("performance_glitch_user", "secret_sauce"), 
                            ("error_user", "secret_sauce"), 
                            ("visual_user", "secret_sauce")])
    def test_Successful_Login_and_Logout(self, loginame, password):
        """ This is testing successful login and logout to the page"""
        ...
        browser.get(self.test_page)
        ...
        loginPage.login(loginame, password)
        assert "inventory" in browser.current_url
        menu.logout()
        assert self.test_page == browser.current_url
        ...
```

Povšimněte si, že v logovacím scénáři nahoře je jak najetí na stránku, zalogovaní tak odlogovaní ('setup'/'teardown') 

Jaké z toho pak plynou výhody:
- Vstupní a výstupní bod/stav testu umožňuje rychle puštění všech kombinací za sebou. 
- Test je také tím izolovaný / atomický - je mu jedno co běželo před ním a co po něm. 
- Jsem schopni ho pustit v libovolném pořadí vuči klidně i dalším testům. 
- Je mu i jedno jak přehodím řádky v tabulce.

## Test Design ověření zalogování/odlogování

Úplně bez problémů je použito několik assertů za sebou i na různé věci. Křížově se ověřuje něco několika způsoby.

```python
    def test_Successful_Login_and_Logout(self, loginame, password):
        """ This is testing successful login and logout to the page"""
        ...

        browser.get(self.test_page)
        loginPage.login(loginame, password)
        assert "inventory" in browser.current_url
        menu.logout()
        assert self.test_page == browser.current_url

        #po odlogovaní zkusí najet na stránku s inventářem
        browser.get(self.test_page_inventory)
        #a ověří že ho to přesměruje na loginpage a na inventář se nedostane
        assert self.test_page == browser.current_url

        #a ověří že je tam zobrazená nějáká chyba v logovaní
        assert browser.find_element(*self.login_error_box)
```

V autotestu je skutečně dost často ověřeno jen to co tam napíšte.
- Tak to tam nezapomeň napsat! 
- A zkusit si, že to selže!
PS: občas tě ale i překvapí, že to přišlo na něco co jste tam nenapsal/a :-).

## Logování samotného testu pomocí python loggru a použití Caplogu (zatím v příkladu jen naznačeno - není použito všude a plně)

Při testování s PyTestem máme na výběr použít různých přístupů k logovaní:
- Caplog - funkcionalita Pytestu (asi nejlepší cesta když s logy něco chcete dělat, která nabízi přidanou funkcionalitu k standartnímu Python logování) 
- standartni python logging (dobrá cesta. Caplog je na něm samozřejmně postaven a využívá jeho k samotné akci logování.)
- napsat si vlastní logování (no, proč se s tím dřít. Už jen napsat printy je zbytečně složité)
- použít jinou externí knihovnu pro logování (Stojí za úvahu, ale aby to bylo výhodné musí to mít hodně vážený benefit)

Z toho logicky plyne, použít v kurzu cestu python logovaní v kombinaci s Caplogem. Více o tomto tématu naleznete zde:
- https://pytest-with-eric.com/fixtures/built-in/pytest-caplog/
- https://pytest-with-eric.com/pytest-best-practices/pytest-logging/#Custom-Logger-vs-Inbuilt-Logging-Module

A i některé další témata jež jsme již probrali na kurzu.

Tam též naleznete velmi dobrý teoretický popis i s praktickými příklady a vysvětlením proč použít caplog.
- dokáže rozdělit fáze pytestu (setup/terdown/test execution ...)
- dokáže oddělit logy z různých testů (ma kontext pytestu)
- můžete ho snadno použít k podmínkám a assertovaní zda něco bylo / nebylo zalogováno
- ...

test.py
```python
...
import logging
...

@pytest.fixture()
def login_page():
    login_page = "https://www.saucedemo.com/"
    logging.debug(f"Going to login page '{login_page}'")
    browser.get(login_page)
    logging.info(f"Login page '{login_page}' loaded already.")
    yield
    current_page = browser.current_url
    try:
        logging.debug(f"Going make user logoff via page menu from page '{current_page}'")
        menu = Menu(browser)
        menu.logout()
        logging.info(f"Logoff form '{current_page}' already done.")
    except:
        logging.warn(f"The page '{current_page}' was not logged in!")
```
Zde si povšimněte těchto triků:
- požívají se různé levely logovaní 
    - debug - když budeme hledat jak se to přesně a podorbně chová
    - info - základní logování ktere informuje orientačně o tom že se něco stalo
    - warn - když je něco silně podezřelého ale ještě není jasné, zda je ot problém
    - error - v tomto příkladě nepoužit, ale dost často je právě součástí except částí kódu. Jednoznačně dokážeme určit že jde o chybové chování.
- do logování vstupují i parametry a stavy login_page, current_page, právě proto, aby nám logování něco realně řeklo.
- používá se f konvence se správným pojmenováním proměných, aby to bylo celé krásně čítelné i z kódu a vlastně je to využito místo komentářů. Ale tyto komentáře vytupují i vtestovacích výsledcích (má to tedy dvojí účel). 
```python
f"Login page '{login_page}' loaded already."
```
- je to dáno specificky do uvozovek, aby z výsledných logů bylo přesně jasné kde začíná a končí daný string/hodnota a dala se například odhalit mezera na víc čí prázdnost proměné jen pohledem do logů.
```python
'{login_page}'
```
### Live logging - aneb jak a proč si logy jednoduše zobrazit

Pokud chcete v konzoli zobrazit výstup z logu stačí přidat parametr --log-cli-level [log_level]

```bash
pytest .\test.py --log-cli-level INFO
```
```bash
pytest .\test.py --log-cli-level DEBUG
```
```bash
pytest .\test.py --log-cli-level 0
```

Více o levelech a live loggingu najdete zde
- https://docs.python.org/3/library/logging.html#levels
- https://docs.pytest.org/en/7.1.x/how-to/logging.html#live-logs

je tam i napsáno jak logy poslat přes pytest do souboru.

K čemu je dobré věnovat se logům z vašeho testu a podívat se na ně?
- uvědomíte si jak průběh testu vypadá pro ostatní, a zda není ještě třeba něco vypsat/opravitm aby to bylo správně či pochopitelné.
- odhalíte případné chyby kterých jste si doposud nevšimli. (Třeba, že to nějakou částí kódu vůbec neprojde, nebo že se testovaný subjekt - Systeém under test - SUT, chová jinak, než by jste očekávali)
- logy jde použít k ověření si, že test funguje tak jak má.
- ...
