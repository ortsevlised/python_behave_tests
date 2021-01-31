from behave import *

from acceptance_tests.locators.home_page import HomePageLocators
from acceptance_tests.page_model.login_page import LoginPage

admin = ({'user': 'superadmin@table.co', 'password': 'TABLE.Berkeley-1250'})


@step("the admin logs into Table.co")
def step_impl(context):
    login_page = LoginPage(context.driver)
    context.driver.get(login_page.url)
    login_page.username_input.send_keys(admin['user'])
    login_page.password_input.send_keys(admin['password'])
    login_page.login_btn.click()
    login_page.wait_for_element(HomePageLocators.GO_TO_HOME_ICON, 15)
