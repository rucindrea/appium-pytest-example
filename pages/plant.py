import allure
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from pages.base import BasePage

class PlantPage(BasePage):
    driver: webdriver
    
    _plant_image_locator = (AppiumBy.ID, 'test:id/plant_save_image')
    _plant_name_locator = (AppiumBy.ID, 'test:id/plant_save_name')
    _plant_about_locator = (AppiumBy.ID, 'test:id/plant_save_about')
    _plant_tip_locator = (AppiumBy.ID, 'test:id/plant_save_tip')
    
    _plant_save_button_locator = (AppiumBy.ID, 'test:id/plant_save_button')
    _plant_cancel_button_locator = (AppiumBy.ID, 'test:id/plant_save_cancel_button')
    
    @allure.step('Save Plant Page - Check that page is displayed')
    def is_displayed(self):
        return self.element_is_present(self._plant_name_locator)
    
    @allure.step('Save Plant Page - Check all elements')
    def check_all_elements(self):
        self.driver.find_element(*self._plant_image_locator)
        self.driver.find_element(*self._plant_name_locator)
        self.driver.find_element(*self._plant_about_locator)
        self.driver.find_element(*self._plant_tip_locator)
        self.driver.find_element(*self._plant_save_button_locator)
        self.driver.find_element(*self._plant_cancel_button_locator)
        return self
    
    @allure.step('Save Plant Page - Save Plant')
    def save_plant(self):
        self.driver.find_element(*self._plant_save_button_locator).click()
        try:
            self.accept_alert(wait=5)
        except:
            pass
        from pages.confirmation import ConfirmationPage
        return ConfirmationPage(self.driver)
    
    @allure.step('Save Plant Page - Cancel saving plant')
    def cancel_plant(self):
        self.driver.find_element(*self._plant_cancel_button_locator).click()
        from pages.add_plant import AddPlantPage
        return AddPlantPage(self.driver)
    
    @allure.step('Save Plant Page - Get plant name')
    def get_plant_name(self):
        return self.driver.find_element(*self._plant_name_locator).text