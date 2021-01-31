from behave import *

from acceptance_tests.page_model.nav_bar import NavBarPage

use_step_matcher("parse")


@step("he goes to the {section} section")
def step_impl(context, section):
    nav_bar = NavBarPage(context.driver)
    nav_bar.settings_gear_icon.click()
    nav_bar.setting_gear_section(section).click()
