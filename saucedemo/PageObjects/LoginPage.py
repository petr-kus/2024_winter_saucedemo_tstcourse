class LoginPage:
    password_field = "password"
    login_name_field = "user-name"
    login_button = "login-button"

    def __init__(self,driver):
        self.driver = driver

    def login(self,name,password):
        self.driver.find_element(By.ID,self.login_name_field ).send_keys(name)
        self.driver.find_element(By.ID,self.password_field).send_keys(password)
        self.driver.find_element(By.ID,self.login_button).click()
