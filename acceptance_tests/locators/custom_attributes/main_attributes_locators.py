from selenium.webdriver.common.by import By


class CustomAttributesLocator:
    ADD_CUSTOM_ATTRIBUTE_BTN = By.XPATH, "//button[text() = 'Add Custom Attribute']"
    ATTRIBUTE_ROWS = By.XPATH, "//div[contains(@class,'TabularRow-sc')]/div[contains(@class,'TabularRow-sc')]"
    ATTRIBUTE_TITLE_INPUT = By.XPATH, "//div[text() = 'Title'] /../ input"
    ATTRIBUTE_IDENTIFIER_INPUT = By.XPATH, "//div[text() = 'Identifier '] /../ input"
    ATTRIBUTE_DATA_TYPE_DROPDOWN = By.CSS_SELECTOR, ".react-select__value-container input"
    ATTRIBUTE_DATA_TYPE_DROPDOWN_OPTIONS = By.CSS_SELECTOR, '.react-select__menu div'
    SAVE_BTN = By.XPATH, "//*[@id='modals']//button[normalize-space()='Save']"
    CANCEL_BTN = By.XPATH, "//button[text()='Cancel']"
    ERROR_ALERTS = By.CSS_SELECTOR, "[class *='ErrorTooltip']"
    TITLE_ERROR_ALERT = By.XPATH, "//div[text() = 'Title']/../div[contains(@class,'ErrorTooltip')]"
    IDENTIFIER_ERROR_ALERT = By.XPATH, "//div[text() = 'Identifier ']/../div[contains(@class,'ErrorTooltip')]"
    DATA_TYPE_ERROR_ALERT = By.XPATH, "//div[text() = 'Data Type']/../div[contains(@class,'ErrorTooltip')]"
    EDIT_MORE_BTN = By.CSS_SELECTOR, "i[title='Options']"
    DELETE_BTN = By.XPATH, "//a[text()='Delete']"

