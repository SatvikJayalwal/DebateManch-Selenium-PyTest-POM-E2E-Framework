from pages.admin_login_page import AdminLoginPage

def test_login_with_admin(driver):
    admin_login = AdminLoginPage(driver)

    print("\nCLICKING ON ADMIN LOGIN")
    admin_login.open_admin_login_page()

    print("\nVERIFYING ADMIN LOGIN TITLE IS VISIBLE")
    assert admin_login.is_admin_login_title_displayed(),"ADMIN LOGIN TITLE NOT DISPLAYED"
    print("ADMIN LOGIN TITLE DISPLAYED SUCCESSFULLY")

    print("\nFILLING USERNAME")
    admin_login.fill_admin_login_username()

    print("\nFILLING PASSWORD")
    admin_login.fill_admin_login_password()

    print("\nCLICKING LOGIN BUTTON")
    admin_login.click_admin_login_btn()

    print("\nVERIFYING ADMIN DASHBOARD TITLE IS VISIBLE")
    assert admin_login.is_admin_dashboard_displayed(), "\nADMIN DASHBOARD TITLE NOT DISPLAYED"
    print("\nADMIN DASHBOARD TITLE DISPLAYED SUCCESSFULLY")

