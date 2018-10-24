from mytestlib.base_page import BasePage
from selenium.webdriver.common.by import By


class MacPage(BasePage):

    PAGE_TITLE = 'Mac – Apple (RU)'

    LOCATORS = {
        "Macbook": (By.XPATH, '//*[@href="/ru/macbook/"]')
    }