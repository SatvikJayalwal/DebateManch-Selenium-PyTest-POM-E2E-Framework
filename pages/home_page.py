from selenium import webdriver
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import json

class HomePage(BasePage):

    SEARCH_BOX = (By.XPATH,"//div[@class='add-topic-form']//input")
    ADD_TOPIC_BTN = (By.XPATH,"//button[contains(text(),'Add Topic')]")
    LOGIN_BTN = (By.XPATH,"//div[@data-testid='topnav-inner']//span[contains(text(),'Login')]")
    LOGIN_POPUP = (By.XPATH,"//div[@data-testid='login-modal-header']//h2[contains(text(),'Login Required')]")
    IFRAME_XPATH = (By.XPATH,"//iframe[contains(@src,'accounts.google.com')]")
    LOGOUT_BTN = (By.XPATH,"//span[@data-testid='nav-logout']")
    TOPIC_ADDED = (By.XPATH,"//div[contains(text(),'Topic added successfully')]")
    TOPIC_ALREADY_EXISTS = (By.XPATH,"//div[contains(text(),'Topic already exists')]")


    def click_add_topic_btn(self):
        self.click_element(self.ADD_TOPIC_BTN)

    def type_in_add_topic_box(self,text_to_add):
        self.send_keys_element(self.SEARCH_BOX,text_to_add)        

    def is_login_popup_displayed(self):
        return self.find_element(self.LOGIN_POPUP).is_displayed()

    def open_login(self):
        return self.click_element(self.LOGIN_BTN)

    def click_google_login(self):
        return self.find_element(self.IFRAME_XPATH).click()

    # R.E.I.R. (Read, Extract, Inject, Refresh)
    # Read user_token from storage.json, Extract the JSON, Inject it in website 
    # with javascript for bypassing login, Refresh page
    def login_through_local_storage_with_javascript_and_refresh(self,file_path="storage.json"):
            with open(file_path,'r') as file:
                data = json.load(file)
                token_value = data["user_token"]
    
            self.driver.execute_script(f"window.localStorage.setItem('user_token','{token_value}');")
            self.driver.refresh()

    def is_logout_button_displayed(self):
        return self.find_element(self.LOGOUT_BTN).is_displayed()   

    def is_topic_added_displayed(self):
        return self.find_element(self.TOPIC_ADDED).is_displayed()

    def is_topic_already_exist_displayed(self):
        return self.find_element(self.TOPIC_ALREADY_EXISTS).is_displayed()