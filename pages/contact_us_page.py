from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class ContactUsPage(BasePage):

    CONTACT_US_PATH = (By.XPATH,"//span[@data-testid='nav-contact']")
    CONTACT_US_TITLE_PATH = (By.XPATH,"//h2[@data-testid='contact-heading']")
    NAME_TEXTBOX = (By.XPATH,"//input[@data-testid='contact-name-input']")
    EMAIL_TEXTBOX = (By.XPATH,"//input[@data-testid='contact-email-input']")
    SUBJECT_TEXTBOX = (By.XPATH,"//input[@data-testid='contact-subject-input']")
    MESSAGE_TEXTBOX = (By.XPATH,"//textarea[@data-testid='contact-message-textarea']")
    SEND_BTN = (By.XPATH,"//button[@data-testid='contact-submit-button']")
    SUCCESS_MESSAGE = (By.XPATH,"//*[contains(text(),'Your message has been received.')]")

    def click_contact_us(self):
        self.click_element(self.CONTACT_US_PATH)

    def is_contact_us_title_displayed(self):
        return self.find_element(self.CONTACT_US_TITLE_PATH).is_displayed()

    def type_name(self,name):
        self.send_keys_element(self.NAME_TEXTBOX,name)

    def type_email(self,email):
        self.send_keys_element(self.EMAIL_TEXTBOX,email)

    def type_subject(self,subject):
        self.send_keys_element(self.SUBJECT_TEXTBOX,subject)

    def type_message(self,message):
        self.send_keys_element(self.MESSAGE_TEXTBOX,message)

    def click_send_btn(self):
        self.click_element(self.SEND_BTN)

    def is_verification_displayed(self):
        return self.find_element(self.SUCCESS_MESSAGE).is_displayed()

    def is_email_error_displayed(self):
        email_element = self.find_element(self.EMAIL_TEXTBOX)
        return email_element.get_attribute("validationMessage")

    

    
    