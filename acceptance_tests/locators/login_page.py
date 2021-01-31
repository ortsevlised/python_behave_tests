from selenium.webdriver.common.by import By


class LoginPageLocators:
    EMAIL_ADDRESS = By.ID, 'email'
    PASSWORD = By.ID, 'password'
    LOGIN_BTN = By.CSS_SELECTOR, "button[type='submit']"
