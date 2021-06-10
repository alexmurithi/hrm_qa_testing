from behave import *
from selenium import webdriver


@given('I launch chrome browser')
def launch_browser(context):
    context.driver = webdriver.Chrome()


@when('I open OrangeHrm homepage')
def open_homepage(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/")


@when('Enter username "{user}" and password "{password}"')
def enter_credentials(context, user, password):
    context.driver.find_element_by_id("txtUsername").clear()
    context.driver.find_element_by_id("txtUsername").send_keys(user)

    context.driver.find_element_by_id("txtPassword").clear()
    context.driver.find_element_by_id("txtPassword").send_keys(password)


@when('click login button')
def click_login_btn(context):
    context.driver.find_element_by_id("btnLogin").click()


@then("User must successfully login to the Dashboard panel")
def login_to_dashboard(context):
    try:
        text = context.driver.find_element_by_xpath("//h1[contains(text(),'Dashboard')]").text
    except:
        context.driver.close()
        assert False, "Test Failed"
    if text == "Dashboard":
        context.driver.close()
        assert True, "Test Passed"
