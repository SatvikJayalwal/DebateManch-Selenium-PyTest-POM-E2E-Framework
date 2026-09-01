from pages.debate_page import DebatePage
from pages.home_page import HomePage
import os
from datetime import datetime

def test_adding_new_debate_question(driver):

    debate_page = DebatePage(driver)
    home_page = HomePage(driver)

    unique_id = datetime.now().strftime("%I:%M:%S:%p") 
    expected_question = f"Do you think developing is more important? {unique_id}"

    project_root = os.getcwd()
    evidence_file_path = os.path.join(project_root,"test_data_files","software_testing_importance_evidence.jpg")

    expected_url_fragment = "geeksforgeeks.org/software-testing"
    
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