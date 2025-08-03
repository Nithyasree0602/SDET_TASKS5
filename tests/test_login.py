import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from selenium import webdriver
from pages.login_page import LoginPage
import time


driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.saucedemo.com/")


login_page = LoginPage(driver)

login_page.login("standard_user", "secret_sauce")


time.sleep(5)
if "inventory" in driver.current_url:
    print("Login successful!")
else:
    print("Login failed or error occurred.")
    print("Error message:", login_page.get_error_message())

driver.quit()
