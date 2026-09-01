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

    def verify_question_attachments(self,specific_question_text,expected_tag,expected_file,expected_url_fragment):

        base_card = f"//*[contains(text(),'{specific_question_text}')]//ancestor::div[@data-testid[contains(.,'card')]]"

        tag_xpath = (By.XPATH,f"{base_card}//*[contains(text(),'{expected_tag}')]")
        file_xpath = (By.XPATH,f"{base_card}//*[contains(text(),'{expected_file}')]")
        url_xpath = (By.XPATH, f"{base_card}//*[contains(@href,'{expected_url_fragment}') or contains(text(), '{expected_url_fragment}')]")
        is_tag_displayed = self.find_element(tag_xpath).is_displayed()
        is_file_displayed = self.find_element(file_xpath).is_displayed()
        is_url_displayed = self.find_element(url_xpath).is_displayed()

        return is_tag_displayed and is_file_displayed and is_url_displayed

    def click_edit_btn(self,specific_question_text):
        base_card = f"//*[contains(text(),'{specific_question_text}')]//ancestor::div[@data-testid[contains(.,'card')]]"
        edit_btn_xpath = (By.XPATH,f"{base_card}//button[contains(text(),'Edit')]")
        self.scroll_to_element(edit_btn_xpath)
        self.click_element(edit_btn_xpath)

    def edit_question_text(self,specific_question_text,append_text_to_edit):
        base_card = f"//*[contains(text(),'{specific_question_text}')]//ancestor::div[@data-testid[contains(.,'card')]]"
        question_edit_textarea_path = (By.XPATH,f"{base_card}//div[@contenteditable='true' and contains(@data-testid,'card-edit-textarea')]")

        edit_question_box = self.find_element(question_edit_textarea_path)
        edit_question_box.send_keys(append_text_to_edit)

    def click_save_btn(self,specific_question_text):
        base_card = f"//*[contains(text(),'{specific_question_text}')]//ancestor::div[@data-testid[contains(.,'card')]]"
        save_btn = (By.XPATH,f"{base_card}//ancestor::div[@data-testid[contains(.,'card')]]//button[contains(text(),'Save')]")
        self.click_element(save_btn)
        self.wait.until(EC.invisibility_of_element_located(save_btn))

    def click_reply_btn(self,specific_question_text):
        base_card = f"//*[contains(text(),'{specific_question_text}')]//ancestor::div[@data-testid[contains(.,'card')]]"
        reply_btn = (By.XPATH,f"{base_card}//button[contains(@data-testid,'card-reply-button')]")
        self.scroll_to_element(reply_btn)
        self.click_element(reply_btn)

    def type_reply_text(self,specific_question_text,reply_text):
        base_card = f"//*[contains(text(),'{specific_question_text}')]//ancestor::div[@data-testid[contains(.,'card')]]"
        reply_box = (By.XPATH,f"{base_card}//div[@contenteditable='true' and contains(@data-testid,'reply-textarea')]")
        reply_element = self.find_element(reply_box)
        reply_element.send_keys(reply_text)

    def upload_reply_file(self,specific_question_text,reply_file_to_upload):
        base_card = f"//*[contains(text(),'{specific_question_text}')]//ancestor::div[@data-testid[contains(.,'card')]]"
        upload_reply_input = (By.XPATH,f"{base_card}//input[contains(@data-testid,'reply-file-input')]")
        reply_upload_file_element = self.send_keys_element(upload_reply_input,reply_file_to_upload)

    def add_reply_url(self,specific_question_text,reply_url_to_paste):
        base_card = f"//*[contains(text(),'{specific_question_text}')]//ancestor::div[@data-testid[contains(.,'card')]]"
        reply_url_element = (By.XPATH,f"{base_card}//input[contains(@data-testid,'reply-url-input')]")
        add_reply_url_btn = (By.XPATH,f"{base_card}//button[contains(@data-testid,'reply-add-url')]")
        self.send_keys_element(reply_url_element,reply_url_to_paste)
        self.click_element(add_reply_url_btn)

    def click_post_reply_btn(self,specific_question_text):
        base_card = f"//*[contains(text(),'{specific_question_text}')]//ancestor::div[@data-testid[contains(.,'card')]]"
        post_reply_btn = (By.XPATH,f"{base_card}//button[contains(@data-testid,'reply-post-button')]")
        self.scroll_to_element(post_reply_btn)
        self.click_element(post_reply_btn)
        self.wait.until(EC.invisibility_of_element_located(post_reply_btn))

    def is_reply_posted(self,specific_question_text,expected_reply_text):
        base_thread_row = f"//*[contains(text(),'{specific_question_text}')]//ancestor::div[contains(@class,'thread-row')]"
        reply_text_xpath = (By.XPATH,f"{base_thread_row}//*[contains(text(),'{expected_reply_text}')]")
        return self.find_element(reply_text_xpath).is_displayed()

    def get_posted_reply_details(self,specific_question_text,expected_reply_text,expected_file,expected_url_fragment):
        base_thread_row = f"//*[contains(text(),'{specific_question_text}')]//ancestor::div[contains(@class,'thread-row')]"
        reply_card = f"{base_thread_row}//*[contains(text(),'{expected_reply_text}')]//ancestor::div[@data-testid[contains(.,'card')]]"

        reply_text_xpath = (By.XPATH,f"{reply_card}//*[contains(text(),'{expected_reply_text}')]")
        reply_file_xpath = (By.XPATH,f"{reply_card}//*[contains(text(),'{expected_file}')]")
        reply_url_xpath = (By.XPATH,f"{reply_card}//*[contains(@href,'{expected_url_fragment}') or contains(text(),'{expected_url_fragment}')]")

        actual_reply_text = self.find_element(reply_text_xpath).text
        actual_reply_file = self.find_element(reply_file_xpath).text
        actual_reply_url = self.find_element(reply_url_xpath).text

        return actual_reply_text, actual_reply_file, actual_reply_url