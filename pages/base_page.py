from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def wait_for_element_present(self, by, locator):
        return self.wait.until(EC.presence_of_element_located((by, locator)))

    def wait_for_element_clickable(self, by, locator):
        return self.wait.until(EC.element_to_be_clickable((by, locator)))

    def wait_for_element_visible(self, by, locator):
        return self.wait.until(EC.visibility_of_element_located((by, locator)))

    def click(self, by, locator):
        try:
            self.wait_for_element_clickable(by, locator).click()
        except Exception as e:
            print(f"Error clicking element {locator}: {e}")

    def enter_text(self, by, locator, text):
        try:
            element = self.wait_for_element_visible(by, locator)
            element.clear()
            element.send_keys(text)
        except Exception as e:
            print(f"Error entering text in {locator}: {e}")

    def get_text(self, by, locator):
        try:
            return self.wait_for_element_visible(by, locator).text
        except Exception as e:
            print(f"Error getting text from {locator}: {e}")
            return ""

    def is_displayed(self, by, locator):
        try:
            return self.driver.find_element(by, locator).is_displayed()
        except:
            return False
