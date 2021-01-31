from selenium.webdriver.common.by import By

from acceptance_tests.locators.custom_attributes.main_attributes_locators import CustomAttributesLocator
from acceptance_tests.page_model.base_page import BasePage

DELETE_ATTRIBUTE_CONFIRMATION_MESSAGE = "Are you sure you want to remove the custom attribute?"


class CustomAttributes(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @property
    def url(self):
        return super(CustomAttributes, self).url + 'settings/custom-attributes'

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

    @property
    def error_alerts(self):
        return self.find_elements(*CustomAttributesLocator.ERROR_ALERTS)

    @property
    def title_error_message(self):
        return self.get_text_from_element(CustomAttributesLocator.TITLE_ERROR_ALERT)

    @property
    def identifier_error_message(self):
        return self.get_text_from_element(CustomAttributesLocator.IDENTIFIER_ERROR_ALERT)

    @property
    def data_type_error_message(self):
        return self.get_text_from_element(CustomAttributesLocator.DATA_TYPE_ERROR_ALERT)

    @property
    def table_rows(self):
        rows = self.find_elements(*CustomAttributesLocator.ATTRIBUTE_ROWS)
        table = []
        for row in rows:
            cells = row.find_elements(By.CSS_SELECTOR, "[class^='TabularCell'] span")
            table.append({
                'name': cells[0].text.lower(),
                'identifier': cells[1].text.lower(),
                'data_type': cells[2].text.lower()
            })
        return table
