from pages.home_page import HomePage

def test_login_with_js(driver):
    home_page = HomePage(driver)

    print("\nVERIFYING USER LOGIN")
    home_page.login_through_local_storage_with_javascript_and_refresh()

    print("\nVERIFYING USER IS LOGGED IN")
    assert home_page.is_logout_button_displayed(), "\nUSER DID NOT LOGIN"

    print("\nLOGIN SUCCESSFULL") 