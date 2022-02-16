from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import os
import allure

class BasePage:
    _android_alert_locator = (AppiumBy.ID, 'android:id/alertTitle')
    _android_alert_ok_button_locator = (AppiumBy.ID, 'android:id/button1')
    
    def __init__(self, driver):
        self.driver = driver
        self.platform = self.driver.desired_capabilities['platformName']
        self.implicit_wait = os.environ['implicit_wait']
        
    @allure.step('Check that element is present')
    def element_is_present(self, by, wait=1):
        self.driver.implicitly_wait(wait)
        count = self.driver.find_elements(*by)
        self.driver.implicitly_wait(self.implicit_wait)
        return len(count) > 0
    
    @allure.step('Check alert text')
    def check_alert_text(self):
        if self.platform == 'iOS':
            return self.driver.switch_to.alert.text
        else:
            return self.driver.find_element(*self._android_alert_locator).text
            
    @allure.step('Accept alert')
    def accept_alert(self, wait=3):
        self.driver.implicitly_wait(wait)
        try:
            if self.platform == 'iOS':
                self.driver.switch_to.alert.accept()
            else:
                self.driver.find_element(*self._android_alert_ok_button_locator).click()
            return self
        except:
            raise Exception('Alert not found')
        finally:
            self.driver.implicitly_wait(self.implicit_wait)

    @allure.step
    def log_to_report(self, message):
        print(message)