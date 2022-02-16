import allure
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from pages.base import BasePage

class ConfirmationPage(BasePage):
    
    _confirmation_title_locator = (AppiumBy.ID, 'test:id/confirmation_title')
    _confirmation_subtitle_locator = (AppiumBy.ID, 'test:id/confirmation_subtitle')
    _confirmation_ok_button = (AppiumBy.ID, 'test:id/confirmation_OK_button')
    
    @allure.step('Confirmation Page - Check that page is displayed')
    def is_displayed(self):
        return self.element_is_present(self._confirmation_title_locator, wait=5)
    
    @allure.step('Confirmation Page - Check all elements')
    def check_all_elements(self):
        self.driver.find_element(*self._confirmation_title_locator)
        self.driver.find_element(*self._confirmation_subtitle_locator)
        self.driver.find_element(*self._confirmation_ok_button)
        return self
        
    @allure.step('Confirmation Page - Click OK')
    def confirm(self):
        self.driver.find_element(*self._confirmation_ok_button).click()
        from pages.add_plant import AddPlantPage
        return AddPlantPage(self.driver)

    @allure.step('Confirmation Page - Get title')
    def get_title(self):
        return self.driver.find_element(*self._confirmation_title_locator).text
    
    @allure.step('Confirmation Page - Get subtitle')
    def get_subtitle(self):
        return self.driver.find_element(*self._confirmation_subtitle_locator).text
    
    @allure.step('Confirmation Page - Get OK button text')
    def get_ok_button_text(self):
        return self.driver.find_element(*self._confirmation_ok_button).text