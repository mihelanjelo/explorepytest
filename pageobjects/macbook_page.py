from mytestlib.base_page import BasePage
from selenium.webdriver.common.by import By


class MacbookPage(BasePage):

    PAGE_TITLE = 'MacBook – Apple (RU)'

    LOCATORS = {
        "Macbook header": (By.XPATH, '//h1[text()="MacBook"]')
    }