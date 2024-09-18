"""
Переопределите параметр с помощью indirect параметризации на уровне теста
"""
import pytest
from selene import browser


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


desktop_only = pytest.mark.parametrize('window_size', [(1600, 900),
                                                       (1920, 1080),
                                                       (3840, 2160)],
                                       ids=['HD', 'FHD', '4k'],
                                       indirect=True)
browser_only = pytest.mark.parametrize('window_size', [(430, 932),
                                                       (412, 915)],
                                       ids=['iPhone', 'Samsung'],
                                       indirect=True)


@desktop_only
def test_github_desktop(window_size):
    browser.open('')
    browser.element('.HeaderMenu-link--sign-up').click()


@browser_only
def test_github_mobile(window_size):
    browser.open('')
    browser.element('.Button--link').click()
    browser.element('.HeaderMenu-link--sign-up').click()
