import allure
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from pages.tabbed import TabbedPage

class MyPlantsPage(TabbedPage):
    driver: webdriver
    
    _water_text_selector = (AppiumBy.ID, 'test:id/my_plants_water_text')
    _water_image_selector = (AppiumBy.ID, 'test:id/my_plants_water_drop')
    _next_watering_title_selector = (AppiumBy.ID, 'test:id/my_plants_title')
    
    _plant_name_selector = (AppiumBy.ID, 'test:id/plant_title')
    _plant_image_selector = (AppiumBy.ID, 'test:id/plant_image')
    _plant_water_label_selector = (AppiumBy.ID, 'test:id/plant_water_label')
    _plant_water_time_selector = (AppiumBy.ID, 'test:id/plant_water_time')
    
    @allure.step('My Plants Page - Check that page is displayed')
    def is_displayed(self):
        return super().is_displayed() and self.element_is_present(self._next_watering_title_selector)
    
    @allure.step('My Plants Page - Check all elements')
    def check_all_elements(self):
        super().check_all_elements()
        self.driver.find_element(*self._water_text_selector)
        self.driver.find_element(*self._water_image_selector)
        self.driver.find_element(*self._next_watering_title_selector)
        return self
    
    @allure.step('My Plants Page - Get all plants')
    def plants(self):
        return self.driver.find_elements(*self._plant_name_selector)
    
    @allure.step('My Plants Page - Get plant name by ID')
    def get_plant_name_by_id(self, id):
        return  self.driver.find_elements(*self._plant_name_selector)[id].text
    
    @allure.step('My Plants Page - Get plant watering time by ID')
    def get_plant_watering_time_by_id(self, id):
        return  self.driver.find_elements(*self._plant_water_time_selector)[id].text