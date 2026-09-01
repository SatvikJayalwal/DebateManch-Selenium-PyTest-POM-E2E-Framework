from pages.debate_page import DebatePage
from pages.home_page import HomePage
import os
from datetime import datetime

def test_reply_question(driver):

    debate_page = DebatePage(driver)
    home_page = HomePage(driver)

    unique_id = datetime.now().strftime("%I:%M:%S:%p")
    expected_question = f"Do you think developing is more important? {unique_id}"

    project_root = os.getcwd()
    evidence_file_path = os.path.join(project_root,"test_data_files","software_testing_importance_evidence.jpg")
    
    expected_url_fragment = "geeksforgeeks.org/software-testing"

    reply_text = f"THIS IS TEST REPLY TO THE QUESTION {unique_id}"

    expected_file_name = "software_testing_importance_evidence.jpg"
    
    print("\nVERIFYING USER LOGIN")
    home_page.login_through_local_storage_with_javascript_and_refresh()
    
    print("\nVERIFYING USER IS LOGGED IN")
    assert home_page.is_logout_button_displayed(), "\nUSER DID NOT LOGIN"    
    
    print("\nCLIKING DEVELOPER VS TESTER DEBATE")
    debate_page.open_developer_vs_tester_debate()

    print("\nVERIFYING IF THE DEBATE PAGE IS OPENED")
    assert debate_page.is_add_question_title_displayed(), "\nDEBATE PAGE NOT OPENED"
    print("\nDEBATE PAGE IS SUCCESSFULLY OPENED")

    print("\nCLICKING TESTER RADIO BUTTON")
    debate_page.click_tester_radio_button()

    print("\nTYPING QUESTION IN TEXTBOX")
    debate_page.type_question_in_textbox(expected_question)

    print("\nADDING TAG/TAGS")
    debate_page.type_tag_in_textbox()

    print("\nPRESSING ENTER TO ADD TAG")
    debate_page.press_enter_to_add_tag()

    print("\nUPLOADING EVIDENCE FILE")
    debate_page.upload_evidence_file(evidence_file_path)

    print("\nGET UPLOADED EVIDENCE FILE NAME")
    evidence_file_text_after_upload = debate_page.get_uploaded_evidence_file_name()

    print("\nVERIFYING THE FILE UPLOAD")
    assert "software_testing_importance_evidence.jpg" in evidence_file_text_after_upload, f"FILE UPLOAD FAILED, FILE NOT FOUND: {evidence_file_text_after_upload}"
    print("\nFILE VERIFIED SUCCESSFULLY")

    print("\nPASTING URL EVIDENCE")
    debate_page.paste_url_evidence(expected_url_fragment)

    print("\nCLICKING ADD URL BUTTON")
    debate_page.click_add_url_btn()

    print("\nCLICKING ADD QUESTION BUTTON")
    debate_page.click_add_question_btn()

    print("\nVERIFYING THE QUESTION IS ADDED TO THE BOARD")
    assert debate_page.is_posted_question_displayed(expected_question), f"\nFAILED: QUESTION NOT FOUND ON BOARD - {expected_question}"
    print("\nQUESTION SUCCESSFULLY DISPLAYED ON THE BOARD")    

    print("\nVERIFYING QUESTION ATTACHMENTS (TAG, FILE, URL) ON THE BOARD")
    expected_tag = "Testing_is_important"
    expected_file_name = "software_testing_importance_evidence.jpg"

    assert debate_page.verify_question_attachments(expected_question,expected_tag,expected_file_name,expected_url_fragment), "\nFAILED: ATTACHMENTS NOT FOUND WITH SPECIFIC QUESTION CARD"
    print("\nQUESTION ATTACHMENTS (TAG, FILE, URL) SUCCESSFULLY VERIFIED ON THE BOARD")

    print("\nCLICKING REPLY BUTTON")
    debate_page.click_reply_btn(expected_question)

    print("\nTYPING REPLY")
    debate_page.type_reply_text(expected_question,reply_text)

    print("\nUPLOADING REPLY FILE")
    debate_page.upload_reply_file(expected_question,evidence_file_path)

    print("\nADDING REPLY URL")
    debate_page.add_reply_url(expected_question,expected_url_fragment)

    print("\nCLICKING POST REPLY BUTTON")
    debate_page.click_post_reply_btn(expected_question)

    print("\nVERIFYING REPLY IS DISPLAYED ON THE BOARD")
    expected_file_name = "software_testing_importance_evidence.jpg"
    
    actual_text,actual_file,actual_url = debate_page.get_posted_reply_details(expected_question,reply_text,expected_file_name,expected_url_fragment)

    assert reply_text in actual_text, "\nFAILED: REPLY NOT FOUND ON BOARD"
    assert expected_file_name in actual_file, "\nFAILED: REPLY NOT FOUND ON BOARD"
    assert expected_url_fragment in actual_url, "\nFAILED: REPLY NOT FOUND ON BOARD"

    print("\nREPLY SUCCESSFULLY DISPLAYED")
