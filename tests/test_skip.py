from selene import browser
import pytest


# @pytest.fixture()
# def desktop_browser_config():
#     browser.config.window_width = 1920
#     browser.config.window_height = 1080
#
#
# @pytest.fixture()
# def mobile_browser_config():
#     browser.config.window_width = 412
#     browser.config.window_height = 915
#
#
# def test_github_desktop(desktop_browser_config):
#     browser.open('')
#     browser.element('.HeaderMenu-link--sign-up').click()
#
#
# def test_github_mobile(mobile_browser_config):
#     browser.open('')
#     browser.element('.Button--link').click()
#     browser.element('.HeaderMenu-link--sign-up').click()


# @pytest.fixture(params=[
#     pytest.param(1600, 900, id='HD+'),
#     pytest.param(1920, 1080, id='FHD'),
#     pytest.param(3840, 2160, id='4K'),
#     pytest.param(430, 932, id='iPhone 14 Pro Max'),
#     pytest.param(412, 915, id='Samsung S20 Ultra')
# ])
@pytest.fixture(params=[
    (1600, 900),
    (1920, 1080),
    (3840, 2160),
    (430, 932),
    (412, 915)
],
    ids=['HD', 'FHD', '4k', 'iPhone', 'Samsung'])
def window_size(request):
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height
    if width >= 1600:
        yield 'desktop'
    else:
        yield 'mobile'


def test_github_desktop(window_size):
    if window_size == 'mobile':
        pytest.skip('This is mobile window size')
    browser.open('')
    browser.element('.HeaderMenu-link--sign-up').click()


def test_github_mobile(window_size):
    browser.open('')
    browser.element('.Button--link').click()
    browser.element('.HeaderMenu-link--sign-up').click()
