from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@given('launch chrome browser')
def launch_browser(context):
    context.driver = webdriver.Chrome()


@when('open orangehrm homepage')
def open_homepage(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/")


@then('verify that logo present on the page')
def verify_logo(context):
    status = context.driver.find_element(By.XPATH, "//div[@id='divLogo']").is_displayed()
    assert status is True


@then('close browser')
def close_browser(context):
    context.driver.close()
