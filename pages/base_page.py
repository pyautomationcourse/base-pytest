import requests
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def send_request(method, url, auth=None, body=None, headers=None, params=None):
    """Send request using requests library"""
    if method == "GET":
        response = requests.get(url, auth=auth, headers=headers, params=params)
    elif method == "POST":
        response = requests.post(url, auth=auth, data=body, headers=headers, params=params)
    return response


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def get_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    def click_on(self, locator):
        self.get_element(locator).click()

    def type_in(self, locator, text):
        self.get_element(locator).send_keys(text)
