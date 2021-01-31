from selenium.webdriver.common.keys import Keys

from acceptance_tests.locators.custom_attributes.main_attributes_locators import CustomAttributesLocator
from acceptance_tests.page_model.base_page import BasePage


class AddAttribute(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @property
    def add_btn(self):
        return self.find_element(*CustomAttributesLocator.ADD_CUSTOM_ATTRIBUTE_BTN)

    @property
    def attribute_title(self):
        return self.find_element(*CustomAttributesLocator.ATTRIBUTE_TITLE_INPUT)

    @property
    def attribute_identifier(self):
        return self.find_element(*CustomAttributesLocator.ATTRIBUTE_IDENTIFIER_INPUT)

    @property
    def attribute_data_type_dropdown(self):
        return self.find_element(*CustomAttributesLocator.ATTRIBUTE_DATA_TYPE_DROPDOWN)

    @property
    def attribute_save_btn(self):
        return self.find_element(*CustomAttributesLocator.SAVE_BTN)

    @property
    def attribute_cancel_btn(self):
        return self.find_element(*CustomAttributesLocator.CANCEL_BTN)

    @property
    def select_data_type(self):
        return self.find_element(*CustomAttributesLocator.ATTRIBUTE_DATA_TYPE_DROPDOWN)

    def add_attribute(self, title, identifier, data_type):
        self.add_btn.click()
        self.attribute_title.send_keys(title)
        self.clear_input(self.attribute_identifier)
        self.attribute_identifier.send_keys(identifier)
        self.select_data_type.send_keys(data_type)
        self.select_data_type.send_keys(Keys.TAB)
        self.attribute_save_btn.click()
