from behave import *

from acceptance_tests.page_model.settings.settings_page import SettingsPage

use_step_matcher("parse")


@step("selects the {section} menu")
def step_impl(context, section):
    settings_page = SettingsPage(context.driver)
    settings_page.setting_section(section).click()
