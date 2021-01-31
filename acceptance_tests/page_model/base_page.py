from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @property
    def url(self):
        return 'http://192.168.1.1:8080'

    @staticmethod
    def clear_input(element):
        while element.get_attribute("value") != "":
            element.send_keys(Keys.BACK_SPACE)
        return element

    def wait_for_element(self, locator, time):
        WebDriverWait(self.driver, int(time)).until(ec.visibility_of_element_located(locator))
        return self.find_element(*locator)

    def move_to_element(self, element):
        ActionChains(self.driver).move_to_element(element).perform()
        return element

    def get_text_from_element(self, element):
        if self.is_currently_visible(element):
            return self.find_element(*element).text
        else:
            return ""

    def is_currently_visible(self, element):
        self.driver.implicitly_wait(0)
        elements = self.find_elements(*element)
        if len(elements) > 0:
            is_visible = True
        else:
            is_visible = False
        self.driver.implicitly_wait(10)
        return is_visible

    def find_element(self, locator_attribute, locator_text):
        """
        Finds an element and returns the element object.
        :param locator_attribute: what to use to locate (example, id, class, xpath,....)
        :param locator_text: the locator text (ex. the id, the class, the name,...)
        """

        possible_locators = ["id", "xpath", "link text", "partial link text", "name", "tag name", "class name",
                             "css selector"]

        if locator_attribute not in possible_locators:
            raise Exception('The locator attribute provided is not in the approved attributes. '
                            'Or the spelling and format does not match.\
                                The approved attributes are : %s ' % possible_locators)
        try:
            element = self.driver.find_element(locator_attribute, locator_text)
            return element
        except Exception as e:
            raise Exception(e)

    # ======================================================================================#
    def find_elements(self, locator_attribute, locator_text):
        """
        Finds an element and returns the element object.
        :param locator_attribute: what to use to locate (example, id, class, xpath,....)
        :param locator_text: the locator text (ex. the id, the class, the name,...)
        """

        possible_locators = ["id", "xpath", "link text", "partial link text", "name", "tag name", "class name",
                             "css selector"]

        if locator_attribute not in possible_locators:
            raise Exception('The locator attribute provided is not in the approved attributes.'
                            ' Or the spelling and format does not match.\
                                The approved attributes are : %s ' % possible_locators)
        try:
            element = self.driver.find_elements(locator_attribute, locator_text)
            return element
        except Exception as e:
            raise Exception(e)
