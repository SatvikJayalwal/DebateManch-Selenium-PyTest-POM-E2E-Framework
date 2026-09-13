from pages.home_page import HomePage
import time
import logging

def test_user_cannot_add_duplicate_topic(driver):
    home_page = HomePage(driver)

    logging.info("DOING USER LOGIN WITH JS")
    home_page.login_through_local_storage_with_javascript_and_refresh()
    assert home_page.is_logout_button_displayed(), "\nUSER COULD NOT LOGIN"
    logging.info("USER LOGIN SUCCESSFUL WITH JS")

    unique_topic = f"Automation vs Manual {int(time.time())}"

    logging.info("TYPING NEW TOPIC IN TEXT BOX")
    home_page.type_in_add_topic_box(unique_topic)
    
    logging.info("CLICKING ADD TOPIC BUTTON (1st Time)")
    home_page.click_add_topic_btn()
    
    assert home_page.is_topic_added_displayed(), "Failed to add the initial topic"
    logging.info("FIRST TOPIC ADDED SUCCESSFULLY")

    logging.info("TYPING THE EXACT SAME TOPIC AGAIN")
    home_page.type_in_add_topic_box(unique_topic)
    
    logging.info("CLICKING ADD TOPIC BUTTON (2nd Time)")
    home_page.click_add_topic_btn()

    assert home_page.is_topic_already_exist_displayed(), "Duplicate warning did not appear!"
    logging.info("DUPLICATE TOPIC CAN NOT BE ADDED - TEST PASSED")