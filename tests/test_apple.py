import time

import pytest

from pageobjects.mac_page import MacPage
from pageobjects.macbook_page import MacbookPage
from pageobjects.main_page import MainPage


@pytest.fixture
def print_hello():
    print('Hello!')


def test_macbooks(print_hello):
    on = pytest.on
    assert on(MainPage).is_page_opened(3)
    time.sleep(2)
    on(MainPage).click_at('Mac', 3)
    assert on(MacPage).is_page_opened(3)
    on(MacPage).click_at('Macbook', 3)
    assert on(MacbookPage).is_page_opened(3)
    assert on(MacbookPage).is_visible('Macbook header', 5)