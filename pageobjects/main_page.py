from mytestlib.base_page import BasePage
from selenium.webdriver.common.by import By


class MainPage(BasePage):

    PAGE_TITLE = 'Apple (Россия) – Официальный сайт'

    LOCATORS = {
        "Mac": (By.XPATH, '//*[@href="/ru/mac/"]')
    }