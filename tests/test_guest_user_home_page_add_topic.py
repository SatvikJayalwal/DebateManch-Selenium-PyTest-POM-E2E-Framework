from pages.home_page import HomePage
import logging

def test_type_in_add_topic_box(driver):

    home_page = HomePage(driver)
    logging.info("ADDING TOPIC IN TEXT BOX")
    home_page.type_in_add_topic_box("summer vs winter")
    logging.info("CLICKING ADD TOPIC BUTTON")
    home_page.click_add_topic_btn()
    logging.info("VERIFYING IF LOGIN POPUP IS DISPLAYED")
    assert home_page.is_login_popup_displayed(), "\nEXPECTED 'LOGIN POPUP' DID NOT APPEAR FOR GUEST USER"
    logging.info("LOGIN POPUP IS SUCCESSFULLY DISPLAYED")
    
