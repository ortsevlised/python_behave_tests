from selenium.webdriver.common.by import By


class CustomAttributesDeleteAlertLocator:
    DELETE_ALERT = By.CSS_SELECTOR, "[class*='Overlay__Panel']"
    DELETE_CONFIRMATION_MESSAGE = By.CSS_SELECTOR, "[class*='Overlay__Title']"
    DELETE_CANCEL_BTN = By.XPATH, "//button[text()='Cancel']"
    DELETE_ACCEPT_BTN = By.XPATH, "//button[text()='Remove']"
    DELETE_CLOSE_BTN = By.CSS_SELECTOR, "[class*= 'Overlay__CloseButton']"
