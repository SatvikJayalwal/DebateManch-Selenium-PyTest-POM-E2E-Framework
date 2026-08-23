from pages.home_page import HomePage

def test_type_in_add_topic_box(driver):

    home_page = HomePage(driver)
    print("\nADDING TOPIC IN TEXT BOX")
    home_page.type_in_add_topic_box("summer vs winter")
    print("\nCLICKING ADD TOPIC BUTTON")
    home_page.click_add_topic_btn()
    print("\nVERIFYING IF LOGIN POPUP IS DISPLAYED")
    assert home_page.is_login_popup_displayed(), "\nEXPECTED 'LOGIN POPUP' DID NOT APPEAR FOR GUEST USER"
    print("\nLOGIN POPUP IS SUCCESSFULLY DISPLAYED")
    
