from random import randint

from hamcrest import *
from selenium.webdriver.common.by import By

from acceptance_tests.locators.custom_attributes.main_attributes_locators import CustomAttributesLocator
from acceptance_tests.page_model.base_page import BasePage
from acceptance_tests.page_model.settings.custom_attributes.delete_attribute_alert import DeleteAttributeAlert

DELETE_ATTRIBUTE_CONFIRMATION_MESSAGE = "Are you sure you want to remove the custom attribute?"


class DeleteAttribute(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def delete_attribute(self, identifier):
        delete_alert = DeleteAttributeAlert(self.driver)
        if identifier == 'random':
            attribute_rows = self.find_elements(*CustomAttributesLocator.ATTRIBUTE_ROWS)
            attribute = attribute_rows[randint(0, len(attribute_rows))]
            name, identifier_, data_type = attribute.text.split('\n')
            attribute_fields = {
                'name': name,
                'identifier': identifier_,
                'data_type': data_type
            }
        else:  # TODO
            attribute = 'some other element'
            attribute_fields = ''
            pass
        element = attribute.find_element(By.TAG_NAME, 'a')
        self.move_to_element(element).click()
        self.find_element(*CustomAttributesLocator.EDIT_MORE_BTN).click()
        self.find_element(*CustomAttributesLocator.DELETE_BTN).click()
        assert_that(delete_alert.message), equal_to('%s' % DELETE_ATTRIBUTE_CONFIRMATION_MESSAGE)
        delete_alert.accept_btn.click()
        return attribute_fields
