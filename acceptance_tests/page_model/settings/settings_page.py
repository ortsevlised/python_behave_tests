from acceptance_tests.locators.custom_attributes.main_attributes_locators import CustomAttributesLocator
from acceptance_tests.locators.settings_locators import SettingsLocators
from acceptance_tests.page_model.base_page import BasePage


class SettingsPage(BasePage):

    @property
    def url(self):
        return super(SettingsPage, self).url + '/settings'

    def setting_section(self, section):
        options = self.find_elements(*SettingsLocators.SETTINGS_MENU)
        for option in options:
            if option.text.lower() == section:
                return option

    @property
    def add_custom_attribute_btn(self):
        return self.find_element(*CustomAttributesLocator.ADD_CUSTOM_ATTRIBUTE_BTN)
