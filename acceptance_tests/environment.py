from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


def before_all(context):
    """
    Setting up the browser
    """
    context.driver = select_browser(context)
    context.driver.set_page_load_timeout(10)
    context.driver.implicitly_wait(10)
    context.driver.maximize_window()
    context.config.setup_logging()


def select_browser(context):
    """
    Selects the browser to user according the the argument passed to the behave runner
    if no one is passed it will run the remote webdriver by default
    """
    browser = context.config.userdata.get('browser')
    if not browser:
        browser = 'remote'
    if browser.lower() == 'remote':
        capabilities = {
            "browserName": "chrome",
            "browserVersion": "88.0",
            "selenoid:options": {
                "enableVNC": True,
                "enableVideo": False,
                "screenResolution": "1280x1024x24"
            }
        }
        return webdriver.Remote(command_executor="https://perfect-fly-85.loca.lt/wd/hub",
                                desired_capabilities=capabilities)
    elif browser.lower() == 'chrome':
        return webdriver.Chrome(ChromeDriverManager().install())
    elif browser.lower() == 'headlesschrome':
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        return webdriver.Chrome(ChromeDriverManager().install(), options=options)
    elif browser.lower() in ('ff', 'firefox'):
        return webdriver.Firefox(GeckoDriverManager().install())
    else:
        raise Exception("The browser type '{}' is not supported".format(context))


def after_all(context):
    context.driver.quit()
