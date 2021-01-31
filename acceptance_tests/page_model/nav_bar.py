from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from acceptance_tests.locators.nav_bar import NavBarLocators
from acceptance_tests.page_model.base_page import BasePage


class NavBarPage(BasePage):

    @property
    def settings_gear_icon(self):
        return self.find_element(*NavBarLocators.GEAR_ICON)

    def setting_gear_section(self, section):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_any_elements_located(NavBarLocators.GEAR_MENU_OPTIONS))
        options = self.find_elements(*NavBarLocators.GEAR_MENU_OPTIONS)
        for option in options:
            if option.text.lower() == section:
                return option
