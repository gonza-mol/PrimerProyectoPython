from selenium.webdriver.common.by import By


class MyAccountLocators():
    text_my_account = (By.XPATH, "//h1[contains(text(),'My account')]")

class MyAccount():

    def __init__(self, driver):
        self.driver = driver

    def verificar_Ingreso_Correcto(self):
        return self.driver.find_element(*MyAccountLocators.text_my_account).text