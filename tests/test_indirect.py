import pytest
from selene import browser, be


@pytest.mark.parametrize("setup_browser", [(1920, 1080), (1280, 1220)], indirect=True)
def test_desktop_indirect(setup_browser):
    browser.open("https://github.com/")
    browser.element(".HeaderMenu-link--sign-in").should(be.visible).click()


@pytest.mark.parametrize("setup_browser", [(575, 660), (393, 873)], indirect=True)
def test_mobile_indirect(setup_browser):
    browser.open("https://github.com/")
    browser.element(".HeaderMenu-link.HeaderMenu-button.js-prevent-focus-on-mobile-nav").should(be.visible).click()