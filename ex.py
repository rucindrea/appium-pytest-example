
import allure
import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy


@allure.description("First test for Plant Manager App")
class TestPlantManagerApp:
    driver: webdriver
    
    @allure.title("Test all the things")
    def test_first_screen(self):
        self.driver.find_element_by_id('test:id/welcome_title')
        self.driver.find_element_by_id('test:id/welcome_subtitle')
        self.driver.find_element_by_id('test:id/welcome_start_button').click()
        

        label = self.driver.find_element_by_id('test:id/user_name_label')
        assert label.text == "What's your name?"
        
        if self.driver.desired_capabilities['platformName'] == 'iOS':
            user_name_input = self.driver.find_element_by_id('test:id/user_name_input')
        else:
            user_name_input = self.driver.find_element_by_accessibility_id('user_name_input')
            
        user_name_input.send_keys('John Doe')
        self.driver.find_element_by_id('test:id/user_confirm_button').click()
        
        
        
        title = self.driver.find_element_by_id('test:id/confirmation_title')
        self.driver.find_element_by_id('test:id/confirmation_subtitle')
        assert title.text == 'Ready!'
        self.driver.find_element_by_id('test:id/confirmation_OK_button').click()
        
        greeting = self.driver.find_element_by_id('test:id/header_greeting')
        assert 'John Doe' in greeting.text
        
        self.driver.find_element_by_id('test:id/plant_select_list')
        
        if self.driver.desired_capabilities['platformName'] == 'iOS':
            my_plants_tab = self.driver.find_element_by_accessibility_id("my_plants_tab")
            add_plant_tab = self.driver.find_element_by_accessibility_id("add_plant_tab")
        else:
            my_plants_tab = self.driver.find_element_by_xpath("//*[@resource-id='my_plants_tab']")
            add_plant_tab = self.driver.find_element_by_xpath("//*[@resource-id='add_plant_tab']")
        
        my_plants_tab.click()
        add_plant_tab.click()
        
        plants = self.driver.find_elements(AppiumBy.ID, 'test:id/plant_name')
        plants[0].click()
        self.driver.find_element_by_id('test:id/plant_save_name')
        self.driver.find_element_by_id('test:id/plant_save_about')
        self.driver.find_element_by_id('test:id/plant_save_tip' )
        self.driver.find_element_by_id('test:id/plant_save_button').click()
