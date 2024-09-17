from selene import browser
import pytest


@pytest.mark.parametrize('window_width, window_height',
                         [(1920, 1080),
                          (412, 915)],
                         ids=['desktop', 'mobile'])
def test_desktop(window_width, window_height):
    if window_width > window_height:
        browser.config.window_width = window_width
        browser.config.window_height = window_height
        browser.open('https://github.com')
        browser.element('.HeaderMenu-link--sign-in').click()
    else:
        browser.config.window_width = window_width
        browser.config.window_height = window_height
        browser.open('https://github.com')
        browser.element('[href="/login"]').click()
    browser.quit()




