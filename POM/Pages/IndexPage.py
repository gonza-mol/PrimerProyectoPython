from selenium.webdriver.common.by import By

class IndexPageLocators():
    btn_sign_in = (By.XPATH, "//a[contains(text(),'Sign in')]")

class IndexPage():

    def __init__(self, driver):
        self.driver = driver

    def click_Sign_In(self):
        self.driver.find_element(*IndexPageLocators.btn_sign_in).click()

