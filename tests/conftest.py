import pytest
from selenium import webdriver


@pytest.fixture(scope="session", autouse=True)
def init_driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(0)
    yield driver
    driver.quit()
