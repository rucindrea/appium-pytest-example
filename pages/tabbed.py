import allure
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from pages.base import BasePage

class TabbedPage(BasePage):
    driver: webdriver
    
    _header_greeting_locator = (AppiumBy.ID, 'test:id/header_greeting')
    _header_image_locator = (AppiumBy.ID, 'test:id/header_user_image')
    
    @property
    def _add_plant_tab_locator(self):
        if self.platform == 'iOS':
            return (AppiumBy.ACCESSIBILITY_ID, 'add_plant_tab')
        else:
            return (AppiumBy.XPATH, "//*[@resource-id='add_plant_tab']")
    
    @property
    def _my_plants_tab_locator(self):
        if self.platform == 'iOS':
            return (AppiumBy.ACCESSIBILITY_ID, 'my_plants_tab')
        else:
            return (AppiumBy.XPATH, "//*[@resource-id='my_plants_tab']")
    
    @allure.step('Check that header and tabs are displayed')
    def is_displayed(self):
        return self.element_is_present(self._header_greeting_locator)

    @allure.step('Check all header and tabs elements')
    def check_all_elements(self):
        self.driver.find_element(*self._header_greeting_locator)
        self.driver.find_element(*self._header_image_locator)
        self.driver.find_element(*self._add_plant_tab_locator)
        self.driver.find_element(*self._my_plants_tab_locator)
        return self
    
    @allure.step('Click Add Plant Tab')
    def click_add_plant_tab(self):
        self.driver.find_element(*self._add_plant_tab_locator).click()
        from pages.add_plant import AddPlantPage
        return AddPlantPage(self.driver)
    
    @allure.step('Click My Plants Tab')
    def click_my_plants_tab(self):
        self.driver.find_element(*self._my_plants_tab_locator).click()
        from pages.my_plants import MyPlantsPage
        return MyPlantsPage(self.driver)
        
    @allure.step('Get header greeting')
    def get_greeting(self):
        return self.driver.find_element(*self._header_greeting_locator).text