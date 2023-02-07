from pages.login_page import LoginPage


class TestSelenium:
    def test_valid_login(self, init_driver):
        driver = init_driver
        login_page = LoginPage(driver)
        login_page.driver.get("https://www.wikipedia.org/")
        login_page.enter_email("test@example.com")
        login_page.enter_password("password")
        login_page.click_login_button()
        assert "Login successful" in driver.page_source

    def test_invalid_login(self, init_driver):
        driver = init_driver
        login_page = LoginPage(driver)
        login_page.driver.get("https://www.wikipedia.org/")
        login_page.enter_email("test@example.com")
        login_page.enter_password("wrongpassword")
        login_page.click_login_button()
        assert "Login failed" in driver.page_source
