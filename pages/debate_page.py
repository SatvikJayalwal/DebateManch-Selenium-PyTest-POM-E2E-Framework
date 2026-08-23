from pages.base_page import BasePage
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DebatePage(BasePage):

    DEVELOPER_VS_TESTER_PATH = (By.XPATH,"//button[contains(text(),'DEVELOPER vs TESTER')]")
    ADD_QUESTION_TITLE = (By.XPATH,"//div[@data-testid='add-question-section']//h3[contains(text(),'Add New Question')]")
    TESTER_RADIO_BTN = (By.XPATH,"//input[@data-testid='side-selector-right-radio']")
    ADD_QUESTION_TEXTBOX_PATH = (By.XPATH,"//div[@id='newQuestionText']")
    ADD_TAG_PATH = (By.XPATH,"//input[@id='newTag']")
    UPLOAD_EVIDENCE_FILE = (By.XPATH,"//input[@data-testid='new-question-file-input']")
    UPLOADED_EVIDENCE_FILE_NAME = (By.XPATH,"//span[@data-testid='new-question-file-name-0']")
    URL_EVIDENCE_TEXTBOX_PATH = (By.XPATH,"//input[@data-testid='new-question-url-input']")
    ADD_URL_BTN = (By.XPATH,"//button[@data-testid='new-question-add-url-button']")
    ADD_QUESTION_BTN = (By.XPATH,"//button[@data-testid='add-question-submit-button']")

    def open_developer_vs_tester_debate(self):
        self.click_element(self.DEVELOPER_VS_TESTER_PATH)

    def is_add_question_title_displayed(self):
        return self.find_element(self.ADD_QUESTION_TITLE).is_displayed()

    def click_tester_radio_button(self):
        self.click_element(self.TESTER_RADIO_BTN)

    def type_question_in_textbox(self,question_text):
        self.send_keys_element(self.ADD_QUESTION_TEXTBOX_PATH, question_text)

    def type_tag_in_textbox(self):
        self.send_keys_element(self.ADD_TAG_PATH,"#Testing_is_important")

    def press_enter_to_add_tag(self):
        self.press_enter_key(self.ADD_TAG_PATH)

    def upload_evidence_file(self,file_path):
        self.send_keys_element(self.UPLOAD_EVIDENCE_FILE,file_path)

    def get_uploaded_evidence_file_name(self):
        return self.find_element(self.UPLOADED_EVIDENCE_FILE_NAME).text

    def paste_url_evidence(self,url_evidence_link):
        self.send_keys_element(self.URL_EVIDENCE_TEXTBOX_PATH,url_evidence_link)

    def click_add_url_btn(self):
        self.click_element(self.ADD_URL_BTN)

    def click_add_question_btn(self):
        self.click_element(self.ADD_QUESTION_BTN)

    def is_posted_question_displayed(self, specific_question_text):
        # Used f-string to inject the exact question text into the XPath
        dynamic_question_path = (By.XPATH, f"//div[@data-testid='board-full']//*[contains(text(), '{specific_question_text}')]")
        
        return self.find_element(dynamic_question_path).is_displayed()

    