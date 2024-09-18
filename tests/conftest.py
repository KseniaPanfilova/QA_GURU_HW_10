import pytest
from selene import browser


@pytest.fixture(scope='function', autouse=True)
def base_url():
    browser.config.base_url = 'https://github.com'

    yield

    browser.quit()
