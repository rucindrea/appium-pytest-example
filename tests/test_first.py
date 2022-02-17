
import allure
import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

class TestPlantManagerApp:
    driver: webdriver
    
    def test_first_screen(self):
        pass