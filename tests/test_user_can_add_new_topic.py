from pages.home_page import HomePage
import time

def test_user_add_new_topic(driver):
    home_page = HomePage(driver)

    print("\nDOING USER LOGIN WITH JS")
    home_page.login_through_local_storage_with_javascript_and_refresh()
    home_page.is_logout_button_displayed(), "\nUSER COULD NOT LOGIN"
    print("\nUSER LOGIN SUCCESSFULL WITH JS")

    print("\nTYPING TEXT TO ADD TOPIC IN TEXT BOX")
    home_page.type_in_add_topic_box(f"test_topicA vs Test_topicB {int(time.time())}")

    print("\nCLICKING ADD TOPIC BUTTON")
    home_page.click_add_topic_btn()

    assert home_page.is_topic_added_displayed(), "\nTOPIC NOT ADDED"
    print("\nTOPIC ADDED SUCCESSFULLY")  

    
