from selenium.webdriver.common.by import By


class NavBarLocators:
    GEAR_ICON = By.CSS_SELECTOR, "i[title = 'Settings']"
    GEAR_MENU_OPTIONS = By.CSS_SELECTOR, "[class*='Dropdown-sc'] a"
