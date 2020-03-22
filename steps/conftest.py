import pytest
from selenium import webdriver
from pytest_bdd import scenario, given, when, then, scenarios
import logging


logging.basicConfig(level=logging.INFO)
mylogger = logging.getLogger()

# Constants

HOME_PAGE = "https://blackswantechnologies.ai/"


# Fixtures

@pytest.fixture()
def browser():
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.implicitly_wait(10)
    yield browser
    browser.quit()


# Shared steps

@given('I have open main page')
def open_main_page(browser):
    browser.get(HOME_PAGE)
    mylogger.info(browser.title)
    assert('BlackSwan Technologies - Intelligence of Everything', browser.title)


# Hooks

def pytest_bdd_step_error(request, feature, scenario, step, step_func, step_func_args, exception):
    mylogger.info('Step failed: {step}'.format(step=step))


def pytest_bdd_after_scenario(request, feature, scenario):
    mylogger.info('____TEST execution is finished =) _____')