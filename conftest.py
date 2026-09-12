from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import pytest
from configparser import ConfigParser
import os
from datetime import datetime

chrome_options = Options()
# chrome_options.add_argument("--headless=new")
# chrome_options.add_argument("--incognito")
chrome_options.add_argument("--start-maximized")

config = ConfigParser()
config.read("config.ini")

BASE_URL = config.get("DEFAULT","url")

@pytest.fixture()
def driver():
    driver = webdriver.Chrome(options=chrome_options)    
    driver.get(BASE_URL)    
    yield driver    
    driver.quit()

@pytest.hookimpl(tryfirst=True,hookwrapper=True)
def pytest_runtest_makereport(item,call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("driver",None)       

        if driver:

            os.makedirs("screenshots",exist_ok=True)
            timestamp = datetime.now().strftime("%H-%M-%S")
            file_path = f"screenshots/{item.name}_{timestamp}.png"

            driver.save_screenshot(file_path)
            print(f"\nSCREENSHOT SAVED AT: {file_path}")