"""
Параметризуйте фикстуру несколькими вариантами размеров окна.
Пропустите мобильный тест, если соотношение сторон десктопное (и наоборот)
"""
from selene import browser
import pytest


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
        yield 'desktop browser'
    else:
        yield 'mobile browser'


def test_github_desktop(window_size):
    if window_size == 'mobile browser':
        pytest.skip('This is mobile browser')
    browser.open('')
    browser.element('.HeaderMenu-link--sign-up').click()


def test_github_mobile(window_size):
    if window_size == 'desktop browser':
        pytest.skip('This is desktop browser')
    browser.open('')
    browser.element('.Button--link').click()
    browser.element('.HeaderMenu-link--sign-up').click()
