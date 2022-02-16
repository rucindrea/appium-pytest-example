
   
import pytest
import os
from appium import webdriver
import allure
from datetime import datetime

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


@pytest.fixture(scope="class", autouse=True)
def driver(request):
    running_platform = os.environ['running_platform']
    capabilities = {}
    if running_platform.lower() == 'ios':
        capabilities = {
            'platformName':     'iOS',
            'deviceName':       'iPhone 13',
            'app':              PATH('apps/plant-manager.app.zip'),
            'automationName':     'XCUITest'
        }
    else:
        capabilities = {
            'platformName':     'android',
            'deviceName':       'android-device',
            'app':              PATH('apps/plant-manager.apk'),
            'automationName':     'UiAutomator2'
        }
    
    url = 'http://localhost:4723/wd/hub'
    request.cls.driver = webdriver.Remote(url, capabilities)
    request.cls.driver.implicitly_wait(10)
    yield request.cls.driver
    
    request.cls.driver.quit()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)

@pytest.fixture(scope="function", autouse=True)
@allure.title("Config: Set driver to take screenshot on failure")
def screenshot_on_failure(request):
    yield
    if request.node.rep_setup.failed or request.node.rep_call.failed:
        try:
            driver = request.cls.driver
            name = request.function.__name__
            date = "_" + str(datetime.now().strftime("%Y-%m-%d_%H:%M"))
            allure.attach(driver.get_screenshot_as_png(),
                          name="screenshot_" + name + date,
                          attachment_type=allure.attachment_type.PNG)
        except Exception:
            pass