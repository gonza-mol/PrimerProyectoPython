from selenium.webdriver.common.by import By

class LoginPageLocators():
    txt_username = (By.CSS_SELECTOR, "#email")
    txt_password = (By.CSS_SELECTOR, "#passwd")
    btn_submit_sign_in = (By.CSS_SELECTOR, "#SubmitLogin")
    label_password_error = (By.XPATH, "//div[@id='center_column']/div/ol/li")
    label_password_without_value = (By.XPATH, "//li[contains(text(),'Password is required.')]")
    label_username_error = (By.XPATH, "//li[contains(text(),'Invalid email address.')]")
    label_username_without_value = (By.XPATH, "//li[contains(text(),'An email address required.')]")




class LoginPage():

    def __init__(self, driver):
        self.driver = driver

    def submit_Username(self, username):
        self.driver.find_element(*LoginPageLocators.txt_username).send_keys(username)

    def submit_Password(self, password):
        self.driver.find_element(*LoginPageLocators.txt_password).send_keys(password)

    def click_Submit_Sign_In(self):
        self.driver.find_element(*LoginPageLocators.btn_submit_sign_in).click()

    def show_error_password(self):
        return self.driver.find_element(*LoginPageLocators.label_password_error).text

    def show_error_without_password(self):
        return self.driver.find_element(*LoginPageLocators.label_password_without_value).text

    def show_error_username(self):
        return self.driver.find_element(*LoginPageLocators.label_username_error).text

    def show_error_without_username(self):
        return self.driver.find_element(*LoginPageLocators.label_username_without_value).text





