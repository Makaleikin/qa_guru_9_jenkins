import os

import allure
from selene.support.shared import browser
import pytest


@allure.step('Конфигурация теста')
@pytest.fixture(scope='session', autouse=True)
def test_browser_configuration():
    browser.config.base_url = os.getenv('selene.base_url', 'https://demoqa.com')
    browser.config.browser_name = os.getenv('selene.browser_name', 'chrome')
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    yield
