import allure
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from pages.tabbed import TabbedPage

class AddPlantPage(TabbedPage):
    driver: webdriver
    
    _plants_list_selector = (AppiumBy.ID, 'test:id/plant_select_list')
    _environment_text_selector = (AppiumBy.ID, 'test:id/plant_select_location_text')
    
    _environment_button_selector = (AppiumBy.ID, 'test:id/env_button')
    _plant_name_selector = (AppiumBy.ID, 'test:id/plant_name')
    _plant_image_selector = (AppiumBy.ID, 'test:id/plant_image')
    
    @allure.step('Add Plant Page - Check if page is displayed')
    def is_displayed(self):
        return super().is_displayed() and self.element_is_present(self._plants_list_selector, wait=10)
    
    @allure.step('Add Plant Page - Check all page elements')
    def check_all_elements(self):
        super().check_all_elements()
        self.driver.find_element(*self._plants_list_selector)
        self.driver.find_element(*self._environment_text_selector)
        self.driver.find_element(*self._environment_button_selector)
        return self
    
    @allure.step('Add Plant Page - Get all locations')
    def locations(self):
        return self.driver.find_elements(*self._environment_button_selector)
    
    @allure.step('Add Plant Page - Get all plants')
    def plants(self):
        return self.driver.find_elements(*self._plant_name_selector)
    
    @allure.step('Add Plant Page - Select location by name')
    def select_location_by_name(self, name):
        for location in self.locations():
            if name == location.text:
                location.click()
                return self
        raise Exception('Location {name} not found')
            
    @allure.step('Add Plant Page - Select plant by name')
    def select_plant_by_name(self, name):
        from pages.plant import PlantPage
        for plant in self.plants():
            if name == plant.text.strip():
                plant.click()
                return PlantPage(self.driver)
        raise Exception('Plant {name} not found')

    @allure.step('Add Plant Page - Select plant by ID')
    def select_plant_by_id(self, id):
        self.plants()[id].click()
        from pages.plant import PlantPage
        return PlantPage(self.driver)