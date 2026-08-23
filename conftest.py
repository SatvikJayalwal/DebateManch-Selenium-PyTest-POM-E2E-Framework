from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import pytest
from configparser import ConfigParser

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
        