
import allure
import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy


@allure.description("First test for Plant Manager App")
class TestPlantManagerApp:
    driver: webdriver
    
    @allure.title("Test all the things")
    def test_first_screen(self):
        pass