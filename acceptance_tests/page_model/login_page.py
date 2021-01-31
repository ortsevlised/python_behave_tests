from acceptance_tests.locators.login_page import LoginPageLocators
from acceptance_tests.page_model.base_page import BasePage


class LoginPage(BasePage):
    @property
    def url(self):
        return super(LoginPage, self).url + '/login'

    @property
    def username_input(self):
        return self.find_element(*LoginPageLocators.EMAIL_ADDRESS)

    @property
    def password_input(self):
        return self.find_element(*LoginPageLocators.PASSWORD)

    @property
    def login_btn(self):
        return self.find_element(*LoginPageLocators.LOGIN_BTN)
