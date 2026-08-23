from pages.contact_us_page import ContactUsPage
from utilities.contact_us_data_loader import load_contact_us_data
import pytest

test_data = load_contact_us_data()
@pytest.mark.parametrize("name,email,subject,message,expected_success",test_data)
def test_contact_us_form_fill(driver,name,email,subject,message,expected_success):
    contact_us = ContactUsPage(driver)

    print("\nCLICKING CONTACT US")
    contact_us.click_contact_us()

    print("\nVERIFYING CONTACT US TITLE DISPLAYED")
    assert contact_us.is_contact_us_title_displayed(), "CONTACT US TITLE NOT DISPLAYED"
    print("\nCONTACT US TITLE DISPLAYED SUCCESSFULLY")

    print("\nTYPING DATA")   
    contact_us.type_name(name)
    contact_us.type_email(email)    
    contact_us.type_subject(subject)
    contact_us.type_message(message)

    print("\nCLICKING SEND BUTTON")
    contact_us.click_send_btn()

    print("\nVERIFY THE SUCCESS MESSAGE")

    if expected_success:        
        assert contact_us.is_verification_displayed(), "\nCONTACT US FORM NOT SUBMITTED"
        print("\nCONTACT US FORM SUBMITTED AND VERIFIED SUCCESSFULLY")

    else:
        assert contact_us.is_email_error_displayed(), "\nBUG : FORM SUBMITTED WITH INVALID EMAIL"
        print("\nNEGATIVE VALIDATION PASSED")
