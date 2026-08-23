from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from configparser import ConfigParser

class AdminLoginPage(BasePage):
    ADMIN_LOGIN = (By.XPATH,"//span[@data-testid='nav-admin']")
    ADMIN_LOGIN_TITLE = (By.XPATH,"//h2[@data-testid='admin-login-title']")
    ADMIN_LOGIN_USERNAME_PATH = (By.XPATH,"//input[@data-testid='admin-login-username-input']")
    ADMIN_LOGIN_PASSWORD_PATH = (By.XPATH,"//input[@data-testid='admin-login-password-input']")
    LOGIN_BTN = (By.XPATH,"//button[@data-testid='admin-login-submit-button']")
    ADMIN_DASHBOARD_PATH = (By.XPATH,"//div[@class='admin-header']//h1[contains(text(),'Admin Dashboard')]")

    config = ConfigParser()
    config.read("config.ini")

    ADMIN_USERNAME = config.get("ADMIN","admin_username")
    ADMIN_PASSWORD = config.get("ADMIN","admin_password")

    def open_admin_login_page(self):
        self.click_element(self.ADMIN_LOGIN)

    def is_admin_login_title_displayed(self):
        return self.find_element(self.ADMIN_LOGIN_TITLE).is_displayed()

    def fill_admin_login_username(self):
        self.send_keys_element(self.ADMIN_LOGIN_USERNAME_PATH,self.ADMIN_USERNAME)

    def fill_admin_login_password(self):
        self.send_keys_element(self.ADMIN_LOGIN_PASSWORD_PATH,self.ADMIN_PASSWORD)

    def click_admin_login_btn(self):
        self.click_element(self.LOGIN_BTN)

    def is_admin_dashboard_displayed(self):
        return self.find_element(self.ADMIN_DASHBOARD_PATH).is_displayed()



    

    
