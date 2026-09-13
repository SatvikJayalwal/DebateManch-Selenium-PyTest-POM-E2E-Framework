from pages.home_page import HomePage
import logging

def test_login_with_js(driver):
    home_page = HomePage(driver)

    logging.info("VERIFYING USER LOGIN")
    home_page.login_through_local_storage_with_javascript_and_refresh()

    logging.info("VERIFYING USER IS LOGGED IN")
    assert home_page.is_logout_button_displayed(), "\nUSER DID NOT LOGIN"

    logging.info("LOGIN SUCCESSFULL") 