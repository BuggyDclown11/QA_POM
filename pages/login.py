import time

from selenium.webdriver.common.by import By

from locator.locator import Locator


class Login:
    def __init__(self,driver):
        self.driver=driver
        self.l=Locator()

    def get_nav_login_id(self):
        return self.driver.find_element(By.ID,self.l.nav_login_bar_id)

    def click_nav_login(self):
        self.get_nav_login_id().click()

    def get_username_id(self):
        return self.driver.find_element(By.ID,self.l.username_form_id)

    def send_username(self,username):
        self.get_username_id().send_keys(username)

    def get_password_id(self):
        return self.driver.find_element(By.ID,self.l.password_form_id)

    def send_password(self,password):
        self.get_password_id().send_keys(password)

    def get_login_btn_id(self):
        return self.driver.find_element(By.XPATH,self.l.login_button_id)
    def click_login_btn(self):
        self.get_login_btn_id().click()

    def loginUser(self,username,password):
        self.click_nav_login()
        time.sleep(5)
        self.send_username(username)
        self.send_password(password)
        self.click_login_btn()