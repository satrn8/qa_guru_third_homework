import pytest
from selene import be, have
from selene.support.shared import browser
browser.config.timeout = 2


@pytest.fixture()
def test_one():
    browser.open("https://www.google.com/ncr")


@pytest.fixture()
def test_two():
    browser.element("[name=q]").should(be.blank).type("selene").press_enter()


@pytest.fixture(scope='session', autouse=True)
def config_browser():
    browser.window_width = 1200
    browser.window_height = 1000


def test_positive(open_google, test_open):
    browser.element("[id=search]").should(have.text("Selene - User-oriented Web UI browser tests in Python"))


def test_negative(open_google, test_open):
    browser.element("[id=search]").should(have.no.text("123"))