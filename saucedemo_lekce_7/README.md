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