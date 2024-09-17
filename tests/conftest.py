import pytest
from selene import browser


@pytest.fixture()
def window_size_desktop():
    browser.config.window_width = 1920
    browser.config.window_height = 1080

    yield

    browser.quit()

@pytest.fixture()
def window_size_mobile():
    browser.config.window_width = 412
    browser.config.window_height = 915

    yield

    browser.quit()