from acceptance_tests.locators.custom_attributes.delete_component_locators import \
    CustomAttributesDeleteAlertLocator as Delete
from acceptance_tests.page_model.base_page import BasePage


class DeleteAttributeAlert(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @property
    def message(self):
        return self.find_element(*Delete.DELETE_CONFIRMATION_MESSAGE).text

    @property
    def accept_btn(self):
        return self.find_element(*Delete.DELETE_ACCEPT_BTN)

    @property
    def cancel_btn(self):
        return self.find_element(*Delete.DELETE_CANCEL_BTN)

    @property
    def close_btn(self):
        return self.find_element(*Delete.DELETE_CLOSE_BTN)
