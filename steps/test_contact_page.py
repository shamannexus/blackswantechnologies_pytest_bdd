from pytest_bdd import scenario, given, when, then, scenarios
from selenium import webdriver
from contact_page import ContactPage
from time import sleep
import pytest


# another way to include feature files
# @scenario('../features/test_contact_page.feature', 'Test contact page')
# def test_contact_page():
#     pass

scenarios('../features/test_contact_page.feature')

# init Contact page object
contact_page_helper = ContactPage()


@when('I fill all fields')
def fill_contact_data(browser):
    contact_page_helper.fill_contact_form(browser, 'name', 'Bogdan')
    contact_page_helper.fill_contact_form(browser, 'email', 'boduk.nexus@gmail.com')
    contact_page_helper.fill_contact_form(browser, 'company', 'IT_testing')
    contact_page_helper.fill_contact_form(browser, 'number', '+4883962768')
    contact_page_helper.fill_contact_form(browser, 'comment', 'Selenium_testing')


@when('I click send button')
def click_button(browser):
    contact_page_helper.click_submit_button(browser)
    sleep(6)


@then('My request successfully send')
def check_request_send():
    #here should be connect to BD to check that request was send
    pass




