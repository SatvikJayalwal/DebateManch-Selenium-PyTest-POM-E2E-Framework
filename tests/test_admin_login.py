from pages.admin_login_page import AdminLoginPage
import logging

def test_login_with_admin(driver):
    admin_login = AdminLoginPage(driver)

    logging.info("CLICKING ON ADMIN LOGIN")
    admin_login.open_admin_login_page()

    logging.info("VERIFYING ADMIN LOGIN TITLE IS VISIBLE")
    assert admin_login.is_admin_login_title_displayed(),"ADMIN LOGIN TITLE NOT DISPLAYED"
    logging.info("ADMIN LOGIN TITLE DISPLAYED SUCCESSFULLY")

    logging.info("FILLING USERNAME")
    admin_login.fill_admin_login_username()

    logging.info("FILLING PASSWORD")
    admin_login.fill_admin_login_password()

    logging.info("CLICKING LOGIN BUTTON")
    admin_login.click_admin_login_btn()

    logging.info("VERIFYING ADMIN DASHBOARD TITLE IS VISIBLE")
    assert admin_login.is_admin_dashboard_displayed(), "\nADMIN DASHBOARD TITLE NOT DISPLAYED"
    logging.info("ADMIN DASHBOARD TITLE DISPLAYED SUCCESSFULLY")

