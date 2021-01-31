from acceptance_tests.locators.home_page import HomePageLocators
from acceptance_tests.page_model.base_page import BasePage


class HomePage(BasePage):

    @property
    def go_to_home(self):
        return self.find_element(*HomePageLocators.GO_TO_HOME_ICON)
