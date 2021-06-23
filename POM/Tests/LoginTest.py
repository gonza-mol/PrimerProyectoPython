from _ast import Assert

from selenium import webdriver
import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__),"..",".."))
import time
from POM.Pages.IndexPage import IndexPage
from POM.Pages.LoginPage import LoginPage
from POM.Pages.MyAccount import MyAccount
import HtmlTestRunner

class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome("C:\\Users\\admin\\PycharmProjects\\PrimerProyecto\\Drivers\\chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()



    def test_Login_success(self):
        driver = self.driver
        driver.get("http://automationpractice.com/index.php")
        time.sleep(2)
        index = IndexPage(driver)
        index.click_Sign_In()
        time.sleep(2)
        login = LoginPage(driver)
        time.sleep(2)
        login.submit_Username("gonzalo.molina@darwoft.com")
        time.sleep(2)
        login.submit_Password("Masterchef1")
        time.sleep(2)
        login.click_Submit_Sign_In()
        time.sleep(2)
        account = MyAccount(driver)
        x = account.verificar_Ingreso_Correcto()
        print(x)
        assert x == 'MY ACCOUNT'
        print("Estoy en la página de My account")


    def test_Login_failed_incorrect_username(self):
        driver = self.driver
        driver.get("http://automationpractice.com/index.php")
        time.sleep(2)
        index = IndexPage(driver)
        index.click_Sign_In()
        time.sleep(2)
        login = LoginPage(driver)
        login.submit_Username("gonzalo.molina@")
        login.submit_Password("Masterchef1")
        login.click_Submit_Sign_In()
        time.sleep(3)
        y = login.show_error_password()
        print(y)
        assert y == "Invalid email address."
        print("Error en el formato del valor del Email")


    def test_Login_failed_without_username(self):
        driver = self.driver
        driver.get("http://automationpractice.com/index.php")
        time.sleep(2)
        index = IndexPage(driver)
        index.click_Sign_In()
        time.sleep(2)
        login = LoginPage(driver)
        login.submit_Password("Masterchef1")
        login.click_Submit_Sign_In()
        time.sleep(3)
        y = login.show_error_without_username()
        print(y)
        assert y == "An email address required."
        print("Error al dejar el campo email vacío, es campo requerido")



    def test_Login_failed_incorrect_password(self):
        driver = self.driver
        driver.get("http://automationpractice.com/index.php")
        time.sleep(2)
        index = IndexPage(driver)
        index.click_Sign_In()
        time.sleep(2)
        login = LoginPage(driver)
        login.submit_Username("gonzalo.molina@darwoft.com")
        login.submit_Password("pppppp")
        login.click_Submit_Sign_In()
        time.sleep(3)
        y = login.show_error_password()
        print(y)
        assert y == "Authentication failed."
        print("Error al ingresar password incorrecta: " + y)



    def test_Login_failed_without_password(self):
        driver = self.driver
        driver.get("http://automationpractice.com/index.php")
        time.sleep(2)
        index = IndexPage(driver)
        index.click_Sign_In()
        time.sleep(2)
        login = LoginPage(driver)
        login.submit_Username("gonzalo.molina@darwoft.com")
        login.click_Submit_Sign_In()
        time.sleep(3)
        z = login.show_error_without_password()
        print(z)
        assert z == "Password is required."
        print("Error al dejar el campo password vacío, es campo requerido")


    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")

if __name__ == '__main__':
     unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\\Users\\admin\\PycharmProjects\\PrimerProyecto\\Reports'), verbosity=2)

