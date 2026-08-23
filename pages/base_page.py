from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class BasePage():

    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,10)

    def find_element(self,locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def click_element(self,locator):
        element_to_click = self.wait.until(EC.element_to_be_clickable(locator))
        element_to_click.click()

    def send_keys_element(self,locator,keys):
        element_to_send = self.find_element(locator)
        element_to_send.clear()
        element_to_send.send_keys(keys)

    def press_enter_key(self,locator):
        element_to_enter = self.find_element(locator)
        element_to_enter.send_keys(Keys.ENTER)

        

    
