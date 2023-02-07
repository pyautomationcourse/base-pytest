from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):
    EMAIL_INPUT = (By.ID, "email")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")

    def enter_email(self, email):
        self.type_in(self.EMAIL_INPUT, email)

    def enter_password(self, password):
        self.type_in(self.PASSWORD_INPUT, password)

    def click_login_button(self):
        self.click_on(self.LOGIN_BUTTON)
