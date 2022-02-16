import allure
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from pages.base import BasePage

class UserPage(BasePage):
    driver: webdriver

    _user_name_label_locator = (AppiumBy.ID, 'test:id/user_name_label')
    _user_confirm_button = (AppiumBy.ID, 'test:id/user_confirm_button')
    
    @property
    def _user_name_input_locator(self):
        if self.platform == 'iOS':
            return (AppiumBy.ID, 'test:id/user_name_input')
        else:
            return (AppiumBy.ACCESSIBILITY_ID, 'user_name_input')
    
    @allure.step('User Page - Check that page is displayed')
    def is_displayed(self):
        return self.element_is_present(self._user_name_label_locator)
    
    @allure.step('User Page - Check all elements')
    def check_all_elements(self):
        self.driver.find_element(*self._user_name_label_locator)
        self.driver.find_element(*self._user_name_input_locator)
        self.driver.find_element(*self._user_confirm_button)
        return self
    
    @allure.step('User Page - Enter user name')
    def enter_user_name(self, user_name):
        self.driver.find_element(*self._user_name_input_locator).send_keys(user_name)
        return self
        
    @allure.step('User Page - Get user name')
    def get_user_name(self):
        return self.driver.find_element(*self._user_name_input_locator).text
    
    @allure.step('User Page - Click Confirm')
    def click_confirm(self):
        self.driver.find_element(*self._user_confirm_button).click()
        from pages.confirmation import ConfirmationPage
        return ConfirmationPage(self.driver)
    
