"""
Сделайте разные фикстуры для каждого теста, которые выставят размеры окна браузера
"""
from selene import browser
import pytest


@pytest.fixture(params=[
    (1600, 900),
    (1920, 1080),
    (3840, 2160),
],
    ids=['HD', 'FHD', '4k'])
def desktop_browser_config(request):
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height


@pytest.fixture(params=[
    (430, 932),
    (412, 915)
],
    ids=['iPhone', 'Samsung'])
def mobile_browser_config(request):
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height


def test_github_desktop(desktop_browser_config):
    browser.open('')
    browser.element('.HeaderMenu-link--sign-up').click()


def test_github_mobile(mobile_browser_config):
    browser.open('')
    browser.element('.Button--link').click()
    browser.element('.HeaderMenu-link--sign-up').click()
