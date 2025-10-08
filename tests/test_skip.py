import pytest
from selene import browser, be



def test_skip_desktop(setup_browser):
    if setup_browser != "Desktop":
        pytest.skip("Window size test skip (Desc)")
    browser.open("https://github.com/")
    browser.element(".HeaderMenu-link--sign-in").should(be.visible).click()


def test_skip_mobile(setup_browser):
    if setup_browser != "Mobile":
        pytest.skip("Window size test skip (Mob)")
    browser.open("https://github.com/")
    browser.element(".HeaderMenu-link.HeaderMenu-button.js-prevent-focus-on-mobile-nav").should(be.visible).click()