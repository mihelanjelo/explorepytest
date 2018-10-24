import pytest
from mytestlib.helper import Helper
from selenium import webdriver


@pytest.yield_fixture(autouse=True)
def run_around_tests():
    helper = Helper(webdriver.Chrome())
    pytest.on = helper.on_page
    pytest.helper = helper
    helper.visit('https://www.apple.com/ru/')
    yield
    helper.quit()
