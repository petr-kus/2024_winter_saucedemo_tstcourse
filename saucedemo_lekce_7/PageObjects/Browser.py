class Browser:
    def __init__(self,driver):
        self.driver = driver

    def go_to_page(self,page):
        self.driver.get(page)
    
    def page(self):
        return self.driver.current_url