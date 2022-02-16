import allure
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from pages.base import BasePage

class WelcomePage(BasePage):
    driver: webdriver
    
    _title_locator = (AppiumBy.ID, 'test:id/welcome_title')
    _subtitle_locator = (AppiumBy.ID, 'test:id/welcome_subtitle')
    _start_button_locator = (AppiumBy.ID, 'test:id/welcome_start_button')
    
    @allure.step('Welcome Page - Check that page is displayed')
    def is_displayed(self):
        return self.element_is_present(self._title_locator)
    
    @allure.step('Welcome Page - Check all elements')
    def check_all_elements(self):
        self.driver.find_element(*self._title_locator)
        self.driver.find_element(*self._subtitle_locator)
        self.driver.find_element(*self._start_button_locator)
        return self
    
    @allure.step('Welcome Page - Click Start button')
    def click_start(self):
        self.driver.find_element(*self._start_button_locator).click()
        from pages.user import UserPage
        return UserPage(self.driver)