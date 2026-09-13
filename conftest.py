from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import pytest
from configparser import ConfigParser
import os
from datetime import datetime
import logging

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
            timestamp = datetime.now().strftime("%Y-%m-%d_%I-%M-%S_%p")
            file_path = f"screenshots/{item.name}_{timestamp}.png"

            driver.save_screenshot(file_path)
            logging.info(f"\nSCREENSHOT SAVED AT: {file_path}")

@pytest.hookimpl(tryfirst=True)
def pytest_runtest_setup(item):
    os.makedirs("logs",exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%d_%I-%M-%S_%p")
    log_file_path = f"logs/{item.name}_{timestamp}.log"
    file_handler = logging.FileHandler(log_file_path)
    formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s", datefmt="%Y-%m-%d %I:%M:%S %p")
    file_handler.setFormatter(formatter)

    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    logger.addHandler(file_handler)
    item.log_handler = file_handler

@pytest.hookimpl(trylast=True)
def pytest_runtest_teardown(item):
    handler = getattr(item,"log_handler",None)

    if handler:
        logger = logging.getLogger()
        logger.removeHandler(handler)
        handler.close()