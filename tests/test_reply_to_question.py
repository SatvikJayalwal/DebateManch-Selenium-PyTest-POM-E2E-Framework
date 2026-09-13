from pages.debate_page import DebatePage
from pages.home_page import HomePage
import os
from datetime import datetime
import logging

def test_reply_question(driver):

    debate_page = DebatePage(driver)
    home_page = HomePage(driver)

    unique_id = datetime.now().strftime("%Y-%m-%d_%I-%M-%S_%p")
    expected_question = f"Do you think developing is more important? {unique_id}"

    project_root = os.getcwd()
    evidence_file_path = os.path.join(project_root,"test_data_files","software_testing_importance_evidence.jpg")
    
    expected_url_fragment = "geeksforgeeks.org/software-testing"

    reply_text = f"THIS IS TEST REPLY TO THE QUESTION {unique_id}"

    expected_file_name = "software_testing_importance_evidence.jpg"
    
    logging.info("VERIFYING USER LOGIN")
    home_page.login_through_local_storage_with_javascript_and_refresh()
    
    logging.info("VERIFYING USER IS LOGGED IN")
    assert home_page.is_logout_button_displayed(), "\nUSER DID NOT LOGIN"    
    
    logging.info("CLIKING DEVELOPER VS TESTER DEBATE")
    debate_page.open_developer_vs_tester_debate()

    logging.info("VERIFYING IF THE DEBATE PAGE IS OPENED")
    assert debate_page.is_add_question_title_displayed(), "\nDEBATE PAGE NOT OPENED"
    logging.info("DEBATE PAGE IS SUCCESSFULLY OPENED")

    logging.info("CLICKING TESTER RADIO BUTTON")
    debate_page.click_tester_radio_button()

    logging.info("TYPING QUESTION IN TEXTBOX")
    debate_page.type_question_in_textbox(expected_question)

    logging.info("ADDING TAG/TAGS")
    debate_page.type_tag_in_textbox()

    logging.info("PRESSING ENTER TO ADD TAG")
    debate_page.press_enter_to_add_tag()

    logging.info("UPLOADING EVIDENCE FILE")
    debate_page.upload_evidence_file(evidence_file_path)

    logging.info("GET UPLOADED EVIDENCE FILE NAME")
    evidence_file_text_after_upload = debate_page.get_uploaded_evidence_file_name()

    logging.info("VERIFYING THE FILE UPLOAD")
    assert "software_testing_importance_evidence.jpg" in evidence_file_text_after_upload, f"FILE UPLOAD FAILED, FILE NOT FOUND: {evidence_file_text_after_upload}"
    logging.info("FILE VERIFIED SUCCESSFULLY")

    logging.info("PASTING URL EVIDENCE")
    debate_page.paste_url_evidence(expected_url_fragment)

    logging.info("CLICKING ADD URL BUTTON")
    debate_page.click_add_url_btn()

    logging.info("CLICKING ADD QUESTION BUTTON")
    debate_page.click_add_question_btn()

    logging.info("VERIFYING THE QUESTION IS ADDED TO THE BOARD")
    assert debate_page.is_posted_question_displayed(expected_question), f"\nFAILED: QUESTION NOT FOUND ON BOARD - {expected_question}"
    logging.info("QUESTION SUCCESSFULLY DISPLAYED ON THE BOARD")    

    logging.info("VERIFYING QUESTION ATTACHMENTS (TAG, FILE, URL) ON THE BOARD")
    expected_tag = "Testing_is_important"
    expected_file_name = "software_testing_importance_evidence.jpg"

    assert debate_page.verify_question_attachments(expected_question,expected_tag,expected_file_name,expected_url_fragment), "\nFAILED: ATTACHMENTS NOT FOUND WITH SPECIFIC QUESTION CARD"
    logging.info("QUESTION ATTACHMENTS (TAG, FILE, URL) SUCCESSFULLY VERIFIED ON THE BOARD")

    logging.info("CLICKING REPLY BUTTON")
    debate_page.click_reply_btn(expected_question)

    logging.info("TYPING REPLY")
    debate_page.type_reply_text(expected_question,reply_text)

    logging.info("UPLOADING REPLY FILE")
    debate_page.upload_reply_file(expected_question,evidence_file_path)

    logging.info("ADDING REPLY URL")
    debate_page.add_reply_url(expected_question,expected_url_fragment)

    logging.info("CLICKING POST REPLY BUTTON")
    debate_page.click_post_reply_btn(expected_question)

    logging.info("VERIFYING REPLY IS DISPLAYED ON THE BOARD")
    expected_file_name = "software_testing_importance_evidence.jpg"
    
    actual_text,actual_file,actual_url = debate_page.get_posted_reply_details(expected_question,reply_text,expected_file_name,expected_url_fragment)

    assert reply_text in actual_text, "\nFAILED: REPLY NOT FOUND ON BOARD"
    assert expected_file_name in actual_file, "\nFAILED: REPLY NOT FOUND ON BOARD"
    assert expected_url_fragment in actual_url, "\nFAILED: REPLY NOT FOUND ON BOARD"

    logging.info("REPLY SUCCESSFULLY DISPLAYED")
